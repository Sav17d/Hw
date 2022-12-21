import math

#1.
for i in range(1, 1001):
    if i%17 == 0:
        print(i)

#2.
for i in range(1, 1001):
    if "2" in str(i):
        print(i)

#3.
for i in range(1, 10001):
    if str(i) == str(i)[::-1]:
        print(i)

#4.
string = "new string"
print(string.count(" "))

#5
v = ["a", "e", "i", "o", "u", "y"]
input = "ODivniyNoviyMir"
result = []
for c in input:
    if c.lower() not in v:
        result.append(c)
str = "".join(result)

str

#6
string = "new string"

for i in string.split():
    if len(i) <= 5:
        print(i)

#7
string = "new string"

out = {}
for i in string.split():
    out[i] = len(i)
out

#8
l = []
string = "newworld"
for i in string:
    if not (i in l):
        l.append(i)
print(l)

#9
sq = lambda x: x * x
l = [2, 5, 7, 8, 10]
print(list(map(sq, l)))

#10
l = [(1, 1), (2, 3), (5, 3), (2, 8)]
n = {}
for i in l:
    if i[1] == 5 * i[0] - 2:
        n[i] = math.sqrt(math.pow(i[0], 2) + math.pow(i[1], 2))
print(n)

#11
l = []
for i in range(2, 28):
    if i%2 == 0:
        l.append(i*i)
print(l)

#12
l = [(1, 1), (2, 3), (5, 3), (2, 8), (1, -11)]
n = 0
for i in l:
    if i[0] >= 0 and i[1] >= 0:
        n = max(n, math.sqrt(math.pow(i[0], 2) + math.pow(i[1], 2)))
print(n)

#13
first = [1, 2, 3, 5, 8]
second = [2, 4, 8, 16, 32]

l = lambda x, y: (x + y, x - y)

print(list(map(l, first, second)))

#14
l = ['43141', '32441', '431', '4154', '43121']
new = []
for i in l:
    n = int(math.pow(int(i), 2))
    if n%2 == 0:
        new.append(n)

new

#15
input = """name,Petya,Vasya,Masha,Vova
grade,5,5,8,3
subject,math,language,physics,math
year,1999,2000,1995,1998"""

new = []
m = {}
for i in input.split("\n"):
    sp = i.split(",")
    m[sp[0]] = sp[1:]

for name, grade, subject, year in zip(m["name"], m["grade"], m["subject"], m["year"]):
    new.append({"name": name, "grade": grade, "subject": subject, "year": year})

new

#16
fst = [[11.9, 12.2, 12.9],
    [15.3, 15.1, 15.1], 
    [16.3, 16.5, 16.5],
    [17.7, 17.5, 18.1]]
fin = [61.2, 61.3, 62.6]   


l = list(zip(*fst))
new = []
for i in l:
    new.append(sum(i))
new