# Converion of Int to Binary


def convertToBinary(num: int) -> str:
    result = ""  # insted of string you can return it in any form like list or tuple
    while num > 0:
        if num % 2 == 1:
            result += "1"
        else:
            result += "0"
        num = num // 2
    result = result[::-1]
    return result


num = 13
convert2binary = convertToBinary(num)
print(f"Conversion of {num} to binary is: {convert2binary}")

# TC -> O(log2N)
# SC -> O(log2N)