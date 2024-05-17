def process_user_data(name, age, gender, email, address, phone_number, access_level):
    """
    Обробляє дані користувача та виконує різні дії.
    """

    # Перевірка валідності імені
    if len(name) < 3:
        raise ValueError("Name must be at least 3 characters long.")

    # Перевірка валідності віку
    if age < 18:
        raise ValueError("User must be at least 18 years old.")

    # Перевірка валідності електронної пошти
    if "@" not in email:
        raise ValueError("Invalid email address.")

    # Форматування адреси
    formatted_address = address.upper()

    # Перевірка валідності рівня доступу
    if access_level not in ["admin", "user", "guest"]:
        raise ValueError("Invalid access level.")

    # Вивід інформації про користувача
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Gender: {gender}")
    print(f"Email: {email}")
    print(f"Address: {formatted_address}")
    print(f"Phone number: {phone_number}")
    print(f"Access level: {access_level}")

    # Додаткові дії (наприклад, збереження даних до бази даних)
    # ...