def count_common_unique(list1, list2):
    # list1: list of strings
    # list2: list of strings
    # return an integer
    dict_1 = {}
    dict_2 = {}
    ans = 0

    for i in list1:
        if i in dict_1:
            dict_1[i] += 1
        else:
            dict_1[i] = 1

    for i in list2:
        if i in dict_2:
            dict_2[i] += 1
        else:
            dict_2[i] = 1 

    for key, value in dict_1.items():
        if key in dict_2 and dict_2[key] == 1 and value == 1:
            ans += 1

    return ans