string_1 = input("Enter first string: ")
string_2 = input("Enter second string: ")

string_1_character_count = {}
string_2_character_count = {}

for character in string_1:
    if character in string_1_character_count:
        string_1_character_count[character] += 1
    else:
        string_1_character_count[character] = 1

for character in string_2:
    if character in string_2_character_count:
        string_2_character_count[character] += 1
    else:
        string_2_character_count[character] = 1

if string_1_character_count == string_2_character_count:
    print("Anagrams")
else:
    print("Not anagrams")


