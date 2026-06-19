# ==========================
# SET OPERATIONS
# ==========================

# Given list of numbers
numbers = [1, 2, 3, 4, 4, 5, 6, 6, 7]

# Create a set of unique numbers
num_set = set(numbers)

print("Original Set:", num_set)

# Add new elements
num_set.add(8)
num_set.add(9)
print("After Adding Elements:", num_set)

# Remove existing element
num_set.remove(3)
print("After Removing Element 3:", num_set)

# Another set for operations
another_set = {5, 6, 7, 8, 10}

# Union
print("Union:", num_set.union(another_set))

# Intersection
print("Intersection:", num_set.intersection(another_set))

# Difference
print("Difference:", num_set.difference(another_set))


# ==========================
# LIBRARY MANAGEMENT SYSTEM
# ==========================

library = {}


def add_book(title, author, year, genre):
    """Add a new book to the library."""
    library[title] = {
        "Author": author,
        "Publication Year": year,
        "Genre": genre
    }
    print(f"Book '{title}' added successfully.")


def remove_book(title):
    """Remove a book from the library."""
    if title in library:
        del library[title]
        print(f"Book '{title}' removed successfully.")
    else:
        print(f"Book '{title}' not found.")


def search_by_title(title):
    """Search for a book by title."""
    if title in library:
        print(f"\nBook Found: {title}")
        print(library[title])
    else:
        print("Book not found.")


def search_by_author(author):
    """Search books by author."""
    print(f"\nBooks by {author}:")
    found = False
    for title, details in library.items():
        if details["Author"].lower() == author.lower():
            print(f"- {title}")
            found = True

    if not found:
        print("No books found.")


def search_by_genre(genre):
    """Search books by genre."""
    print(f"\nBooks in Genre '{genre}':")
    found = False
    for title, details in library.items():
        if details["Genre"].lower() == genre.lower():
            print(f"- {title}")
            found = True

    if not found:
        print("No books found.")


def display_books(sort_by="title"):
    """Display all books sorted by title or author."""
    print("\nLibrary Books:")

    if sort_by.lower() == "author":
        sorted_books = sorted(
            library.items(),
            key=lambda item: item[1]["Author"]
        )
    else:
        sorted_books = sorted(library.items())

    for title, details in sorted_books:
        print(
            f"Title: {title}, "
            f"Author: {details['Author']}, "
            f"Year: {details['Publication Year']}, "
            f"Genre: {details['Genre']}"
        )


# ==========================
# TESTING WITH SAMPLE DATA
# ==========================

# Add books
add_book("The Great Gatsby", "F. Scott Fitzgerald", 1925, "Fiction")
add_book("1984", "George Orwell", 1949, "Dystopian")
add_book("To Kill a Mockingbird", "Harper Lee", 1960, "Fiction")
add_book("The Hobbit", "J.R.R. Tolkien", 1937, "Fantasy")

# Display all books sorted by title
display_books("title")

# Display all books sorted by author
display_books("author")

# Search operations
search_by_title("1984")
search_by_author("George Orwell")
search_by_genre("Fiction")

# Remove a book
remove_book("The Hobbit")

# Display updated library
display_books()