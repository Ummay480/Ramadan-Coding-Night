import json


class BookCollection:
    """ A class to manage a collection of books, allowing usera to store and organize their books"""

    def __init__(self):
        """Initialize a new book collection with an empty list and setup file storage."""

        self.book_list = []
        self.storage_file = "books_data.json"
        self.read_from_file()

    def read_from_file(self):
        """load savedbooks from a JSON file into memory.
        if the file does not exist or is corrupted, start with an empty collection."""
        try:
            with open(self.storage_file, "r") as file:
                self.book_list = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            self.book_list = []

    def save_to_file(self):
        """save the current book collection to a JSON file for permanent storage."""
        with open(self.storage_file, "w") as file:
            json.dump(self.book_list, file, indent=4)

    def create_new_book(self):
        """ Add a new book to the collection by gathering information from the user."""
        book_title = input("Enter the title of the book: ")
        book_author = input("Enter the author of the book: ")
        publication_year = input("Enter publication year: ")
        book_genre = input("Enter the genre of the book: ")
        is_book_read = (
            input("Have you read this book? (yes/no): ").strip()lower() == "yes"
        )
        new_book = {
            "title": book_title,
            "author": book_author,  
            "year": publication_year,
            "genre": book_genre,
            "read": is_book_read,
        }
                        
        self.book_list.append(new_book)
        self.save_to_file()
        print("Book added successfully! \n")

    def delete_book(self):
        """Delete a book from the collection using its title."""
        book_title = input("Enter the title of the book to delete: ")
        for book in self.book_list:
            if book["title"].lower() == book_title.lower():
                self.book_list.remove(book)
                self.save_to_file()
                print(f"Book '{book_title}' deleted successfully. \n")
                return
        print(f"Book '{book_title}' not found in the collection. \n")

    def load_books(self):

































































        # Run the main aplplication loop with a user friendly menu interface
        def start_application(self):
            """ Run the main application loop with a user friendly menu interface."""
            while True:
                print("📚welcome to the Book Collection Manager! 📕")
                print("1. Add a new book")
                print("2. Delete a book")
                print("3. View all books")
                print("4. Update book details")
                print("5. Search for a book")
                print("6. View reading progress")
                print("7. Exit")
                user_choice = input("Enter your choice (1-7): ")

                if user_choice == "1":
                    self.create_new_book()
                elif user_choice == "2":
                    self.delete_book()
                elif user_choice == "3":
                    self.view_all_books()
                elif user_choice == "4":
                    self.update_book_details()
                elif user_choice == "5":
                    self.search_books()
                elif user_choice == "6":
                    self.view_reading_progress()
                elif user_choice == "7":
                    print("Thank you for using the Book Collection Manager. Goodbye!")

                    break
                else:
                    print("Invalid choice. Please try again.\n")
                        class BookCollection()

    if __name__ == "__main__":
       book_manager = BookCollection()
       book_manager.start_application()

                
        










