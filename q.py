a = [19, 17, 24, 1, 100, 25, 846, 39]
i = 0
min = a[i]
max = a[i]
while i < len(a):
    if a[i] < min:
        min = a[i]
    if a[i] > max:
        max = a[i]
    i = i + 1
print ("min =", min,"max =", max)


A = {0: 0, 1: 1}
def fib(n):
    if n in A:
        return A[n]
    A[n] = fib(n-1) + fib(n-2)
    return A[n]
print(fib(15))


def Contains(s: str):
l = ["й", "ц", "к", "н", "г", "ш", "щ", "з", "х", "ф", "в", "п", "р", "л", "д", "ж", "ч", "с", "м", "т"]
for x in s:
if x in l:
return True
return False

def Split(s: str) -> list:
l = []
ss = ""
for x in s:
if x == " " or x == ', ' or x == '. ' or x == '? ' or x == '! ':
l.append(ss)
ss = ""
else:
ss += x
l.append(ss)
for x in l:
if Contains(x):
print(x)

def CreateDictionary(l: list) -> dict:
d = dict()
for x in l:
d[x] = l.count(x)
return d

def Sq(x) -> bool:
from math import sqrt
for i in range(1, int(sqrt(x)+1)):
if x == i*i:
return True
return False

def CreateSets(l: list):
event = set()
sq = set()
for x in l:
if x % 2 == 0:
event.add(x)
for x in l:
if Sq(x):
sq.add(x)
print(event)
print(sq)
print("Intersection: ", event.intersection(sq))
print("Union: ", event.union(sq))
print("Difference: ", event.difference(sq))
print("Symmetric Difference: ", event.symmetric_difference(sq))



