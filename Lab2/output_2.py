class Phone:
    """
    Репрезентує номер телефону користувача.
    """
    def __init__(self, code, number):
        self.code = code
        self.number = number

    def __str__(self):
        """
        Повертає повний номер телефону у форматі +[код][номер].
        """
        return f"+{self.code}{self.number}"


class User:
    """
    Репрезентує дані користувача.
    """
    TYPE_ENGINEER = 1
    TYPE_MANAGER = 2    

    def __init__(self, name, age, type, phone: Phone):
        self.name = name
        self.age = age
        self.type = type
        self.phone = phone

    def print_details(self):
        """
        Виводить інформацію про користувача.
        """
        print("Name:", self.name)
        print("Age:", self.age)
        print("Type:", self.type)
        print("Phone:", self.phone)


# Приклад використання класу
phone = Phone("38050", "9379992")
user = User("John", 25, User.TYPE_ENGINEER, phone)
user.print_details()