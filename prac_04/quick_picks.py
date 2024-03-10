import random

MIN_RANDOM_NUMBER = 1
MAX_RANDOM_NUMBER = 45
RANDOM_NUMBER_EACH_LINE = 6

num_line = int(input("How many quick picks? "))

for i in range(num_line):
    numbers = []
    while len(numbers) < RANDOM_NUMBER_EACH_LINE:
        num = random.randint(MIN_RANDOM_NUMBER, MAX_RANDOM_NUMBER)
        if num not in numbers:
            numbers.append(num)
    numbers.sort()
    print(" ".join(f"{num:2}" for num in numbers))
