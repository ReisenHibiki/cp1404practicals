"""
Word Occurrences
Estimate: 15 minutes
Actual:   20 minutes
"""

user_input = input("Enter a string: ")
word_to_count = {}
width = 0
# for word in user_input.split():
#     if word in word_to_count:
#         word_to_count[word] += 1
#     else:
#         word_to_count[word] = 1
for word in user_input.split():
    word_to_count[word] = word_to_count.get(word, 0) + 1
    if width < len(word):
        width = len(word)

for i in sorted(word_to_count):
    print(f"{i:{width}} : {word_to_count[i]}")

