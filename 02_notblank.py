def not_blank(question):
    """checks that a user has not left a response blank"""

    while True:
        response = input(question)

        if response != "":
            return response

        print("You cannot leave this blank, Please enter a response\n")


# main
who = not_blank("Please enter your name: ")
print(f"\nHello {who}")
