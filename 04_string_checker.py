# Functions
def string_checker(question, ans_list):
    """Checks that the user entered the full word OR the first letter"""

    if ans_list is None:
        ans_list = ["yes", "no"]
    while True:

        response = input(question).lower()

        for item in ans_list:

            # check for the entire word
            if response == item:
                return item

            # check for the first letter of the response
            elif response == item[0]:
                return item

        print(f"Please choose an option from {ans_list}\n")


# Main
levels = ['easy', 'medium', 'hard']

like_coffee = string_checker("Do you like coffe? ", ['yes', 'no'])
coffee_level = string_checker("choose a level of coffee: ", levels)

