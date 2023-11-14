sentence = input("Enter a sentence: ")
i = 1
counter = 1

while i < len(sentence):
    sym = sentence[0]
    if sym == " ":
        counter += 1
    i += 1
counter += 1
print(counter)
