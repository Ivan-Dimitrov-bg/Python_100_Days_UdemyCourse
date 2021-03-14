# Unlimited Positional Arguments
# *args - tuple

def add(*args):
    sum = 0
    for n in args:
        sum+=n
    print(sum)


add(1, 4, 5, 6)
add(1, 4)