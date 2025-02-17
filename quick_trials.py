print('hello')

weather: str = 'sunny sunny'
num: int = 90

data: dict[str, int] = {
    'bob': 1,
    'sarah': 2
}

sacha: bool = True
jhootha: bool = False

ghantha: None = None

print('ghantha salaa', ghantha)


def add(a: int, b: int) -> int:
    return a + b


class Person:
    name: str
    age: int

    def __init__(self, name: str, age: int) -> None:  # purana tarikka
        self.name = name
        self.age = age


# ----------------------------------------------
upper_case: str = 'Roadmap to become MLOps engineer in 3 months'
print(upper_case.upper())


lower_case: str = 'Roadmap to become MLOps engineer in 3 months'
print(lower_case.lower()) 

from pathlib import Path
print(Path(__file__).parent)


