x = 10
try:
    if x > 5:
        raise ValueError("x should not greater than 5")
except Exception as ve:
    print("caught error")
