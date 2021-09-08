# set balance for testing purpose
balance = 5

rounds_played = 6

play_again = input("Press <enter> to play...")
while play_again == "":

    # increase number of rounds played
    rounds_played += 1

    # print rounds number
    print(rounds_played)
    balance -= 1
    print("Balance: ",balance)
