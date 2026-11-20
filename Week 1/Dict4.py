# Counting Frequencies

text = "python programming"

frequency = {}

for char in text:
    if char != " ":
        frequency[char] = frequency.get(char,0) + 1

print(frequency)