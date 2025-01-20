"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*nums):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """
    return [x**2 for x in nums]


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"

def is_prime(number):
    i = 2
    while number % i != 0 and i <= number:
        i += 1
    return i == number


def filter_numbers(*args):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """
    num_list, arg=args
    if arg==ODD:
        result=[x for x in num_list if x%2]
    elif arg==EVEN:
        result=[x for x in num_list if x%2==0]
    elif arg==PRIME:
        result=[x for x in num_list if is_prime(x)]
    return result
