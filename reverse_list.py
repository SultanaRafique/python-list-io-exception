def reverse_list(list):
    rvs_lst = []
    for i in range(len(list) -1 ,-1,-1):
        rvs_lst.append(list[i])

    return rvs_lst


list1 = [1, 2, 3, 4]
rev_list = reverse_list(list1)
print(rev_list)
