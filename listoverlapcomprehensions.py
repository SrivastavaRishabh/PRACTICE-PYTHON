from random import randint
a = []
b = []
for i in range(randint(0,20)):
    a.append(randint(0,30))
for i in range(randint(0, 20)):
    b.append(randint(0,30))
print("List A : ",a)
print("\nList B: ",b)
c = [i for i in a if i in b]
print("\nList C: ",list(set(c)))