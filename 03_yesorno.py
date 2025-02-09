# Functions
def yes_or_no(question):
    """Checks if a user responds yes / y or no / n"""

    cor_resp = {"yes": "yes", "y": "yes", "no": "no", "n": "no"}

    while True:
        response = input(question).lower()

        if response in cor_resp:
            return cor_resp[response]

        print("Please enter \"yes\" or \"no\"\n")


# Main

for _ in range(6):
    want_instructions = yes_or_no("Do you want to see the instructions? ")
    print(f"You chose {want_instructions}\n")
