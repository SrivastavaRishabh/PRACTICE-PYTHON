a = int(input("Enter a number : "))
b = int(input("Enter a number : "))
c = int(input("Enter a number : "))
if a > b:
    if b > c:
        print("", b, " is maximum ")
    else:
        print("", c, " is maximum ")
elif b > c:
    if c > a:
        print("", b, " is maximum ")
    else:
        print("", a, " is maximum ")
elif c > a:
    if a > b:
        print("", c, " is maximum")
    else:
        print("", b, " is maximum ")
else:
    print("All are equal ")
