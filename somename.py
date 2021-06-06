intro = input("Enter your introduction: ")
wordCount = 1
characterCount = 0
for i in intro:
    characterCount+=1
    if i==" ":
        wordCount+=1
print(characterCount)
print(wordCount)