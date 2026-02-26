import re
from typing import Callable, Generator


def generator_numbers(text: str) -> Generator[float, None, None]:
    """
    Анализирует текст и возвращает генератор действительных чисел,
    которые отделены пробелами.
    """
    for word in text.split():
        try:
            yield float(word)
        except ValueError:
            continue


def sum_profit(text: str, func: Callable) -> float:
    """
    Принимает текст и функцию-генератор, суммирует все числа и возвращает итог.
    """
    total = 0.0
    for number in func(text):
        total += number
    return total


text = "Загальний дохід працівника складається з декількох частин: 900.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."

total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")
