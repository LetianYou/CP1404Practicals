authorised_user = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
numbers = []

username = input("Please enter your username: ")
if username in authorised_user:
    print("Access granted")
else:
    print("Access denied")

for i in range(5):
    num = int(input("Number: "))
    numbers.append(num)

print(f"The first number is {numbers[0]}")
print(f"The last number is {numbers[-1]}")
print(f"The smallest number is {min(numbers)}")
print(f"The largest number is {max(numbers)}")
print(f"The average of the number is {sum(numbers) / len(numbers)}")
