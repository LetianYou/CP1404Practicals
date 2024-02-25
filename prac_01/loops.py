for i in range(1, 21, 2):
    print(i, end=' ')
print()

# a
for i in range(0, 101, 10):
    print(i, end=' ')
print()

# b
for i in range(20, 0, -1):
    print(i, end=' ')
print()

# c
star_numbers = int(input("How many stars do you want to print? "))
print("*" * star_numbers)

# d
for i in range(1, star_numbers + 1):
    print("*" * i)
