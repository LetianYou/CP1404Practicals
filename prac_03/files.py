# 1
name = input("Please enter the name you wish to record: ")

open_file = open("name.txt", "w")

print(f"Recorded name: {name}", file=open_file)

open_file.close()


# 2
open_file = open("name.txt", "r")

name = open_file.readlines()

print(f"your recorded name is: {name}")

open_file.close()


# 3
open_file = open("numbers.txt", "r")

line_1 = open_file.readline().strip()
line_2 = open_file.readline().strip()

result = int(line_1) + int(line_2)

print(f"The result is: {result}")

open_file.close()


# 4
open_file = open("numbers.txt", "r")

total = 0

for line in open_file:
    number = int(line.strip())
    total += number

print(f"{total}")

open_file.close()
