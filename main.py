# Import Letter to Morse Code Dictionary
from morse_code import MORSE_CODE_DICT

# Ask User for word to translate
word = input('Please enter the word you would like to convert into morse code: ').upper()
# Create empty list to hold converted word
morse_list = []

# Loop through each letter in the word
for letter in list(word):

    # Try to find letter in Dictionary and if found, add to list
    try:
        morse_letter = MORSE_CODE_DICT[letter]
        morse_list.append(morse_letter)

    # If an invalid character is added (i.e. spaces, special chars), just skip it
    except KeyError:
        pass

# Cobmine list back into String with spaces in between morse letters
morse_word = " ".join(morse_list)

# Print results to user
print(f'Your converted word is {morse_word}')

