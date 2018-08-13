num = int(input("Enter a number "))
if num%2 == 0:
    print("even")
else:
    print("odd")
num1 = int(input("Enter another number "))
if num1%4 == 0:
    print("Divisible by 4")
else:
    check = int(input("Enter check number"))
    if check%num1 == 0:
        print("Divisible")
    else:
        print("Not divisible")
