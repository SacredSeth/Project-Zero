# Functions
def int_checker(question, exit_code="xxx"):
    """ Function to make sure user inputs and integer """

    while True:

        test_exit = input(question)

        if test_exit == exit_code or test_exit == exit_code[0]:
            return 1

        try:
            response = int(test_exit)

            if response > 0:
                return response
            else:
                print("Please enter an integer greater than 0\n")

        except ValueError:
            print("Please enter an integer\n")


# Main
test = int_checker("Input a number: ")

if test == 1:
    print("You left")
else:
    print(f"Your number is: {test}")
