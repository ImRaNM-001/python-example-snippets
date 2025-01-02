# Ex: 1
class Calculator:
    # def add(self, a: int, b: int = 0, c: int = 0) -> int:
    #     return a + b + c

    add = lambda self, a = 0, b= 0, c = 0: a + b + c

calc: Calculator = Calculator()
print(calc.add(5))                      # Output: 5 (b and c take default value 0)
print(calc.add(5, 3))                   # Output: 8
print(calc.add(5, 3, 2))                # Output: 10



# Ex: 2
class MathUtils:
    def process_numbers(self, *args: tuple[int, ...]) -> int:
        result: int = 0
        for num in args:
            result += num
        return result

math_utils: MathUtils = MathUtils()
print(math_utils.process_numbers(1, 2, 3))                  # Output: 6
print(math_utils.process_numbers(1, 2, 3, 4, 5))             # Output: 15


# Ex: 3
class Person:
  def greet(self, **kwargs: dict[str, object]) -> None:
    for key, value in kwargs.items():
      print(f'{key}: {value}')

person = Person()
person.greet(name = 'John', age = 30) # Output: name: John \n age: 30