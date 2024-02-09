def permute(string, it = 0):
    if it == len(string) - 1:
        print(''.join(string))
    else:
        for i in range(it, len(string)):
            string[it], string[i] = string[i], string[it]
            permute(string, it + 1)
            string[it], string[i] = string[i], string[it]

string = list(input())
permute(string)