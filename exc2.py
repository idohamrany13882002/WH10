import random

random.random

# exc a
# try - except,  is trying a code that is problematic and catching the error and handling it so the code won't crash.

# exc b
# if you catch the error before it occurs, you can handle it therefore the code will not crash.

# exc c
try:
    x: int = 88 / 0
    print(x)
except:
    print(" you can't divide 88 by 0")

# exc d
age: int = int(input("enter your age: "))
try:
    if age < 18:
        raise AttributeError(f" you are {age} and that is too young")
except:
    print(f"{age} is too young")

# exc e
l1: list[int] = [random.randint(1, 100) for _ in range(4)]
print(f"l1: {l1}")  # to check
while True:
    try:
        num: int = int(input("enter a number: "))
        if num == -999:
            break
        print (l1[num])
    except:
        print (f" {num} is not an index in the list, or not a number")
