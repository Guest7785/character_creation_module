from math import sqrt

message = ('Добро пожаловать в самую лучшую программу для вычисления '
           'квадратного корня из заданного числа')
print(message)


def calculate_square_root(number):
    """Вычисляет квадратный корень."""
    return sqrt(number)


def calc(your_number):
    """Проверяет."""
    if your_number <= 0:
        return


root = 25.5
result = calculate_square_root(root)
print(f'Мы вычислили квадратный корень из введённого вами числа. '
      f'Это будет: {result} ')


calc(root)
