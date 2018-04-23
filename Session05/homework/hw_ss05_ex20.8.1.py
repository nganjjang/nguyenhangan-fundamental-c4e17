my_string = ("ThiS is String with Upper and lower case Letters").lower()
letter_count = {}
for letter in my_string:
    if letter != " ":
        letter_count[letter] = letter_count.get(letter, 0) + 1
letter_count_items = list(letter_count.items())
letter_count_items.sort()
for key, value in letter_count_items:
    print(key, value)
