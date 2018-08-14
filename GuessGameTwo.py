def play():
    i = 0
    j = 100
    m = 50
    counter = 1
    print("Please guess a number ")
    print("Is ", str(m), " your number ? \n 0 for its low \n 1 for it's high \n 2 yes it is")
    condition = int(input())
    while condition != 2:
        counter += 1
        if condition == 0:
            i = m + 1
        elif condition == 1:
            j = m - 1

        m = (i + j)//2
        print("Is ", str(m), " your number ? \n 0 for its low \n 1 for it's high \n 2 yes it is")
        condition = int(input())
    print("It took", counter, "times to guess your number")


play()
