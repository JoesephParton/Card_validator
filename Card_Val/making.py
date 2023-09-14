import random


def get_card_num():
    card_num = ""
    for _ in range(0, 10):
        digit = random.randint(0, 9)
        card_num += str(digit)
    return card_num


def luhr_calc(card_num):
    total = 0

    for index, number in enumerate(card_num):
        number = int(number)
        if (index + 1) % 2 == 0:
            number *= 2
            if len(str(number)) == 2:
                number = int(str(number)[0]) + int(str(number)[1])
        total += number
    return total

def last_num(card_num, total):
    num_ten = total % 10

    if num_ten == 0:
        card_num += '0'

    else:
        card_num += str(10 - num_ten)

    return card_num

card_num = get_card_num()
total = luhr_calc(card_num)
print(last_num(card_num, total))

