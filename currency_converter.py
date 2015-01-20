rates = [("USD", "EUR", 0.86),
         ("JPY", "USD", 0.0084),
         ("EUR", "JPY", 136.99)]


def get_rate(start, to):
    for itm in rates:
        if start == itm[0] and to == itm[1]:
            rate = itm[2]
            return rate
        elif start == itm[1] and to == itm[0]:
            rate = round(1/(itm[2]), 2)
            return rate


def convert(rates, value, start, to):
    if start == to:
        return value
    else:
        rate = get_rate(start, to)
        return value * rate
