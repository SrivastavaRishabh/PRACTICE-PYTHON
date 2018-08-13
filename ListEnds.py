from random import randint
a = []
for i in range(randint(0,20)):
    a.append(randint(0,100))
b = []
b.append(a[0])
b.append(a[-1])
print("List a : ",a)
print("\nList b :",b)