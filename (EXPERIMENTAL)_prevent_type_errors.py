from typing import List, TypeVar, Generic, Any

T = TypeVar('T')

class TypedList(Generic[T], List[T]):
    def __init__(self, *args: T) -> None:
        super().__init__(args)
        self._check_types()

    def __setitem__(self, index: int, value: T) -> None:
        self._check_type(value)
        super().__setitem__(index, value)

    def append(self, value: T) -> None:
        self._check_type(value)
        super().append(value)

    def extend(self, values: List[T]) -> None:
        for value in values:
            self._check_type(value)
        super().extend(values)

    def insert(self, index: int, value: T) -> None:
        self._check_type(value)
        super().insert(index, value)

    def _check_type(self, value: Any) -> None:
        if not isinstance(value, self._type):
            raise TypeError(f"Expected type {self._type.__name__}, got {type(value).__name__}")

    def _check_types(self) -> None:
        for item in self:
            self._check_type(item)

    @property
    def _type(self) -> type:
        return self.__orig_class__.__args__[0]

# Example usage
if __name__ == "__main__":
    # Create a list of integers
    int_list = TypedList[int](1, 2, 3, 4, 5)
    print(int_list)

    # This will raise a TypeError
    try:
        int_list[2] = 'kal kal'
    except TypeError as e:
        print(e)

    # This will also raise a TypeError
    try:
        int_list.append('hello')
    except TypeError as e:
        print(e)

    # Create a list of strings
    str_list = TypedList[str]("a", "b", "c")
    print(str_list)

    # This will raise a TypeError
    try:
        str_list[1] = 123
    except TypeError as e:
        print(e)



""" by pieces AI
from typing import Any, TypeVar, Generic, Type

T = TypeVar('T')

class TypedVariable(Generic[T]):
    def __init__(self, value: T, expected_type: Type[T]) -> None:
        self._expected_type = expected_type
        self.value = value

    @property
    def value(self) -> T:
        return self._value

    @value.setter
    def value(self, new_value: T) -> None:
        if not isinstance(new_value, self._expected_type):
            raise TypeError(f"Expected value of type {self._expected_type.__name__}, got {type(new_value).__name__}")
        self._value = new_value

# Example usage
if __name__ == "__main__":
    # Initialize with an integer
    int_var = TypedVariable(10, int)
    print(int_var.value)  # Output: 10

    # Re-initialize with a valid type
    int_var.value = 20
    print(int_var.value)  # Output: 20

    # Attempt to re-initialize with an invalid type
    try:
        int_var.value = "string"  # This will raise a TypeError
    except TypeError as e:
        print(e)  # Output: Expected value of type int, got str

    # Initialize with a list
    list_var = TypedVariable([1, 2, 3], list)
    print(list_var.value)  # Output: [1, 2, 3]

    # Re-initialize with a valid type
    list_var.value = [4, 5, 6]
    print(list_var.value)  # Output: [4, 5, 6]

    # Attempt to re-initialize with an invalid type
    try:
        list_var.value = 123  # This will raise a TypeError
    except TypeError as e:
        print(e)  # Output: Expected value of type list, got int

"""