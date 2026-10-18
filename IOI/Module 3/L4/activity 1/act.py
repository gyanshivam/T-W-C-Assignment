number = int(input("Input your number: "))

if number < 0:
    print(number, "is not an Armstrong number")
else:
    digit_count = len(str(number))
    total = 0

    for ch in str(number):
        total += int(ch) ** digit_count

    if total == number:
        print(number, "is an Armstrong number")
    else:
        print(number, "is not an Armstrong number")