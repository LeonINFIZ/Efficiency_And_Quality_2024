def calculate_price(product_prices, discount):
    """
    Обчислює загальну вартість продуктів з урахуванням знижки.
    """
    total_price = 0
    for price in product_prices:
        if discount:
            total_price += price * 0.9  # 10% discount
        else:
            total_price += price
    return total_price


def calculate_total_price_with_tax(product_prices, discount, tax_rate):
    """
    Обчислює загальну вартість продуктів з урахуванням знижки та податку.
    """
    return calculate_price(product_prices, discount) * (1 + tax_rate)