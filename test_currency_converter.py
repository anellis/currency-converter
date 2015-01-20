from currency_converter import *

rates =[("USD", "EUR", 0.86),
        ("JPY", "USD", 0.0084),
        ("EUR", "JPY", 136.99)]


def test_get_rates():
    assert get_rate("USD", "EUR") == 0.86
    assert get_rate("EUR", "USD") == round((1/0.86), 2)
    assert get_rate("JPY", "USD") == 0.0084
    assert get_rate("USD", "JPY") == round((1/0.0084), 2)


def test_convert():
    assert convert(rates, 1, "USD", "USD") == 1
    assert convert(rates, 4, "USD", "USD") == 4
    assert convert(rates, 4, "USD", "EUR") == round((0.86 * 4), 2)
    assert convert(rates, 12, "EUR", "JPY") == round((12 * 136.99), 2)
    assert convert(rates, 1000, "JPY", "USD") == round((1000 * 0.0084), 2)
