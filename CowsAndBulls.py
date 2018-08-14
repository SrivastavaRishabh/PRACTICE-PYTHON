from random import randint


def play(num1, n1):
    cb = [0, 0]
    for i in range(4):
        if num1[i] in n1 and num1[i] == n1[i]:
            cb[0] += 1
        elif num1[i] in n1 and num1[i] != n1[i]:
            cb[1] += 1
    return cb


if __name__ == "__main__":
    n = str(randint(1000, 9999))
    guess = 0
    start = True
    while start:
        num = input("Guess a four digit number : ")
        if len(num) != 4:
            print("Enter a four digit number")
        elif num == 'exit':
            print("Oops! The number was : ",n)
            break
        else:
            cowsbulls = play(num, n)
            guess += 1
            print("You have ", str(cowsbulls[0]), " cows and ", str(cowsbulls[1]), " bulls ")
            if cowsbulls[0] == 4:
                start = False
                print("You won the game in ", guess, " guesses ")
                break
            else:
                print("Try again")
