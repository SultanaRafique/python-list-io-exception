def try_except():
    try:
        x = 1 / 0
    except:
        print("division by zero exception")


def try_except_msg():
    try:
        x = 1 / 0
    except ZeroDivisionError as zde:
        print(zde)
        print("division by zero exception")


try_except()
try_except_msg()
