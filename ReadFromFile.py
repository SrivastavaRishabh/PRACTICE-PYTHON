import urllib.request

count_dict = {}
data = urllib.request.urlopen('http://www.practicepython.org/assets/nameslist.txt')
for line in data:
    line = str(line)
    line = line.replace("\\n", "")
    line = line.replace("b'", "")
    line = line.replace("'", "")
    if line in count_dict:
        count_dict[line] += 1
    else:
        count_dict[line] = 1
print(count_dict)