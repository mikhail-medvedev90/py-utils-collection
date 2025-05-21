def strict(func: callable) -> callable:
    """
    Декоратор для строгой проверки типов аргументов функции согласно её аннотациям.
    При вызове обёрнутой функции проверяет, что каждый переданный аргумент соответствует
    ожидаемому типу, указанному в аннотациях функции.
    Если тип аргумента не совпадает с аннотацией, выбрасывается исключение TypeError
    с информативным сообщением.

    Аргументы:
        func (Callable): Функция, которую нужно обернуть проверкой типов.

    Возвращает:
        Callable: Обёрнутую функцию с проверкой типов.
    """

    def wrapper(*args: tuple) -> any:
        annotations = func.__annotations__
        for arg, annotation in zip(args, annotations.items()):
            name, expected_type = annotation
            if not isinstance(arg, expected_type):
                raise TypeError(f"Аргумент {name} ожидается {expected_type}, а получен {type(arg)}")
        return func(*args)
    return wrapper

@strict
def sum_two(a: int, b: int) -> int:
    """Складывает два целых числа. Возвращает: int: Сумма a и b."""
    return a + b
