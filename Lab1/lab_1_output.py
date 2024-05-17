def validate_name(name):
    """
    Перевіряє валідність імені користувача.
    """
    if len(name) < 3:
        raise ValueError("Name must be at least 3 characters long.")


def validate_age(age):
    """
    Перевіряє валідність віку користувача.
    """
    if age < 18:
        raise ValueError("User must be at least 18 years old.")


def validate_email(email):
    """
    Перевіряє валідність адреси електронної пошти.
    """
    if "@" not in email:
        raise ValueError("Invalid email address.")


def format_address(address):
    """
    Форматує адресу користувача.
    """
    return address.upper()


def validate_access_level(access_level):
    """
    Перевіряє валідність рівня доступу користувача.
    """
    if access_level not in ["admin", "user", "guest"]:
        raise ValueError("Invalid access level.")


def process_user_data(name, age, gender, email, address, phone_number, access_level):
    """
    Обробляє дані користувача та виконує різні дії.
    """
    validate_name(name)
    validate_age(age)
    validate_email(email)
    formatted_address = format_address(address)
    validate_access_level(access_level)

    # Виводить інформацію про користувача
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Gender: {gender}")
    print(f"Email: {email}")
    print(f"Address: {formatted_address}")
    print(f"Phone number: {phone_number}")
    print(f"Access level: {access_level}")

    # Додаткові дії (наприклад, збереження даних до бази даних)
    # ...