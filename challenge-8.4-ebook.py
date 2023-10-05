number = int(input("Enter a positive integer: "))

for divisor in range(1, number+1):
    if number % divisor == 0:
        print(f"{divisor} is a factor of {number}")
