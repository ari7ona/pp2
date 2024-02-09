def convert(temperature: int):
    temperature = (temperature - 32) * 5/9
    return temperature

print(convert(int(input())))