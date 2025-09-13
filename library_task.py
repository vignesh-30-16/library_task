# Main class
class Library:
    # book details
    libraryBookDetails = [
        {
            "title": "Do Epic Shit's",
            "book_id": 1,
            "available_copies": 30,
            "tookTheBook": 0,
        },
        {
            "title": "A Girl Behind Star",
            "book_id": 2,
            "available_copies": 40,
            "tookTheBook": 0,
        },
        {
            "title": "Essentialism",
            "book_id": 3,
            "available_copies": 50,
            "tookTheBook": 0,
        },
    ]

    # user details
    def __init__(self, userId, userName):

        self.userId = userId
        self.userName = userName

    # View all the books
    def view_books(self):
        for i in Library.libraryBookDetails:

            print(
                f"Book Id :{i['book_id']}\nTitle :{i['title']}\nAvailable Copies :{i['available_copies']}\n"
            )

    # function for Borrow books
    def borrow_book(self, userBookId):

        for i in Library.libraryBookDetails:

            if userBookId == i["book_id"]:

                try:
                    # how many Copies need
                    num_copies = int(input("\nEnter the How many Copies need: "))

                except ValueError as e:

                    print(f"\nMessage:{e}")

                # number of copies is more than available copies and out of stock
                if num_copies > i["available_copies"] and i["available_copies"] != 0:

                    print(
                        "You Enter the more then available copies (OR) you didn't Enter the Correct values "
                    )
                    return

                # user can Borrow copies
                else:
                    i["available_copies"] -= num_copies
                    i["tookTheBook"] += num_copies

                    print(
                        f"\nBook Title:{i['title']}\nBook Id:{i['book_id']}\nTotally {self.userName} Borrowed copies:{i['tookTheBook']}\nFinal Available Copies are:{i['available_copies']}\n"
                    )
                    return

        # alert for Wrong Book ID
        else:
            print("Wrong Book ID pleas check it")

    # function for return books
    def return_book(self, userBookId):

        for i in Library.libraryBookDetails:

            # user give values and stored is checking and took book nor in be 0
            if userBookId == i["book_id"] and i["tookTheBook"] != 0:

                try:
                    #  how many Copies you return
                    num_copies = int(input("\nEnter the How many Copies need: "))
                except ValueError as e:

                    print(f"Message:{e}")

                # number of copies is more than available copies and more then you Borrow
                if num_copies > i["available_copies"] or num_copies > i["tookTheBook"]:

                    print(
                        f"Trying to cancel more then you Borrow and Available copies are {i['available_copies']} (OR) Trying more then the Available copies"
                    )

                    return

                # user can return the book function
                else:
                    i["available_copies"] += num_copies
                    i["tookTheBook"] -= num_copies

                    print(
                        f"\nBook Title:{i['title']}\nBook Id:{i['book_id']}\nTotally {self.userName} Return copies:{i['tookTheBook']}\nFinal Available Copies are:{i['available_copies']}\n"
                    )
                    return

        # alert for Wrong Book ID and didn't Borrow any Book copies
        else:
            print("Wrong Book ID (OR) You didn't Borrow any Book copies ")


# object for class
userOne = Library(123, "vignesh")

# while for menu
while True:

    # User input for menu
    try:
        userInput = int(
            input(
                "1-view books\n2-borrow book\n3-return book\n4-Exit\nEnter the value: "
            )
        )
    except ValueError as e:

        print(f"Message:{e}")

    # To access View book
    if userInput == 1:
        userOne.view_books()

    # To access borrow book
    elif userInput == 2:

        try:
            # for use chose the book id
            userForBookID = int(input("Enter the book Id to chose: "))

        except ValueError as e:

            print(f"Message:{e}")

        else:
            userOne.borrow_book(userForBookID)

    # To access Return book
    elif userInput == 3:

        try:
            # for use chose the book id
            userForBookID = int(input("Enter the book Id to chose: "))

        except ValueError as e:

            print(f"Message:{e}")

        else:
            userOne.return_book(userForBookID)

    # To Exit
    elif userInput == 4:
        print("Exiting")
        break

    # for wrong key
    else:
        print("Please Enter the correct menu value (1-4) ")
