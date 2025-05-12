from ensure import ensure_annotations, EnsureError

# 1> raw code - without exception handling
def multiply(a: int, b: int) -> int:
    return a * b

print('1> ', multiply(3, '7'))             # due to str type of '7' at runtime, no error is thrown rather python repeats '7' thrice i.e, 3 times outputing the result as 777


# 2> with proper exception handling
def multiply(a: int, b: int) -> int:
    if not isinstance(a, int):
        raise TypeError(f"Expected 'a' to be int, got {type(a).__name__}")
    if not isinstance(b, int):
        raise TypeError(f"Expected 'b' to be int, got {type(b).__name__}")
    return a * b

try:
    print('2> ', multiply(3, '10'))         

except TypeError as error:
    print(f'2>.. Error: {error}')                # Error: Expected 'b' to be int, got str



# @ensure_annotations                   # WRONG SYNTAX
# multiply_ = lambda a, b : a * b
"""
    NOTE: Applying a decorator (@ensure_annotations) to a lambda function directly, is not allowed in Python syntax. 
    Decorators can only be applied to function definitions (using the def keyword) and class definitions, not to lambda functions or assignments.
"""

# Option 1: using lambda - define the lambda first and then apply the decorator to it afterward - I don't prefer this as types are not controlled, expected "exception messages" as below are not called
multiply_ = lambda a, b : a * b
multiply_ =  ensure_annotations(multiply_)           


# 3> using external library "ensure" - Option 2: Define a regular function instead of a lambda and apply the decorator
@ensure_annotations                      # type: ignore
def multiply_(a: int, b: int) -> int:
    if not isinstance(a, int) or not isinstance(b, int):
        raise EnsureError
    else:
        return a * b

print('3> ', multiply_(3, 7))          # prints 21

try:
    print('4> ', multiply_(3, '71'))        # prints 777

except EnsureError as error:
    print(f'4> {error}')                    # Argument b of type <class 'str'> to <function multiply_ at 0x1031a4fe0> does not match annotation type <class 'int'>

