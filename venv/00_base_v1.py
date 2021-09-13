# Functions
def num_check(question, low, high):
    error = "Please eneter a whole number beetween 1 and 10\n"

    valid = False
    while not valid:
        try:
            #ask the question
            response = int(input(question))

            # if the amount is too low/ high give
            if low < response <= high:
                return response


        # output an error
            else:
                print(error)

        except ValueError:
            print(error)

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


how_much = num_check ("How much would you like to play with? ", 0, 10)
print("You will be spending ${}" .format(how_much))
