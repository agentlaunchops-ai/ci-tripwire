import test from 'node:test';
import assert from 'node:assert/strict';
import { calculateBudget } from '../public/js/local-publication-planner.mjs';
const baseline = { setup: 1200, monthly: 50, growth: 25, hours: 3, hourly: 20, sponsor: 150, months: 12 };
test('combines cash, annualized weekly labor, and setup recovery without forecasting sales', () => {
  const result = calculateBudget(baseline);
  assert.equal(result.cash, 75); assert.equal(result.labor, 260);
  assert.equal(result.setupRecovery, 100); assert.equal(result.target, 435);
  assert.equal(result.placements, 3);
});
test('zero sponsor price leaves the placement count unset', () => assert.equal(calculateBudget({ ...baseline, sponsor: 0 }).placements, null));
test('zero costs require zero placements', () => assert.equal(calculateBudget({ setup: 0, monthly: 0, growth: 0, hours: 0, hourly: 0, sponsor: 10, months: 12 }).placements, 0));
test('fractional cost coverage rounds up', () => assert.equal(calculateBudget({ ...baseline, sponsor: 100 }).placements, 5));
test('exact cent boundaries do not add a placement through floating-point error', () => {
  assert.equal(calculateBudget({ setup: 0, monthly: 10, growth: 5.03, hours: 0, hourly: 0, sponsor: 15.03, months: 12 }).placements, 1);
  assert.equal(calculateBudget({ setup: 0, monthly: .1, growth: .2, hours: 0, hourly: 0, sponsor: .3, months: 12 }).placements, 1);
});
test('fractional setup recovery and weekly labor retain exact placement boundaries', () => {
  assert.equal(calculateBudget({ setup: 1, monthly: 0, growth: 0, hours: 0, hourly: 0, sponsor: .01, months: 3 }).placements, 34);
  assert.equal(calculateBudget({ setup: 0, monthly: 0, growth: 0, hours: .03, hourly: 1, sponsor: .13, months: 12 }).placements, 1);
});
test('fractional cents are rejected instead of silently rounding assumptions', () => assert.throws(() => calculateBudget({ ...baseline, sponsor: 1.001 }), RangeError));
test('rejects invalid financial values instead of showing misleading totals', () => {
  for (const key of Object.keys(baseline)) for (const value of [-1, NaN, Infinity, 1000001, '10', null]) assert.throws(() => calculateBudget({ ...baseline, [key]: value }), RangeError);
  for (const months of [0, .5, 1.5]) assert.throws(() => calculateBudget({ ...baseline, months }), RangeError);
});
