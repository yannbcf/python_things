from typing import Callable
import time

def measure_time(func: Callable) -> Callable:
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time_ms = (end_time - start_time) * 1000
        print(f"{func.__name__} took {execution_time_ms:.2f} ms to execute")
        return result

    return wrapper

@measure_time
def slow_function():
    time.sleep(2)

if __name__ == "__main__":
    slow_function()
