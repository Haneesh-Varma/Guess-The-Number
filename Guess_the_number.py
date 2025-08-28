import random
number = random.randint(0,101)
userno = int(input("Guess the number bwtween 1-100: "))
no_of_tries = 1
while userno != number:
    # userno = int(input("Guess the number: "))
    if userno > number:
        print("Your number is greater than the actual number, keep trying 😉")
        no_of_tries += 1
        userno = int(input("Guess the number: "))
        continue
    else:
        print("Your number is lesser than the actual number, keep trying 😉")
        no_of_tries += 1
        userno = int(input("Guess the number: "))
        continue
print(f"Great you've guessed the number in you're {no_of_tries} try")