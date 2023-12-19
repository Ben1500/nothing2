def add_lists(list1, list2):

    if len(list1) != len(list2):
        if len(list1) > len(list2):
            list1.pop()
        else:
            list2.pop()

    result = []
    for i in range(len(list1)):
        sum_of_elements = list1[i] + list2[i]
        result.append(sum_of_elements)

    return result

liss1 = [1, 2, 3, 4, 3]
liss2 = [1, 2, 3, 4, 1, 2]

print(add_lists(liss1, liss2))