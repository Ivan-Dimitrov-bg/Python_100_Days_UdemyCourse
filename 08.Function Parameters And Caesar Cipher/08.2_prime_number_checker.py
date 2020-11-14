# Write your code below this line 👇
import Math


def prime_checker(number):
    it_is_Prime = True
    for i in range(2, int(Math.Sqrt(number))):
        if number % i == 0:
            it_is_Prime = False

    if it_is_Prime:
        print(f"It's a prime number.")
    else:
        print(f"It's not a prime number.")


# Write your code above this line 👆

# It's a prime number.
# It's not a prime number.

# Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)