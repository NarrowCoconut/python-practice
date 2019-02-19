import random
a = -50
b = 50
myList = []
i = 0
size = 4
even = 0
odd = 0
w = 0
positive = 0
negative = 0

while i < size:
    randNum = random.randint(a, b)
    myList.append(randNum)
    i += 1

m = max(myList)
n = min(myList)
ave = sum(myList)/len(myList)
aveMN = (m + n)/2


def check(num):
    return bool(num % 2 == 0)


def within(num):
    return bool(-25 <= num <= 25)


def plus(num):
    return bool(num > 0)


def minus(num):
    return bool(num < 0)


for x in myList:
    if check(x):
        even += 1
    else:
        odd += 1


for x in myList:
    if within(x):
        w += 1

for x in myList:
    if plus(x):
        positive += 1

for x in myList:
    if minus(x):
        negative += 1

print(myList)
print('even =', even)
print('odd =', odd)
print('within 25 =', w)
print('negative =', negative)
print('positive =', positive)
print('max =', m)
print('min = ', n)
print('average =', ave)
print('average max min =', aveMN)
