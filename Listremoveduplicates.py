from random import randint

def generatelist(limit):
    for i in range(limit):
        a.append(randint(1, 30))
    print("List A : ", a)

def removeduplicates(a):
     newlist = [i for i in a]
     return list(set(newlist))

a = []
limit = (randint(1,20))
generatelist(limit)
print("New list : ",removeduplicates(a))
