binary_number = '1001110110110101'
hexadecimal_number = ""

# Group the binary number into groups of 4 digits
while len(binary_number) % 4 != 0:
    binary_number = '0' + binary_number

# Convert each group of 4 digits to a hexadecimal digit
for i in range(0, len(binary_number), 4):
    group = binary_number[i:i+4]
    decimal_value = 0
    power = 3

    # Convert the binary group to decimal
    for digit in group:
        decimal_value += int(digit) * (2 ** power)
        power -= 1

    # Convert the decimal value to hexadecimal
    if decimal_value < 10:
        hexadecimal_number += str(decimal_value)
    else:
        hexadecimal_number += chr(decimal_value + 55)

print("Hexadecimal value:", hexadecimal_number)