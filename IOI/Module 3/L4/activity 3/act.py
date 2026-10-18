def roman_to_int(roman):
    values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    index = 0
    while index < len(roman):
        current = values[roman[index]]
        if index + 1 < len(roman):
            following = values[roman[index + 1]]
            if current < following:
                total += following - current
                index += 2
                continue
        total += current
        index += 1
    return total

roman_input = input("Input roman numeral : ")
print("Integer equivalent : ", roman_to_int(roman_input))