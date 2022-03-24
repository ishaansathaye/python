## 6/20/19 ##

def factorial(num1):
    product = 1
    step = -1
    if(num1 < 0):
        print('Negative numbers! Cannot factorial!')
    if(num1 == 0):
        print(num1, "! = 0")
    if(num1 > 0):
        for i in range(num1, 1, step):
            product = product*i
        print(num1,"! = " ,product)


# num = input("Input a number: ")
# newNum = int(num)
# factorial(newNum)

def leapYear(year):
    if(year < 0):
        print('year does not exist')
    if(year == 0):
        print('cant do that year')
    if(year > 0):
        if((year%4) == 0):
            print(year, " is a leap year!")
        else:
            print(year, " is not a leap year!")

# year = input('Type a year: ')
# intYear = int(year)
# leapYear(intYear)

something = [1, 2, 4, 78, 100, 101]
largestNumber = 0
for i in something:
    if(i > largestNumber):
        largestNumber = i
print("largest number in the array is", largestNumber)





