## 2/16/19 ##

import math
from fractions import Fraction


class Person:
    def __init__(self, age, gender, name):
        self.a = age
        self.g = gender
        self.n = name
    def printInfo(self):
        if(self.g == 'm' or self.g == 'M'):
            pronoun = 'his'
        else:
            pronoun = 'her'
        print('Name is ' + self.n + ' and ' + pronoun + 'age' + ' is ' + self.a + ' years old')

# name = input('What is your name?')
# age = input('What is your age?')
# gender = input('What is your gender?')
#
# newPerson = person(age, gender, name)
# print(newPerson.printInfo())


def primenumberchecker(num):
    if num > 1:
        for i in range(2, num):
            if(num % i) == 0:
                print(str(num) + ' is not a prime number, because ' + str(i) + ' x ' + str(int((num/i))) + ' = '
                      + str(num))
                break
        else:
            print(str(num) + ' is a prime number!')

    else:
        print(str(num) + ' is not a prime number!')


# num1 = input('Type a number: ')
# intNum1 = int(num1)
# primenumberchecker(intNum1)

def quadCalc(a, b, c):
    intA = int(a)
    intB = int(b)
    intC = int(c)
    if a != 0 and b != 0 and c != 0:
        if a == 1:
            a = ''
        elif b == 1:
            b = ''
        print(str(a) + 'x^2 + ' + str(b) + 'x + ' + str(c))
        discrim = (math.pow(float(intB), 2)) - 4*float(intA)*float(intC)
        if(discrim < 0):
            print('Solution is imaginary, because discriminant is negative.')
        else:
            sol1 = ((-1*intB) + math.sqrt(discrim)) / (2*intA)
            sol2 = ((-1*intB) - math.sqrt(discrim)) / (2*intA)
            finalSol1 = Fraction(float(sol1)).limit_denominator()
            finalSol2 = Fraction(float(sol2)).limit_denominator()
            if sol1 == sol2:
                print('x = ' + str(finalSol1))
            else:
                print('x = ' + str(finalSol1))
                print('x = ' + str(finalSol2))
    else:
        print('Not a valid quadratic')

# a = input("Give the a value of quadratic: ")
# b = input("Give the b value of quadratic: ")
# c = input("Give the c value of quadratic: ")
#
# inta = int(a)
# intb = int(b)
# intc = int(c)
#
# quadCalc(inta, intb, intc)

###### INHERITANCE ####### part of Object-Orientated program


class Parent:
    def __init__(self):
        print("This is the parent class")
    def parentFunc(self):
        print("This is the parent function")

class Child(Parent): # inherits the parent class traits
    def __init__(self):
        print("this is the child class")
    def childFunc(self):
        print("this is the child function")

# c = Child()
# c.childFunc()
# c.parentFunc() # inherits the function of the parent class


class Father:
    def __init__ (self):
        pass
    def test(self):
        print('father')
class Son(Father):
    def __init__(self):
        pass
    def test(self): # overiding the parent class by reinitializing the test function
        print('son')

new = Son()
print(new.test())






