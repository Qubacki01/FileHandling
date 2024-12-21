###
#
#
import csv

def read_books_csv(filename):
    books = []
    with open(filename, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)  # Read csv file; map rows to dictionary
        for row in reader:      # Process rows of file
            books.append(row)   # and add to list
    return books


def filter_by_genre(books, genre):  # Filter books by genre; 
    return [book for book in books if book['Genre'] == genre]   # If books genre matches, incl book


def write_books_to_file(books, genre):   # Write books to genre file
    genre_file = f"books_{genre.replace(' ', '_')}.txt"     # Replace with underscores in filename
    with open(genre_file, 'w', encoding='utf-8') as file:   # Open file in write
        for book in books:
            file.write(f"{book['Title']}, {book['Author']}, {book['Year']}\n")
    print(f"{genre} have been written to {genre_file}")


def get_genres(books):   # Get all genres from file
    genres = set(book['Genre'] for book in books)  # Create set of genres; 
    return genres



def main():
    books_csv_file = 'books.csv'            # Read
    books = read_books_csv(books_csv_file)
    

    genres = get_genres(books)  # Get all genres from books
    
    for genre in genres:
        filtered_books = filter_by_genre(books, genre)
        if filtered_books:
            write_books_to_file(filtered_books, genre)
        else:
            print(f"No books found.")

if __name__ == "__main__":
    main()
