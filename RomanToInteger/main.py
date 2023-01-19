# Title:        Roman to Integer
# Author:       SN
# Purpose:      To convert roman numerals to their integer equivalent.
# Version:      Python 3.9

numeralDict = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
}


def romanToInt(str):
    total = 0
    i = 0

    while (i < len(str)):
        val1 = numeralDict[str[i]]
        if (i + 1 < len(str)):
            val2 = numeralDict[str[i + 1]]
            if (val1 >= val2):
                total = total + val1
                i = i + 1
            else:
                total = total - val1
                i = i + 1
        else:
            total = total + val1
            i = i + 1
    return total


print(romanToInt("VII")) #prints 7
print(romanToInt("XIV")) #prints 14
