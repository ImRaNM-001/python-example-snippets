# how to skip writing constructor:

# case 1- ultimate one-selected
from dataclasses import dataclass

@dataclass
class MyClass:
    name: str
    age: int
    is_active: bool

    def greet(self: 'MyClass') -> str:
        return f'Hello, my name is {self.name}, I\'m {self.age} years old and I\'m a {self.is_active} legend.'
    
# Create an instance of MyClass
my_class: MyClass = MyClass('Alice', 30, True)

# Call the greet() method and print the result
print(my_class.greet())              # Output: Hello, my name is Alice, I am 30 years old and I'm a True legend



# case 2- declaring constructor usual / traditional way - skipped
class MyClass_1:
    def __init__(self, name: str, age: int, is_active: bool) -> None:
        self.name: str = name
        self.age: int = age
        self.is_active: bool = is_active

    def greet_1(self) -> str:
        return f'Hello, my name is {self.name} and I am {self.age} years old.'


# case 3- write all in 1 line and also added type for self - skipped
class MyClass_2:
    def __init__(self, name: str, age: int, is_active: bool) -> None:
        self.name: str; self.age: int; self.is_active: tuple[str, int, bool] = name, age, is_active

    def greet_2(self: "MyClass_2") -> str:
        return f'Hello, my name is {self.name} and I am {self.age} years old.'
