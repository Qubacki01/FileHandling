###
#
#

def read_from_file(name):
    with open(name) as file:
        content = file.read()
    return content

file_content = read_from_file('pets.txt')

print(file_content) # Print text from file

words = file_content.split()    # Split content into words and count words
word_count = len(words)


print('Number of words:', word_count)
