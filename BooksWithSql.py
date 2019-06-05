import DataSql

rFile = open("books.txt", "r")
#bookLIST = rFile.readlines()
bookLIST = [line.rstrip() for line in rFile]
print bookLIST
rFile.close()

myFile = open("books.txt","a")

#
#   MyBook Schema :
#   id integer PRIMARY KEY
#   name text NOT NULL
#   author text
#   year integer
#   doIHaveIt boolean

def create_my_book_table(conn):
    sql_create_books_table = """
                            CREATE TABLE IF NOT EXISTS projects (  id integer PRIMARY KEY,
                            name text NOT NULL,
                            author text,
                            year integer,
                            DoIHaveIt integer
                            )"""
    if conn is not None:
        DataSql.create_table(conn,sql_create_books_table)
    else:
        print("Error! cannot create the database connection.")

def input_destinations(user_input):
    if user_input == "0":
        connection = DataSql.create_database("myBooks.db")
        create_my_book_table(connection)
        return connection
    if user_input == "1":
        add_book()
    elif user_input == "2":
        boo = str(raw_input("Enter the name"))
        print boo
        if boo in bookLIST:
            print("yeahhh .. I found the book")
        else :
            print("nooooo .... Sorry Cant find it")
    elif user_input == "3":
        print bookLIST
    elif user_input == "4":
        bo = str(raw_input("Enter the name"))
        if bo in bookLIST:
            index = bookLIST.index(bo)
            del bookLIST[index]
        else:
            print "No such book found"
            return
        with open("books.txt", "r") as f:
            lines = f.readlines()
        with open("books.txt", "w") as f:
            for line in lines:
                if line.strip("\n") != bo:
                    f.write(line)
    elif user_input == "5":
        b = str(raw_input("Enter the substring name"))
        for book in bookLIST:
            if b in book:
                print book
    elif user_input == "6":
        year = str(raw_input("Enter the year"))
        for book in bookLIST:
            splitStr = book.split(", ")
            if year == splitStr[1]:
                print splitStr[0]
    elif user_input == "7":
        bookname = str(raw_input("enter the book"))
        for book in bookLIST:
            splitStr = book.split(", ")
            if bookname == splitStr[0]:
                print splitStr[1]
    elif user_input == "8":
        it = str(raw_input("enter the name"))
        for book in bookLIST:
            splitStr = book.split(", ")
            if it == splitStr[0]:
                print splitStr[2]
    elif user_input == "9":
        h = str(raw_input("enter the name"))
        for book in bookLIST:
            splitStr = book.split(", ")
            if h == splitStr[0]:
                if splitStr[3] == "yes":
                    print "I have read the Book"
                else:
                    print "I have not read the Book"


def main():
    main_input = 0

    while main_input != 10:
        print("What do you  like to do \n "
              "                           0. Create Database and Table"
              "                           1. Add a Name\n "
              "                           2. find a name \n "
              "                           3. print the list \n "
              "                           4. delete a name \n "
              "                           5. Find book with substring \n "
              "                           6. find book using year \n "
              "                           7. find year of publishment \n "
              "                           8. find how many times kabeer has read the book \n "
              "                           9. find if kabeer has the book or not \n "
              "                           10. exit");
        main_input = input(": ")

        # print(type(main_input))
        input_destinations(str(main_input))

    myFile.close()
    return


if __name__ == '__main__':
    main()