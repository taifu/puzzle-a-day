def date_to_array(day, month):
    """ Day: 1-31 Month: 1-12 -> (m, d) """
    assert 1 <= month <= 12
    assert 1 <= day <= 31
    return (month - 1, 11 + day)


def solve(day, month):
    print(day, month)
