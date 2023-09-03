# Write a function takes a two-word string and returns True if both words begin with same letter:
# animal_crackers('Levelheaded Llama') --> True
# animal_crackers('Crazy Kangaroo') --> False


# In this solution, lower case before the split, by tacking lower() function before split() function
# It would work the same way if you used upper() because it will just uppercase any lowered case letter


def animal_crackers(text):
    wordlist = text.lower().split()
    print(wordlist)

    return wordlist[0][0] == wordlist[1][0]

print(animal_crackers('Crazy cat'))
