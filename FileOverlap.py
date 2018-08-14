import urllib.request


prime = []
data1 = urllib.request.urlopen('http://www.practicepython.org/assets/primenumbers.txt')
for line in data1:
    line = str(line)
    line = line.replace("\\n", "")
    line = line.replace("b'", "")
    line = line.replace("'", "")
    prime.append(line)

happy = []
data2 = urllib.request.urlopen("http://www.practicepython.org/assets/happynumbers.txt")
print(prime)
for line in data2:
    line = str(line)
    line = line.replace("\\n", "")
    line = line.replace("b'", "")
    line = line.replace("'", "")
    happy.append(line)

print(happy)
overlap = [i for i in prime if i in happy]
print(overlap)
