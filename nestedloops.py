word = input("Enter a word: ")

char_count = {}
repeated = 0

# Count frequency of each character
for ch in word:
    if ch in char_count:
        char_count[ch] += 1
    else:
        char_count[ch] = 1

# Count how many characters appear more than once
for ch in char_count:
    if char_count[ch] > 1:
        repeated += 1

print("Number of repeated characters:", repeated)
