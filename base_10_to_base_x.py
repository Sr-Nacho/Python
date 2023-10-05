"""
This is basically copied completely from chatgpt for later use
"""

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

## Reverse of the above function ##
def base_n_to_decimal(number, base):
    if base < 2 or base > 36:
        return "Base out of range (2-36)"
    
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = 0
    
    # Reverse the input number as we process it from right to left
    number = number[::-1]
    
    for i in range(len(number)):
        digit = digits.index(number[i])
        result += digit * (base ** i)
    
    return result

# Input from the user
num = int(input('Input data as a number in base 10: '))
base_x = int(input('Enter the base you want to convert to: '))

# Call the function to convert
result = decimal_to_base_n(num, base_x)

print(f"The number {num} in base 10 is equivalent to {result} in base {base_x}.")

# Reverse of the above
num = input('Input data as a number in the specified base: ')
base_x = int(input('Enter the base of the input number: '))

# Call the function to convert
result = base_n_to_decimal(num, base_x)

print(f"The number {num} in base {base_x} is equivalent to {result} in base 10.")
