
two_digit_number = input("Type a two digit number: ")

lastTwoDigits = two_digit_number[-2:]

firstDigit = int(lastTwoDigits[0])

secondDigit = int(lastTwoDigits[1])

result = int(firstDigit) + int(secondDigit)

print(result)

