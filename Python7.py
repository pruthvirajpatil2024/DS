def remove_nth_occurrence(lst, word, n):
    count = 0

    for i in range(len(lst)):
        if lst[i] == word:
            count += 1

            if count == n:
                del lst[i]
                return lst

    return lst  # if occurrence not found


# Driver Code
words = ["apple", "banana", "apple", "orange", "apple"]
print("Original List=", words)

word = "banana"
n = 1

result = remove_nth_occurrence(words, word, n)
print(f"after removing (n) th occurrence OF '{word}':", result)

