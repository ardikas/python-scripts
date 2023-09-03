# Write a function takes a two-word string and returns True if both words begin with same letter:
# animal_crackers('Levelheaded Llama') --> True
# animal_crackers('Crazy Kangaroo') --> False


def animal_crackers(text):

    split_string = text.split()

    if split_string[0][0] == split_string[1][0]:
        return True
    else:
        return False

    pass

# Check
print(animal_crackers('Levelheaded Llama'))
print(animal_crackers('Crazy Kangaroo'))
