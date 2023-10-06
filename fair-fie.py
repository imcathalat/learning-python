from random import randint

def roll():
    return randint(1, 6)

sums = 0
for i in range(10_000):
    sums += roll()

average = sums/10000

print(f"The average result of 10.000 rolls is {average}")
