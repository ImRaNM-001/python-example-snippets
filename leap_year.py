def is_leap_year(year: int) -> bool:
    """
    Check if a given year is a leap year.

    A year is a leap year if:
    - It is divisible by 4, and
    - It is not divisible by 100, unless it is also divisible by 400.

    Args:
    year (int): The year to check.

    Returns:
    bool: True if the year is a leap year, False otherwise.
    """
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

# Example usage
year: int = int(input('Enter a year: '))
print(f'{year} is a leap year: {is_leap_year(year)}')