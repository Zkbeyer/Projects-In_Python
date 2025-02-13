import Book

def print_start():
    print("Welcome to the book collection manager!");
    print("This program lets you manage your book collection.");
    print("");
          
def get_book_input():
    title = input("Enter the title of the book: ");
    author = input("Enter the author of the book: ");
    year = input("Enter the year of publication: ");
    print("");
    return Book.Book(title,author,year);

def book_options_input():
    print("What would you like to do with this book?")
    print("1. Check out the book");
    print("2. Return the book");
    print("3. View book information");
    print("4. Add another book");
    choice = input("Choice: ");
    print("");
    return choice;

def book_options(book,choice):
    if choice == "1":
        print(book.check_out());
    elif choice == "2":
        print(book.return_book());
    elif choice == "3":
        print(book.get_info());
            
    return;

def display_library(library):
    for book in library:
        print(book.get_info());
        print("");

def main():
    library = [];

    print_start();

    while True:
        book = get_book_input();
        library.append(book);
        book_options(book,book_options_input());
        print("");
        choice = input("Would you like to add another book? (y/n): ");
        if choice != "y":
            break;

    display_library(library);

main();
              
        
        
        
    
