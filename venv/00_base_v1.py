import random
# Functions
def num_check(question, low, high):
    error = "Please enter a whole number between 1 and 10\n"

    valid = False
    while not valid:
        try:
            # ask the question
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
rounds_played = 0
played_before = yes_no("Have you played the game before?")
print("You chose {}" .format(played_before))
print()
if played_before == "no":
    instruction()
print("Program continues")

how_much = num_check("How much would you like to play with? ", 0, 10)
print("You will be spending ${}" .format(how_much))
balance = how_much

play_again = input("Press <enter> to play...").lower()
while play_again == "":

    # increase number of rounds played
    rounds_played += 1

    # print rounds number
    print()
    print("*** Rounds #{} ***".format(rounds_played))

    chosen_num = random.randint(1, 100)
    # adjust balance
    # if random # is between 1 and 5
    # user gets unicorn (add 4$ to balance)
    if 1 <= chosen_num <= 5:
        chosen = "unicorn"
        balance += 4
        # if the random num is between 6 and 36
        # user gets donkey (subtract 1$ from balance)
    elif 6 <= chosen_num <= 36:
        chosen = "donkey"
        balance -= 1
    else:
        if chosen_num % 2 == 0:
            chosen = "horse"
        else:
            chosen = "zebra"
            balance -= 0.5

    print("You got a {}. Your balance is ${:.2f}".format(chosen, balance))
    print()

    if balance < 1:
        play_again = "xxx"
        print("Sorry you have run out of money")
    else:
        play_again = input("Press enter to play again or 'xxx' to quit")
