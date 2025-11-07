from icontract import require, ensure
import math

@require(lambda x: x >= 0, "x must be non-negative")
@ensure(lambda result, x: result <= x, "result must be at most x")
def sqrt_roundup(x: float) -> int:
    return math.ceil(math.sqrt(x))

# a simple test...
sqrt_roundup(8)
