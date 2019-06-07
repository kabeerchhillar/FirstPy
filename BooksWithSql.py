import DataSql

#
#   MyBook Schema :
#   id integer PRIMARY KEY
#   name text NOT NULL
#   author text
#   year integer
#   doIHaveIt boolean

def add_books(conn,book):
    sql = ''' INSERT INTO my_book (name,author,year,DoIHaveIt)
                VALUES(?,?,?,?); '''
    cur = conn.cursor()
    cur.execute(sql,book)
    return cur.lastrowid


def create_my_book_table(conn):
    sql_create_books_table = """
                            CREATE TABLE IF NOT EXISTS my_book (  
                            id integer PRIMARY KEY,
                            name text NOT NULL,
                            author text,
                            year integer,
                            DoIHaveIt text ); """
    if conn is not None:
        DataSql.create_table(conn,sql_create_books_table)
    else:
        print("Error! cannot create the database connection.")

def input_destinations(user_input,connection):
    if user_input == "0":
        create_my_book_table(connection)

    if user_input == "1":
 #       book_name = str(input("Name the Book "));
 #       book_author = str(input("Name the Author "));
 #       book_year = int(input(" Give the year of book  "));
 #       book_Ihave = str(input(" Do i have the book "));
 #       book = (book_name, book_author, book_year, book_Ihave);
         book = ("abcd", "xxaqws", 1999, "yes");

         add_books(connection,book);

def main():
    main_input = 0

    connection = DataSql.create_database("myBooks.db")

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
        input_destinations(str(main_input),connection)

        book = ("abcd", "xxaqws", 1999, "yes");

        add_books(connection, book);

    return


if __name__ == '__main__':
    main()