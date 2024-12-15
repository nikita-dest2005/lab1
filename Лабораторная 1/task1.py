# TODO Написать 3 класса с документацией и аннотацией типов
import doctest


class Tree:
    def __init__(self, height: float, age: int):
        """
        Создание и подготовка к работе объекта "Дерево"

        :param height: Высота дерева в метрах
        :param age: Возраст дерева в годах

        Примеры:
        >>> oak = Tree(5.5, 20)
        """
        if not isinstance(height, (int, float)):
            raise TypeError("Высота дерева должна быть типа int или float")
        if height <= 0:
            raise ValueError("Высота дерева должна быть положительным числом")
        self.height = height

        if not isinstance(age, int):
            raise TypeError("Возраст дерева должен быть типа int")
        if age < 0:
            raise ValueError("Возраст дерева не может быть отрицательным числом")
        self.age = age

    def grow(self, years: int) -> None:
        """
        Увеличение высоты дерева на основе возраста.

        :param years: Количество лет, на которое дерево будет расти

        Примеры:
        >>> oak = Tree(5.5, 20)
        >>> oak.grow(5)
        """
        ...

    def shed_leaves(self) -> None:
        """
        Сбрасывание листвы дерева.

        Примеры:
        >>> oak = Tree(5.5, 20)
        >>> oak.shed_leaves()
        """
        ...


class Car:
    def __init__(self, model: str, year: int):
        """
        Создание и подготовка к работе объекта "Автомобиль"

        :param model: Модель автомобиля
        :param year: Год выпуска автомобиля

        Примеры:
        >>> toyota = Car("Toyota Camry", 2020)
        """
        if not isinstance(model, str):
            raise TypeError("Модель должна быть строкой")
        if not model:
            raise ValueError("Модель не может быть пустой строкой")
        self.model = model

        if not isinstance(year, int):
            raise TypeError("Год должен быть типа int")
        if year < 1886:  # Первый автомобиль был создан в 1886
            raise ValueError("Год выпуска не может быть раньше 1886")
        self.year = year

    def start_engine(self) -> None:
        """
        Запуск двигателя автомобиля.

        Примеры:
        >>> toyota = Car("Toyota Camry", 2020)
        >>> toyota.start_engine()
        """
        ...

    def stop_engine(self) -> None:
        """
        Остановка двигателя автомобиля.

        Примеры:
        >>> toyota = Car("Toyota Camry", 2020)
        >>> toyota.stop_engine()
        """
        ...


class Facebook:
    def __init__(self, username: str, friends_count: int):
        """
        Создание и подготовка к работе объекта "Facebook"

        :param username: Имя пользователя
        :param friends_count: Количество друзей

        Примеры:
        >>> user = Facebook("john_doe", 150)
        """
        if not isinstance(username, str):
            raise TypeError("Имя пользователя должно быть строкой")
        if not username:
            raise ValueError("Имя пользователя не может быть пустой строкой")
        self.username = username

        if not isinstance(friends_count, int):
            raise TypeError("Количество друзей должно быть типа int")
        if friends_count < 0:
            raise ValueError("Количество друзей не может быть отрицательным числом")
        self.friends_count = friends_count

    def add_friend(self) -> None:
        """
        Добавление друга.

        Примеры:
        >>> user = Facebook("john_doe", 150)
        >>> user.add_friend()
        """
        ...

    def remove_friend(self) -> None:
        """
        Удаление друга.

        Примеры:
        >>> user = Facebook("john_doe", 150)
        >>> user.remove_friend()
        """
        ...


if name == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации
    pass
