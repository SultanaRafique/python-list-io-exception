def even(begin, num):
    if begin % 2 != 0:
        begin = begin + 1

    even_list = []
    for i in range(num):
        even_list.append(begin)
        begin = begin + 2

    return even_list


begin = int(input("Enter start number: "))
count = int(input("Enter count: "))
res = even(begin, count)
print(res)
