word_1 = "matching"
word_2 = "mwimming"

list_1 = list(word_1)
list_2 = list(word_2)

# This code breaks the words down into letters.
similarity = 0
commmon_letters = []

for idx, letter in enumerate(list_1):
    if list_1[idx] == list_2[idx]:
        similarity += 1
        commmon_letters.append(letter)
substrings = [[]]
idx = 0

# This code checks for the substrings two words have in common.
substring = ""
while idx < len(commmon_letters) + 1:
    if substring in word_1:
        print(f"Found {substring} in word.")
        if idx < len(commmon_letters): 
            substring += commmon_letters[idx]
        else:
            print("Done")
    else:
        idx -= 1
        substring = f"{commmon_letters[idx]}"
        print(f"Not in word. New substring: {substring}")
    idx += 1
#print(substring)
#print(commmon_letters)