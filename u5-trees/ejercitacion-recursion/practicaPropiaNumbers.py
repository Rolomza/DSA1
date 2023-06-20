# Decimal to Binary

from math import floor
import nntplib


def convertToBinary(n):
    # option 1

    # digit = str(n % 2)
    # return convertToBinary(n//2) + digit if n > 1 else digit

    #option 2
    if n <= 1:
        return str(n)
    else:
        return convertToBinary(n // 2) + convertToBinary(n % 2)

print(convertToBinary(2))