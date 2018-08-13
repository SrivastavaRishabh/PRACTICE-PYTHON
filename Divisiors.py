num = int(input("Enter a number"))
b = []
for i in range(1,num):
    if num % i == 0:
        b.append(i)
print(b)