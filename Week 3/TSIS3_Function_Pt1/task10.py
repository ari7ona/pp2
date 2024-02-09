def unique(list):
    unique_list = []
    for i in list:
        if i not in unique_list:
            unique_list.append(i)
    return unique_list

print(unique([1, 1, 2, 3, 4, 4, 5]))