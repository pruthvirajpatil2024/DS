text="python is easy and  python is powerfull "
words=text.split()
word_freq={}
for word in words:
    if word in word_freq:
        word_freq[word]+=1
    else:
        word_freq[word]=1
print("word frequency in the string")
for word,freq in word_freq.items():
    print(f"{word}:{freq}")
