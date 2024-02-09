def histogram(list):
    hg_list = []
    for i in list:
        hg_list.append(i*('*'))
    return ' '.join(hg_list[0::])

print(histogram([4, 9, 7]))