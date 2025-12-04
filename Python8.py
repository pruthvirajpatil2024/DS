# Program to count the occurrences of each word in a sentence

sentence = "the cat and the dog and the cat"
words = sentence.split()

word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print("Sentence:", sentence)
print("Word occurrences:")

for word, count in word_count.items():
    print(word, ":", count)

print("=== Code Execution Successful ===")
