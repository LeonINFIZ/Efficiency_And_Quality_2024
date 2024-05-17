class User:
    """
    Репрезентує дані користувача.
    """
    def __init__(self, name, age, gender, height, weight):
        self.name = name
        self.age = age
        self.gender = gender
        self.height = height
        self.weight = weight


class Scores:
    """
    Репрезентує оцінки користувача.
    """
    def __init__(self, score1, score2, score3, score4, score5):
        self.scores = [score1, score2, score3, score4, score5]

    def calculate_total_score(self):
        """
        Розраховує загальний рейтинг користувача.
        """
        return sum(self.scores)


def is_adult(age):
    """
    Визначає, чи є користувач повнолітнім.
    """
    return age >= 18


def print_results(user, total_score, adult):
    """
    Виводить результати обробки даних користувача.
    """
    print("Name:", user.name)
    print("Age:", user.age)
    print("Gender:", user.gender)
    print("Height:", user.height)
    print("Weight:", user.weight)
    print("Total Score:", total_score)
    print("Adult:", adult)


# Приклад використання
user = User("John", 25, "Male", 175, 70)
scores = Scores(85, 90, 75, 88, 92)
total_score = scores.calculate_total_score()
adult = is_adult(user.age)
print_results(user, total_score, adult)