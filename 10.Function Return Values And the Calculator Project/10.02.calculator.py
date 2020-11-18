from art import logo
def Calculate(first_number, second_number, operation):
    if operation == "+":
        result = first_number + second_number
    elif operation == "-":
        result = first_number - second_number
    elif operation == "*":
        result = first_number * second_number
    elif operation == "/":
        result = first_number / second_number
    return result


end_calculation = False
first_number = float(input("Please enter first number: "))
while not end_calculation:
    operation = input("Please enter opreation => + - * / \n ")
    second_number = float(input("Please enter second number: "))
    first_number = float(Calculate(first_number, second_number, operation))
    print(first_number)
    more_calculation = input("Do you like to continue N/Y: ")
    if more_calculation == "N":
        end_calculation = True
