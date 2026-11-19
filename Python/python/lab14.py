# Lab 14 - Library Book Collection

# Initial book records stored as tuples:
# (title, author, year, category)

books = [
    ("Python Crash Course", "Eric Matthes", "2019", "Programming"),
    ("Automate the Boring Stuff", "Al Sweigart", "2020", "Programming"),
    ("Artificial Intelligence: A Modern Approach",
     "Stuart Russell", "2021", "AI"),
    ("Clean Code", "Robert C. Martin", "2008",
     "Software Engineering")
]

# Set of unique categories in the library
library_categories = {book[3] for book in books}

# Student wishlist
student_wishlist = {
    "AI",
    "Cloud Computing",
    "Robotics",
    "Cybersecurity"
}


def display_books():
    print("\n--- Current Library Catalog (Fixed Records) ---")

    if not books:
        print("No books available.")
        return

    for i, (title, author, year, category) in enumerate(books, start=1):
        print(f'{i}. "{title}" by {author} ({year}) | Genre: {category}')

    print(f"Total Books: {len(books)}")


def add_book():
    print("\n--- Add New Book Record ---")

    title = input("Enter book title: ").strip()
    author = input("Enter author name: ").strip()
    year = input("Enter publication year: ").strip()
    category = input("Enter category/genre: ").strip()

    if not title or not author or not category:
        print("[ERROR] Title, author, and category cannot be empty.")
        return

    if not year.isdigit() or int(year) <= 0:
        print("[ERROR] Enter a valid publication year.")
        return

    # Store the record as an immutable tuple
    book = (title, author, year, category)
    books.append(book)

    # Update the library category set
    library_categories.add(category)

    print(f'[SUCCESS] "{title}" added as an immutable catalog record.')
    print(f'[INFO] Category set updated with: "{category}"')


def display_categories():
    print("\n--- Unique Categories Available in Library (Set) ---")

    if not library_categories:
        print("No categories available.")
    else:
        for category in sorted(library_categories):
            print(f"- {category}")

    print(f"Total Unique Genres: {len(library_categories)}")


def add_to_wishlist():
    print("\n--- Add Category to Student Wishlist ---")

    category = input("Enter requested category/genre: ").strip()

    if not category:
        print("[ERROR] Category cannot be empty.")
    elif category in student_wishlist:
        print(f'[INFO] "{category}" is already in the wishlist.')
    else:
        student_wishlist.add(category)
        print(f'[SUCCESS] "{category}" added to student wishlist.')


def category_gap_analysis():
    print("\n--- Category Gap Analysis ---")

    # Categories requested by students and available in the library
    intersection = student_wishlist & library_categories

    # Categories requested but not available in the library
    difference = student_wishlist - library_categories

    # All categories from both sets
    union = student_wishlist | library_categories

    print("\nStudent Wishlist:")
    print(sorted(student_wishlist))

    print("\nLibrary Categories:")
    print(sorted(library_categories))

    print("\nCategories Available in Both (Intersection):")
    print(sorted(intersection) if intersection else "None")

    print("\nRequested Categories Missing from Library (Difference):")
    print(sorted(difference) if difference else "None")

    print("\nAll Unique Categories (Union):")
    print(sorted(union))

    print(f"\nCategories in Both Sets: {len(intersection)}")
    print(f"Categories Missing from Library: {len(difference)}")
    print(f"Total Unique Categories: {len(union)}")


# Main menu-driven program
while True:
    print("\n" + "=" * 48)
    print("          LIBRARY BOOK & CATEGORY MANAGER")
    print("=" * 48)

    print("\nSelect an operation:")
    print("1. View Cataloged Books")
    print("2. Add New Book Record")
    print("3. View Unique Library Categories")
    print("4. Add Category to Student Wishlist")
    print("5. Run Category Gap Analysis")
    print("6. Exit")

    choice = input("\nEnter your choice (1-6): ").strip()

    if choice == "1":
        display_books()

    elif choice == "2":
        add_book()

    elif choice == "3":
        display_categories()

    elif choice == "4":
        add_to_wishlist()

    elif choice == "5":
        category_gap_analysis()

    elif choice == "6":
        print("\nThank you for using the Library Book & Category Manager!")
        print("Goodbye!")
        break

    else:
        print("[ERROR] Invalid choice. Please enter a number from 1 to 6.")