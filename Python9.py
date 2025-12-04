#List of words
words = ['apple','banana','avocado','cherry','blueberry','apricot']

#Empty dictionary
char_dict = {}

#Loop throught
for word in words:
    key= word[0]
    if key in char_dict:
        char_dict[key].append(word)
    else:
        char_dict[key]= [word]
print("Dictionary with first character as key")
print(char_dict)
