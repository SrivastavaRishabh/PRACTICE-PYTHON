from random import randint
num = randint(1, 9)
n = 15
count = 1
while n != "exit" and n != num:
    n = (input("Guess a number or press and enter 'exit' : "))
    if n == "exit":
        break

    n = int(n)

    if n > num:
        print("Guess is high!")
        count += 1

    elif n < num:
        print("Guess is low!")
        count += 1

    else:
        print("You got the number in just ", count, " attempts! ")
