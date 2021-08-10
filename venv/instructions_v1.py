# Functions go here
def yes_no(questions):
    valid = False
    while not valid:
        response = input(questions).lower()

        if response == "yes" or response == "y":
            response = "yes"
            return response

        elif response == "no" or response == "n":
            response = "no"
            return response

        else:
            print("please answer yes / no")

def instruction():
    print("**** How to Play ****")
    print()
    print("The rules of the game go here")
    print()
    return ""


# main routine goes here
played_before = yes_no("Have you played the game before?")
print("You chose {}" .format(played_before))
print()


if played_before == "no":
    instruction()

print("Program continues")
