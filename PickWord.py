import urllib.request
import random


def randomword():
    data = urllib.request.urlopen('http://norvig.com/ngrams/sowpods.txt')
    word = []
    for line in data:
        line = str(line)
        line = line.replace("\\n", "")
        line = line.replace("b'", "")
        line = line.replace("'", "")
        line = line.replace("\\r", "")
        word.append(line)
    print(random.choice(word))


randomword()
