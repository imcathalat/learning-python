import random

def coin_flip():
        if random.randint(0, 1) == 0:
            return "heads"
        else:
            return "tails"

heads_tally = 0
tails_tally = 0

for trial in range(10_000):
    if coin_flip() == "heads":
        heads_tally += 1
    else:
        tails_tally += 1

if heads_tally > tails_tally:
    ratio = heads_tally/tails_tally
    print(f"The ration of heads to tails is {ratio}")
else:
    ratio = tails_tally/heads_tally
    print(f"The ration of tails to heads is {ratio}")
