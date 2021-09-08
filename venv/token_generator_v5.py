import random

# main routine goes here


STARTING_BALANCE = 100

balance = STARTING_BALANCE
# testing loop to generate 20 tokens

for item in range(0, 10):
    chosen_num = random.randint(1, 100)
    # adjust balance
    # if random # is beetween 1 and 5
    # user gets unicorn (add 4$ to balance)
    if 1 <= chosen_num <= 5:
        chosen = "unicorn"
        balance += 4
        # if the randowm num is beetwen 6 and 36
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

