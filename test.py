from math import sqrt

message: str = """Добро пожаловать в самую лучшую программу для
вычисления квадратного корня из заданного числа"""

print(message)


def calculatesquareroot(number: float) -> float:
    """Вычисляет квадратный корень."""
    return sqrt(number)


def calc(your_number: float) -> None:
    """Description"""
    if your_number <= 0:
        return
    else:
        number = calculatesquareroot(your_number)
        return print(f'Мы вычислили квадратный корень из введённого вами числа'
                     f'. Это будет: {number}')


print(message)
calc(25.5)
