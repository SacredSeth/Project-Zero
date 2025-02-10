# Functions
def string_checker(question, ans_list, num_letters=1):
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
            elif response == item[:num_letters]:
                return item

        print(f"Please choose an option from {ans_list}\n")


# Main
y_n = ['yes', 'no']
payment_list = ['cash', 'credit']

like_coffee = string_checker("Do you like coffee? ", y_n)
print(f"You {like_coffee} like coffee")

pay_method = string_checker("Payment method: ", payment_list, 2)
print(f"You are paying with {pay_method}")
