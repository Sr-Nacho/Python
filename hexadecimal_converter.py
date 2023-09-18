num = input('input data as a number string in base 10 to convert to base 16: ')
data = hex(int(num))
print(data)
data = int(data, 16)
