"""
    Calculates the nth Fibonacci number recursively.

    Args: 
        n: The position in the sequence (starting from 0).

    Returns: The nth Fibonacci number.
"""


def fibonacci(num: int) -> int:
    return num if num <= 1 else fibonacci(num - 1) + fibonacci(num - 2)

for _ in range(10):
    print(fibonacci(_), end = ' ')
print()                                   # Adding print() at the end ensures that the output ends with a newline character, which might help avoid any trailing characters like %.
    
    
    
    
    



