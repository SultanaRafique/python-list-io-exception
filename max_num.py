def max_val(values):
    max_num = values[0]
    for i in range(len(values)):
        if values[i] > max_num:
            max_num = values[i]

    return max_num


values = [2, 3, 56, 7, 8, 9, 66]
max_val = max_val(values)
print(max_val)
