def reverse(string):
    string = string.split()
    reverse_string = ' '.join(string[::-1])
    return reverse_string

print(reverse('We are ready'))