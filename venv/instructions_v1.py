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
show_instructions = yes_no("Have you played the game before?")
print("You chose {}" .format(show_instructions))
print()
having_fun = yes_no("Are you having fun?")
print("You said {} to having fun" .format(having_fun))

if show_instructions == "yes" :
    instruction()

