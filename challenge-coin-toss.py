from random import randint

def coin_roll():
    return randint(0, 1)

hands_tally = 0
tails_tally = 0
sums = 0
num_rolls = 10_000

for trial in range(num_rolls):
    result_trial = coin_roll()
    if result_trial == 0:
        hands_tally += 1
    else:
        tails_tally += 1

    if hands_tally != 0 and tails_tally != 0:
        sums += 1
        hands_tally = 0
        tails_tally = 0

average_flips = num_rolls/sums
print(f"The average to for a coin to land on a both a heads and a tails is {average_flips}")

    
