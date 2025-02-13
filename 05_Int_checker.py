# Functions
def int_checker(question, exit_code="xxx"):
    """ Function to make sure user inputs an integer greater than 0"""

    while True:

        # tests for exit code
        test_exit = input(question)

        if test_exit == exit_code or test_exit == exit_code[0]:
            return 0

        try:
            response = int(test_exit)

            if response > 0:
                return response
            else:
                print("Please enter an integer greater than 0")

        # incase input isn't an integer
        except ValueError:
            print("Please enter an integer")


# Main
while 1:
    test = int_checker("Input a number: ")

    if test == 0:
        print("You left")
        break
    else:
        print(f"Your number is: {test}\n")
