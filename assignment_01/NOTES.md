# AI Use Notes

## Tool used

ChatGPT / Codex

## Questions discussed

These questions summarize the debugging topics discussed, rather than reproduce every original prompt.

1. What does this error mean? `AttributeError: 'AirConditioner' object has no attribute 'fan'`
2. Why does assigning to `self.temperature` inside the temperature setter cause a `RecursionError`?
3. Why does storing the value in `self._temperature` avoid calling the setter again?
4. Why should `is_energy_saving` be calculated from the current temperature?
5. Why does the temperature range check require `or` instead of `and`?
6. Why must the constructor use the temperature setter?
7. How can `cooler()` avoid reducing the temperature below the minimum?

## What I learned

- Attribute names must match exactly.
- The temperature setter must write to its backing attribute to avoid calling itself repeatedly.
- Validation must reject values below the minimum or above the maximum.
- The constructor should use the validated temperature setter instead of bypassing it.
- Calculating energy-saving status from the current temperature prevents an outdated result.
- Boundary checks prevent methods from creating invalid state.

## Disclosure

AI explained the errors, and suggested specific code changes.
