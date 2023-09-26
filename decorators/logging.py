from typing import Callable

def log_function_call(func: Callable) -> Callable:
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"Calling {func.__name__} with args={args}, kwargs={kwargs}, result={result}")
        return result

    return wrapper

@log_function_call
def add(a: int, b: int) -> int:
    return a + b

if __name__ == "__main__":
    add(3, 4)
