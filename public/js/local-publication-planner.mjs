export function calculateBudget(values) {
  const fields = ['setup', 'monthly', 'growth', 'hours', 'hourly', 'sponsor', 'months'];
  for (const name of fields) {
    if (typeof values[name] !== 'number' || !Number.isFinite(values[name]) || values[name] < 0 || values[name] > 1000000) {
      throw new RangeError('Enter finite, non-negative amounts below 1,000,001.');
    }
  }
  if (values.months < 1 || !Number.isInteger(values.months)) throw new RangeError('Recovery months must be a whole number of at least 1.');
  const scaled = {};
  for (const name of fields.filter(name => name !== 'months')) {
    const hundredths = Math.round(values[name] * 100);
    if (Math.abs(values[name] * 100 - hundredths) > 0.0000001) throw new RangeError('Use no more than two decimal places.');
    scaled[name] = BigInt(hundredths);
  }
  // Exact rational cents prevent binary floating-point error from adding a placement.
  const months = BigInt(values.months);
  const denominator = 1200n * months;
  const cashCents = scaled.monthly + scaled.growth;
  const laborNumerator = scaled.hours * scaled.hourly * 52n;
  const targetNumerator = cashCents * denominator + laborNumerator * months + scaled.setup * 1200n;
  const placementDenominator = scaled.sponsor * denominator;
  const cash = Number(cashCents) / 100;
  const labor = Number(laborNumerator) / 120000;
  const setupRecovery = Number(scaled.setup) / values.months / 100;
  const target = Number(targetNumerator) / Number(denominator) / 100;
  const placements = scaled.sponsor > 0n ? Number((targetNumerator + placementDenominator - 1n) / placementDenominator) : null;
  return { cash, labor, setupRecovery, target, placements };
}

if (typeof document !== 'undefined') {
  const form = document.querySelector('#publication-planner');
  const money = value => new Intl.NumberFormat('en-US', { style: 'currency', currency: 'USD' }).format(value);
  const numericFields = ['setup', 'monthly', 'growth', 'hours', 'hourly', 'sponsor', 'months'];
  let budget;
  function update() {
    try {
      const values = Object.fromEntries(numericFields.map(name => {
        const input = form.elements.namedItem(name);
        return [name, input.value.trim() === '' ? NaN : input.valueAsNumber];
      }));
      budget = calculateBudget(values);
      document.querySelector('#cash-total').textContent = money(budget.cash);
      document.querySelector('#labor-total').textContent = money(budget.labor);
      document.querySelector('#recovery-total').textContent = money(budget.setupRecovery);
      document.querySelector('#budget-total').textContent = money(budget.target);
      document.querySelector('#placements-total').textContent = budget.placements === null ? 'Enter a net placement price' : String(budget.placements);
      document.querySelector('#planner-error').textContent = '';
      document.querySelector('#download-plan').disabled = false;
    } catch (error) {
      budget = null;
      for (const id of ['cash-total', 'labor-total', 'recovery-total', 'budget-total', 'placements-total']) document.getElementById(id).textContent = 'Check inputs';
      document.querySelector('#planner-error').textContent = error.message;
      document.querySelector('#download-plan').disabled = true;
    }
  }
  form.addEventListener('input', update);
  form.addEventListener('submit', event => event.preventDefault());
  document.querySelector('#download-plan').addEventListener('click', () => {
    update();
    if (!budget || !form.reportValidity()) return;
    const textFields = ['market', 'promise', 'issue', 'sources', 'demo'];
    const lines = ['LOCAL PUBLICATION WORKSHEET', 'Planning assumptions only. This is not an earnings forecast.', '', ...textFields.map(name => `${form.elements.namedItem(name).labels[0].textContent}: ${form.elements.namedItem(name).value || '(not filled in)'}`), '', 'BUDGET ASSUMPTIONS (USD)', ...numericFields.map(name => `${form.elements.namedItem(name).labels[0].textContent}: ${form.elements.namedItem(name).value}`), '', `Monthly cash expenses: ${money(budget.cash)}`, `Monthly labor allowance: ${money(budget.labor)}`, `Monthly setup recovery: ${money(budget.setupRecovery)}`, `Monthly cost target: ${money(budget.target)}`, `Placements to cover modeled costs: ${budget.placements === null ? 'No net placement price entered' : budget.placements}`, '', 'MODEL: Cash = operating cost + audience growth budget. Labor = weekly hours x hourly value x 52 / 12. Setup recovery = setup cost / recovery months. Cost target = cash + labor + setup recovery. Placements = cost target / net placement amount, rounded up.', 'Dollar totals are displayed rounded to cents. Placement counts use unrounded totals.', 'Assumes a constant weekly workload across 52 weeks, spread across 12 months. Omits taxes, financing, and costs not entered. Placement amounts are net of direct fees and delivery costs.', '', 'WORKFLOW CHECKS', ...Array.from(form.querySelectorAll('input[type=checkbox]')).map(input => `${input.checked ? '[x]' : '[ ]'} ${input.labels[0].textContent.trim()}`), '', 'Affiliate promotion: CI Tripwire may earn a commission on purchases through its Local Media Empire link.', 'Product checklist: https://dsotn.com/articles/local-media-empire-publishing-checklist/'];
    const url = URL.createObjectURL(new Blob([lines.join('\n')], { type: 'text/plain;charset=utf-8' }));
    const link = document.createElement('a');
    link.href = url; link.download = 'local-publication-plan.txt';
    document.body.append(link); link.click(); link.remove();
    setTimeout(() => URL.revokeObjectURL(url), 1000);
    document.querySelector('#download-status').textContent = 'Your worksheet download has been requested.';
  });
  update();
}
