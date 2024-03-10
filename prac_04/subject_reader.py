"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = get_data()
    print(data)
    subject_details = display_subject_details(data)
    print(subject_details)


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    data = []
    for line in input_file:
        print(line)  # See what a line looks like
        print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        print(parts)  # See what the parts look like (notice the integer is a string)
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        data.append(parts)
        print(parts)  # See if that worked
        print("----------")
    input_file.close()
    return data


def display_subject_details(data):
    for subject in data:
        subject_code = subject[0]
        teacher = subject[1]
        num_of_students = subject[2]
        print(f"{subject_code} is taught by {teacher} and has {num_of_students} students")


main()
