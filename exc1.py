import random

# exc a
l1: list[int] = [x for x in range(95, 106)]
print(f"l1: {l1}")  # to check

# exc b
l2: list[int] = [x for x in range(10, 21, 2)]
print(f"l2: {l2}")  # to check

# exc c
l3: list[bool] = [random.choice([True, False]) for _ in range(5)]
print(f"l3: {l3}")

# exc d
l4: list[int] = [random.randint(1, 101) for _ in range(10)]
print(f"l4: {l4}")  # to check

# exc e
l5: list[int] = [x for x in l4 if x > 50]
print(f"l5: {l5}")  # to check

# exc f
# you can make it in one row, change the range to 50 to 100

# exc g
sen: str = input("enter a string: ")
l7: list[str] = [x for x in sen if x not in ["t", " "]]
print(f"l7: {l7}")

# exc h
l8: list[int] = [random.randint(10, 100) for _ in range(10)]
print(f"l8: {l8}")
l9: list[int] = [x % 10 for x in l8]
print(f"l9: {l9}")
