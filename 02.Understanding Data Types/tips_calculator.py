#If the bill was $150.00, split between 5 people, with 12% tip.
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

amount = input("enter your bill: ")
procent = input("enter the tip you want to leave: 10, 12 or 15 : ")
numberOfPeople = input("how many people will split the bill: ")

result = (float(amount)/float(numberOfPeople))*((float(procent)/100) + 1)

print("Everyone need to pay: {:.2f}".format(result))

#result = round(result, 2)
#print(f"Each person should pay: ${result}")