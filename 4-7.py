###
#
#

import re

def count_vowels(text): # Count number of vowels
    vowels = re.findall(r'[aeiouAEIOU]', text)  # Match all vowels
    return len(vowels)




# Main program
if __name__ == "__main__":
    text = input("Enter text: ")

    vowel_count = count_vowels(text)
    print(f"Number of vowels: {vowel_count}")
