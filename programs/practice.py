## 6/3/19 ##

array = [1, 2, 3, 4, 5, 4]


# array.append(6)

for i in array:
    print(i)

print()

array.reverse()

for i in array:
    print(i)

print()

print(len(array))

print()

print(array.count(4))

print()

myArray = [1, 2, 3, 4, 5, 6]
myArray.insert(2, 8839202939)

for i in myArray:
    print(i)

print()

myArray.remove(4)

for i in myArray:
    print(i)



myList = [1, 2, 3, 4, 5, 6]

largest = 10000000000
for i in myList:
    if(i < largest):
        largest = i

print(largest)

sampleList = ['acdba', 'mommy', 'something', 'dad', 'd']

for i in sampleList:
    if((len(i) >= 2) and (i[0] == i[-1])):
        print(i)


myTuple = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

def last(n):
    return n[-1]

def sort_list(myTuple):
    return sorted(myTuple, key=last)

print(sort_list(myTuple))

onelist = [1, 2, 3, 4, 5]
twoList = [9, 8, 7, 6, 1]

for i in onelist:
    for j in twoList:
        if(i == j):
            print(i)

things = [1, 2, 3, 4, 5, 6, 7]

for i in things:
    if((i%2) == 0):
        things.remove(i)
print(things)

import itertools

thingies = [1, 2, 3]

print(list(itertools.permutations(thingies)))




lists = [2, 1, 4, 54, 3, -1, 3, 2, 1]
unique = []

for i in lists:
    if i not in unique:
        unique.append(i)
unique.sort()
print(unique)









