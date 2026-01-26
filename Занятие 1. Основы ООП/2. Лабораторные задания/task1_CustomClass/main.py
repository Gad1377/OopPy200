import doctest


class Tree:
    def __init__(self, height: float, age: int):
        """
        Дерево с заданной высотой и возрастом.

        :param height: Высота дерева в метрах.
        :param age: Возраст дерева в годах.
        """
        if not isinstance(height, (float, int)) or height <= 0:
            raise ValueError('Высота дерева должна быть положительной')
        if not isinstance(age, int) or age < 0:
            raise ValueError('Возраст дерева должен быть неотрицательным целым числом')
        self.height = height
        self.age = age

    def grow(self, years: int) -> None:
        """
        Увеличивает возраст дерева на указанное число лет.

        :param years: Количество лет роста.
        """
        if not isinstance(years, int) or years < 0:
            raise ValueError('Годы роста должны быть положительными целыми числами.')
        self.age += years

    def cut_down(self) -> str:
        """
        Возвращает сообщение о вырубке дерева.
        """
        return f'Дерево было вырублено'





class Chair:
    def __init__(self, height: float, material: str):
        """
        Стул с з высотой и материалом изготовления.

        :param height: Высота стула в сантиметрах.
        :param material: Материал изготовления стула
        """
        if not isinstance(height, (float, int)) or height <= 0:
            raise ValueError("Высота стула должна быть положительным числом.")
        if not isinstance(material, str) or len(material.strip()) == 0:
            raise ValueError("Материал стула должен быть строкой.")
        self.height = height
        self.material = material

    def adjust_height(self, new_height: float) -> None:
        """
        Изменяет высоту стула .

        :param new_height: Новая высота стула в сантиметрах.
        """
        if not isinstance(new_height, (float, int)) or new_height <= 0:
            raise ValueError("Высота стула должна быть положительным числом.")
        self.height = new_height

    def break_chair(self) -> str:
        """
        Возвращает сообщение о поломке стула.
        """
        return f"Сломался стул"


class TelegramUser:
    def __init__(self, name: str, email: str):
        """
        Создает новый аккаунт пользователя на Telegram.

        :param name: Имя пользователя.
        :param email: Адрес электронной почты пользователя.
        """
        if not isinstance(name, str) or len(name.strip()) == 0:
            raise ValueError('Имя пользователя должно быть строкой и не пустым')
        if '@' not in email:
            raise ValueError('Email адрес должен содержать символ "@"')
        self.name = name
        self.email = email
        self.friends = set()

    def add_friend(self, friend_email: str) -> None:
        """
        Добавляет друга по адресу электронной почты.

        :param friend_email: Email друга.
        """
        if '@' not in friend_email:
            raise ValueError('Адрес друга должен содержать символ "@"')
        self.friends.add(friend_email)

    def count_friends(self) -> int:
        """
        Подсчет количества друзей.
        """
        return len(self.friends)


if __name__ == '__main__':
    doctest.testmod()
