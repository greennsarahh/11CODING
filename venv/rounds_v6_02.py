import random
# set balance for testing purpose
balance = 5
rounds_played = 0

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

    if balance < 1:
        play_again = "xxx"
        print("Sorry you have run out of money")
    else:
        play_again = input("Press enter to play again or 'xxx' to quit")


