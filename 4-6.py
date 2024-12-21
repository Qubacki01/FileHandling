###
#
#

def calculate_file_stats(file_name):    # Calculate lines, words, characters in text file
    try:
        num_lines = 0
        num_words = 0
        num_characters = 0

        with open(file_name, 'r', encoding='utf-8') as file:    # Open file and process
            for line in file:
                num_lines += 1      # Add nr of lines
                num_characters += len(line)   # Add nr of char
                num_words += len(line.split())     # Split line to words and count

        print(f"File name: {file_name}")    # Print the results
        print(f"Number of lines: {num_lines}")
        print(f"Number of characters: {num_characters}")
        print(f"Number of words: {num_words}")

    except FileNotFoundError:
        print(f"'{file_name}' does not exist.")


if __name__ == "__main__":  # Main program
    file_name = input("Enter the name of the text file: ")  # Name input

    calculate_file_stats(file_name)
