## 2/15/19 ##

# dictionaries
shopList = {"bananas": 8, "things": 9, "apples": 10}

print(shopList["bananas"])

shopList["apples"] = 21

del shopList["bananas"]

print(shopList)
print

print(len(shopList))

# tuples:

tupleShopList = ("cherries", "bananas", "apples")

tuple2 = (14, 19, 20)

tuple3 = tupleShopList + tuple2 

del tuple3  # deleted tuple
print
print(len(tuple2))

print(tuple2 * 20)

# conditional statements

if (2 > 3):
    print
    print("hello")
else:
    print
    print("2 is not greater than 3")

if (3 >= 3) and (9 <= 10) and (3 != 2):
    print
    print("hello")
else:
    print
    print("2 is not greater than 3")

age = 21
if (age <= 13):
    print("you are young")
elif (age > 13 and age < 18):
    print("you are in high school")
else:
    print("you are in college or an adult")

# For Loops


list1 = ["apples", "cherries", 'pears']
tuples = (12, 13, 14)

for anItem in list1:
    print
    print(anItem)

for i in range(0, 10):
    print(i)

for i in range(1, 10, 2):
    print
    print(i)

listNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in range(0, 10):
    for j in range(0, 5):
        z = i + j
        print(str(i) + ' + ' + str(j) + ' = ' + str(z))

# While Loops

print
c = 0
while (c <= 5):
    if (c == 5):
        print("c is 5")
    else:
        print(str(c) + " is less than 5")
    c = c + 1

a = 0
print
while (a < 5):
    print (a)
    if (a == 3):  #
        break  # break and does not do anything after
    a = a + 1

# d = 0
# print
# while (d < 5):
#     if (d == 3):
#         continue  # continues and does not do anything afterwards so it will keep running as long 3 == 3
#     print(d)
#     d = d + 1

d = 0
print
while (d < 5):
    d = d + 1  # need this incremental so continue exits when 3 == 3
    if (d == 3):
        continue  # skips printing 3 and anything below it and goes back to start the while loop
    print(d)

print

print('Ishaan'),  # printing on the same line
print('Sathaye')


def passloop():
    e = 0
    while (e < 5):
        e += 1
        if (e == 3):
            pass  # filler code to just execute and do nothing
        print(e)
print
passloop()

# Try and except statements
print

try:
    if(name < 3):
        print('name is less than three')
except:
    print('there is something wrong')

print()
print()

'''FUNCTIONS '''

def afuntion(name):
    print('Your name is ' + name)

afuntion('Ishaan')
print

def sumofnumbers(a, b):
    sum = a+b
    print(sum)

sumofnumbers(1, 2)
print()


def returnAdd(num1, num2):
    sum = num1+num2
    return(sum)   # can use return to use that value stored for another variable or SEND BACK A VALUE
    print('Hello') # will not do this because  there is a return statement

sum = returnAdd(12, 34)

print(sum)
print()
print()


# IN_BUILT FUNCTIONS

print(abs(-234))

print(bool(0))
print(bool(None))
print(bool(1234))

print(dir('string')) # gives all the functions you could do with a string

sent = 'hello'
print(help(sent.upper)) # help functions tells what the function int he parameter does
print(help(sent.splitlines))

sent1 = 'print("Hi")'
eval(sent1) # runs the string as if it is code
exec(sent1) # for running multiple lines of code same thing as EVAL

num = 1
str(num)
int(num)
float(num)


## OBJECT ORIENTATED PROGRAMMING ##
print()

class Personal:
    def gettheName(self):
        print("ishaan")
    def gettheAge(self):
        print('16')

examplePerson = Personal()
examplePerson.gettheAge()
examplePerson.gettheName()

print()

class difPerson:
    def __init__(self, name, age):
        self.n = name
        self.a = age
    def getName(self):
        print('Hello ' + self.n)
    def getAge(self):
        print(self.n + ' is ' + self.a + ' years old')

p1 = difPerson('ishaan', '16')
print(p1.getName())
print(p1.getAge())