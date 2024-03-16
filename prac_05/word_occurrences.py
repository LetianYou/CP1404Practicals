KEY_WORDS = {"a", "collection", "fun", "is", "it", "nice", "of", "thing", "this", "words"}

user_input = input("Please enter the string: ").split()

count_string = {}

for word in user_input:
    if word in KEY_WORDS:
        count_string[word] = count_string.get(word, 0) + 1

for word, count in sorted(count_string.items()):
    print(f"{word:{max(len(word) for word in count_string)}} : {count}")
