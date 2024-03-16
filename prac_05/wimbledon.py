import csv


def main():
    filename = "wimbledon.csv"
    file_data = read_csv(filename)
    champions = count_champions(file_data)
    display_champions(champions)
    countries = get_countries(champions)
    display_countries(countries)


def read_csv(filename):
    file_data = []
    in_file = open(filename, "r", encoding="utf-8-sig")
    reader = csv.reader(in_file)
    for row in reader:
        file_data.append(row)
    in_file.close()
    return file_data


def count_champions(file_data):
    champions = {}
    for row in file_data:
        player = row[0]
        if player in champions:
            champions[player] += 1
        else:
            champions[player] = 1
    return champions


def display_champions(champions):
    for champion, num_win in champions.items():
        print(f"Wimbledon Champions:\n{champion} {num_win}")


def get_countries(champions):
    countries = set()
    for champion in champions.keys():
        countries.add(champion.split()[-1])
    return sorted(countries)


def display_countries(countries):
    print(f"\nThese {len(countries)} countries have won Wimbledon:")
    print(", ".join(countries))


main()
