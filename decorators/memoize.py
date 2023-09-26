from typing import Callable

from measure import measure_time
from functools import lru_cache

def memoize(func: Callable[[int], int]) -> Callable:
    cache = {}

    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)

        return cache[args]
    
    return wrapper

@memoize
@measure_time
def fibonacci(n: int) -> int:
    return n if n <= 1 else fibonacci(n - 1) + fibonacci(n - 2)

@lru_cache(maxsize=None)
@measure_time
def lru_fibonacci(n: int) -> int:
    return n if n <= 1 else fibonacci(n - 1) + fibonacci(n - 2)

if __name__ == "__main__":
    print(fibonacci(10))
    print(lru_fibonacci(10))
