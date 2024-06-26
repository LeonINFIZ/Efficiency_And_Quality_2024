Аналіз та рефакторинг "довгого методу"

Проблема: Метод process_user_data в файлі lab_1_input.py містить занадто багато коду та відповідає за різні задачі: валідацію даних, форматування та виведення. Це ускладнює розуміння коду та його подальшу підтримку.

Рішення: Для покращення коду було застосовано рефакторинг за допомогою відокремлення методу. Кожен етап обробки даних було виділено в окрему функцію:
-validate_name: перевіряє валідність імені.
-validate_age: перевіряє валідність віку.
-validate_email: перевіряє валідність електронної пошти.
-format_address: форматує адресу.
-validate_access_level: перевіряє валідність рівня доступу.

Тепер метод process_user_data викликає ці функції для виконання відповідних дій.

Виграш:

-Підвищення читабельності: Код став більш структурованим та легшим для розуміння.
-Спрощення підтримки: Модифікація окремих етапів обробки даних стала простішою, оскільки кожна функція відповідає за конкретну задачу.
-Потенціал для повторного використання: Виділені функції можна використовувати в інших частинах програми.