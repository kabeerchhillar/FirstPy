rFile = open("books.txt", "r")
#bookLIST = rFile.readlines()
bookLIST = [line.rstrip() for line in rFile]
print bookLIST
rFile.close()

myFile = open("books.txt","a")

def input_destinations(user_input):
    if user_input == "1":
        boom = str(raw_input("Enter the name"))
        bookLIST.append(boom)
        myFile.write(boom + "\n")
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

def main():
    main_input = 0

    while main_input != 7:
        print("What do you  like to do \n 1. Add a Name\n 2. find a name \n 3. print the list \n 4. delete a name \n 5. Find book with substring \n 6. find year of publishment \n 7.exit")
        main_input = input(": ")

        # print(type(main_input))
        input_destinations(str(main_input))

    myFile.close()
    return;


if __name__ == '__main__':
    main()