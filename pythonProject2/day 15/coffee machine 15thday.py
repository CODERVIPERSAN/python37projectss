# TODO:1.TO IMPORT THE RESOURCES FILE

from data import MENU, resources

# setting up the pycharm environment
# coffee machine
print("hello world ")


##########################################################################
# code for the coffee machine

# TODO:2.TO CREATE THE REPORT
# TODO:5.COLLECT ALL THE INFORMATION ABOUT THE COFFEE

def computer_list():
    cpy = {}
    for i, j in resources.items():
        cpy[i] =j
    return cpy


def report(resource_dict):
    for item, quantity in resource_dict.items():
        print(item, quantity)


# TODO:6.INPUTTING ALL THE MONEY TYPE DO YOU HAVE
# TODO:7.SUM(INPUT) IS IT ENOUGH OF THE COFFEE YOU NEED


def coin(co):
    """compare the inputed cost and the coffee
     cost and difference in them is positive
     balance then return balance  if the differencence negative
     otherwise it will return false """
    money_list = []
    for list_of_money in range(6):
        if list_of_money == 0:
            x = int(input("how much 5 ruppee"))
            total = x * 5
            money_list.append(total)

        if list_of_money == 1:
            x = int(input("how much 10 ruppee"))
            total = x * 10
            money_list += [total]
        if list_of_money == 2:
            x = int(input("how much 50 ruppees "))
            total = x * 50
            money_list.append(total)
        if list_of_money == 3:
            x = int(input("how much 20 ruppee "))
            total = x * 20
            money_list.append(total)
        if list_of_money == 4:
            x = int(input("how much 100 ruppe do you have"))
            total = x * 100
            money_list.append(total)
        if list_of_money == 5:
            x = int(input("how much 200 ruppee do you have "))
            total = x * 200
            money_list.append(total)

    balance = sum(money_list) - co
    if balance >= 0:
        print("here is  your balance", balance)
        return co
    elif balance < 0:
        print("not sufficient money try again")
        return False


def tank(user, res):
    """gets the user_input and
    return the remaining
    resources in dictionary
    if it not sufficient for coffee return false"""
    sub_tank = MENU[user]['ingredients']
    key = res.keys()
    value = res.values()

    main_tank = dict(zip(key, value))
    for i in main_tank:
        main_tank[i] = main_tank[i] - sub_tank[i]
        if main_tank[i] <= 100:
            print(f"warning your {i} is low")
        if main_tank[i] < 0:
            print(f"not sufficient {i}", "money refunded")
            return False
    return main_tank


def refill(diction):
    for i in resources:
        diction[i] = resources[i]
    return diction


def cost(user):
    """return the cost of the user input"""
    return MENU[user]['cost']


# TODO:9. RESOURCES ARE SUBTRACTED FROM THE INITIAL VALUE

# TODO:3.GAME LOOP USING WHILE FOR REPEATING (FLAGS)
endgame = False
reports = False
while not endgame:
    n = 0
    start = computer_list()
    starts = 1
    s = []
    while start and starts:
        # TODO:4.INPUT THE WHICH COFFEE  DO YOU NEED ?
        user_input = input("what do you need (espresso ,cappuccino, latte)")

        if user_input == "report":
            report(start)
            print("amount of money in machine", sum(s))
            continue
        if user_input == "refill":
            t = refill(start)
            s = []
            print(t)
            continue
        if user_input == "off":
            endgame = True
            break
        else:
            if n == 0:
                start = tank(user_input, resources)
            else:
                start = tank(user_input, start)
            n += 1
        # TODO:5.COIN OPERATOR
            if start:
                cost_of_coffee = cost(user_input)
                starts = coin(cost_of_coffee)
                s += [cost_of_coffee]

    # TODO:8.IF TRUE SUBSTRATE THE MONEY FROM THE COST AND RETURN THE BALANCE
    # TODO:9.IF 7 IS TRUE THE SENT THE MESSAGE ENJOY THE COFFEE

    # TODO:10. RESOURCES IS SUFFICIENT OR NOT

    # TODO:11.REFILL FUNCTION (ENTER REFILL TO REFILL AND START THE PROCESS AGAIN)


