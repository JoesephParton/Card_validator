

def get_input():
    valid = False
    exiting = False

    while valid is False and exiting is False:
        card_num = input("Your 11 digits on your card: ")
        if card_num == "x":
            print("exiting")
            exiting = True 

        elif len(card_num) != 11 or card_num.isdigit is False:
            print("Incorrect input try again")
            
        else:
            valid = True
    return card_num

def varifier(card_num):
    total = 0
    for index, number in enumerate(card_num):
        number = int(number)
        if (index + 1) % 2 == 0:
            number *= 2
            if len(str(number)) == 2:
                number = int(str(number)[0]) + int(str(number)[1])
        total += number

    if total % 10 == 0:
        validitate = True

    else:
        validitate = False

    return validitate


card_num = get_input()

if card_num == "x":
    pass

else:
    print(varifier(card_num))
