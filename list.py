import random
my_list = ["hello", "55-555-5555", 88]
print(type(my_list))
print(my_list)
print(my_list[2])
print(my_list[-3])
print(my_list[:])

my_list = ["a", "b", "c", "d", "e", "f", "a", "a"]
print(my_list[1:3])
print(my_list[:3])
my_list[3] = "k"
print(my_list[:])

del my_list[3]
print(my_list[:])
print(len(my_list))


for i in range(len(my_list)):
    print(my_list[i])
    print(f"index [{i}] : {my_list[i]}")

print(my_list.count("a"))
print(my_list.count("b"))
print([1, 2, 3] + [3, 4, 7])
second_list = list((1, 2, 3))

values = [0, 0, 0, 0, 0,]
for i in range(1, 5):
    values[i] = i + values[i - 1]

values[0] = values[1] + values[4]

print(values)

values = []
for i in range(5):
    values.append(i)

print(values)

"""values = []
for i in random.randint(1, 100):
    values.append(i)

print(values)


for i in range(len(my_list)):
    print(values[i], end="|")
    

list_one = [1, 2, 3, 4, 5]
list_two = list_one.copy()
deep_list_two = list_one.deepcopy()
print(list_two)
print(list_two)
print(deep_list_two)
"""