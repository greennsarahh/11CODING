
# set balance for testing purpose
balance = 5

rounds_played = 6

play_again = input("Press <enter> to play...").lower()
while play_again == "":

    # increase number of rounds played
    rounds_played += 1

    # print rounds number
    print()
    print("*** Rounds #{} ***".format(rounds_played))
    balance -= 1
    print("Balance: ",balance)
    print()

    if balance < 1:
        play_again = "xxx"
        print("Sorry you have run out of money")
    else:
        play_again = input("Press enter to play again or 'xxx' to quit")
