def decimalToBinary(decimal):
    binary = ""
    while decimal > 0:
        remainder = decimal % 2
        binary = str(remainder) + binary
        decimal = decimal // 2
    return binary if binary else "0"
    
print(decimalToBinary(3434))