def decimal_to_base_n(number, base):
    if base < 2 or base > 36:
        return "Base out of range (2-36)"
    
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""
    
    while number > 0:
        digit = number % base
        result = digits[digit] + result
        number //= base
    
    return result

# Input from the user
num = int(input('Input data as a number in base 10: '))
base_x = int(input('Enter the base you want to convert to: '))

# Call the function to convert
result = decimal_to_base_n(num, base_x)

print(f"The number {num} in base 10 is equivalent to {result} in base {base_x}.")
