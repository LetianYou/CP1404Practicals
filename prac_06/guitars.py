from guitar import Guitar


def main():
    """ Main function to interact with the user and display guitar details."""
    print("My guitars!")
    guitars = []
    name = input("Name: ")
    while name:
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitars.append(Guitar(name, year, cost))
        print(f"{name} ({year}) : ${cost:.2f} added.\n")
        name = input("Name (leave blank to finish): ")

    print("\nThese are my guitars:")
    for i, guitar in enumerate(guitars, 1):
        vintage_string = " (vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar.name:20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")


main()
