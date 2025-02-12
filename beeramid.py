def beeramid(bonus, price):

    if bonus < price:
        return -1
    div = bonus / price

    i = 0 
    j = 0
    sum = 0
    while sum <= div:
        j =  i ** 2
        sum +=j

        if sum > div:
            return i - 1

        i  += 1


def beeramid_2(bonus,price):
    if bonus < price:
        return 0

    levels = 0
    while bonus >= (levels + 1) ** 2 * price:
        levels += 1
        bonus -= levels ** 2 * price

    return levels

