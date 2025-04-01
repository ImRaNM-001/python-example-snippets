from ensure import ensure_annotations, EnsureError

def multiply(a: int, b: int) -> int:
    return a * b

print(multiply(3, '7'))     # due to str type of '7' at runtime, no error is thrown rather python repeats '7' thrice i.e, 3 times outputing the result as 777


# @ensure_annotations                   # WRONG SYNTAX
# multiply_ = lambda a, b : a * b
"""
    NOTE: Applying a decorator (@ensure_annotations) to a lambda function directly, is not allowed in Python syntax. Decorators can only be applied to function definitions (using the def keyword) and class definitions, not to lambda functions or assignments.
"""

# Option 1: using lambda - define the lambda first and then apply the decorator to it afterward - I don't prefer this as types are not controlled, expected "exception messages" as below are not called
multiply_ = lambda a, b : a * b
multiply_ =  ensure_annotations(multiply_)           


# Option 2: Define a regular function instead of a lambda and apply the decorator
@ensure_annotations                      # type: ignore
def multiply_(a: int, b: int) -> int:
    return a * b

try:
    print(multiply_(3, '7'))        # prints 777

except EnsureError as error:
    print(error)                    # Argument b of type <class 'str'> to <function multiply_ at 0x1031a4fe0> does not match annotation type <class 'int'>

print(multiply_(3, 7))          # prints 21
