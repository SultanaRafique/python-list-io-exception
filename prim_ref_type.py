def pri_ref(number, list_number):
    number = 100
    list_number[0] = 111


number = 0
list_number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("before change number", number)
print("before change list", list_number)

pri_ref(number, list_number)

print("after change number", number)
print("after change list", list_number)
