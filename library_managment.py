import mysql.connector
def connect_to_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",  
        password="",  
        database="library_management"
    )
def create_tables():
    db = connect_to_db()
    cursor = db.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS members (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(100), email VARCHAR(100))")
    cursor.execute("CREATE TABLE IF NOT EXISTS books (id INT AUTO_INCREMENT PRIMARY KEY, title VARCHAR(200), author VARCHAR(100))")
    db.close()
    print("Tables created.")
def add_member(name, email):
    db = connect_to_db()
    cursor = db.cursor()
    cursor.execute("INSERT INTO members (name, email) VALUES (%s, %s)", (name, email))
    db.commit()
    db.close()
    print("Member added.")
def show_members():
    db = connect_to_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM members")
    members = cursor.fetchall()
    db.close()
    for member in members:
        print(member)
def add_book(title, author):
    db = connect_to_db()
    cursor = db.cursor()
    cursor.execute("INSERT INTO books (title, author) VALUES (%s, %s)", (title, author))
    db.commit()
    db.close()
    print("Book added.")
def search_book(title):
    db = connect_to_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM books WHERE title LIKE %s", ('%' + title + '%',))
    books = cursor.fetchall()
    db.close()
    for book in books:
        print(book)
def main():
    create_tables()
    while True:
        print("\nLibrary Management System")
        print("1. Add Member")
        print("2. Show Members")
        print("3. Add Book")
        print("4. Search Book")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            name = input("Enter member name: ")
            email = input("Enter member email: ")
            add_member(name, email)
        elif choice == '2':
            show_members()
        elif choice == '3':
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            add_book(title, author)
        elif choice == '4':
            title = input("Enter book title to search: ")
            search_book(title)
        elif choice == '5':
          print("Exiting... Goodbye!")
          break
        else:
         print("Invalid choice. Try again.")
if __name__ == "__main__":
    main()