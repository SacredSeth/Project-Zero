# Functions
def num_check(question, datatype,  exit_code="xxx"):
    """ Function to make sure user inputs an integer / float that is greater than 0 """

    # get correct error message for data type
    if datatype == int:
        err = "Please enter an integer greater than 0"
    else:
        err = "Please enter a number greater than 0"

    while True:

        # tests for exit code
        test_exit = input(question).lower()

        if test_exit == exit_code or test_exit == exit_code[0]:
            return 0

        # Case for integers
        if datatype == int:
            try:
                response = datatype(test_exit)

                if response > 0:
                    return response
                else:
                    print(err)

            except ValueError:
                print(err)

        # case for others (mostly float)
        else:
            try:
                response = datatype(test_exit)
                if response > 0:
                    return response
                else:
                    print(err)

            except ValueError:
                print(err)


# Main

# loop for testing
while 1:
    print()

    my_float = num_check("Please enter a number: ", float)
    print(f"You chose {my_float}")

    if my_float == 0:
        print("You left")
        break
