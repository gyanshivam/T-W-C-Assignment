number = int(input("Enter your number: "))

if number < 0:
    print(f"{number} is not a palindrome")
else:
    original = number
    digits = []
    temp = number

    while temp > 0:
        digits.append(temp % 10)
        temp //= 10

    is_palindrome = True
    left = 0
    right = len(digits) - 1

    while left < right:
        if digits[left] != digits[right]:
            is_palindrome = False
            break
        left += 1
        right -= 1

    if is_palindrome:
        print(f"{original} is a palindrome")
    else:
        print(f"{original} is not a palindrome")