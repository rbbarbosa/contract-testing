# contract-testing

Exploring Design by Contract in Python with icontract, pytest, and hypothesis -- runtime contract enforcement meets property-based testing.

Run `pytest` to test the contract in [`python_contract.py`](python_contract.py) and find the counterexample:

```
E       Falsifying example: test_sqrt_roundup_contracts(
E           x=0.0,
E       )
```
