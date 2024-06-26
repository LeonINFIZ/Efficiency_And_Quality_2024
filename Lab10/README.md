Рефакторинг коду: розширення функціональності бібліотечних класів

Завдання 1:

Проблема: Клас BasicCalculator мав обмежену функціональність - відсутні методи для множення та ділення.

Рішення:

1. Створення підкласу AdvancedCalculator: створено підклас AdvancedCalculator, який успадковує від BasicCalculator та додає методи multiply та divide.

Виграш:

-Розширення функціональності: клас AdvancedCalculator надає повний набір операцій калькулятора.
-Збереження базового класу: клас BasicCalculator залишається незмінним.

Завдання 2:

Проблема: Клас LibraryBook надавав лише базові функції - відсутні методи для отримання детальної інформації про книгу.

Рішення:

1. Введення класу BookDetails: створено клас BookDetails для зберігання та надання детальної інформації про книгу.
2. Делегування до класу BookDetails: клас LibraryBook тепер містить об'єкт класу BookDetails та делегує йому отримання інформації про книгу.

Виграш:

-Розширення функціональності: клас LibraryBook тепер надає метод get_book_info для отримання детальної інформації про книгу.
-Збереження базового класу: клас LibraryBook залишається незмінним, а додаткова функціональність реалізована через делегування.