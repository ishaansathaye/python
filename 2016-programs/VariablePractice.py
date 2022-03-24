#Created August 12, 2016 at 2:27 PM
def some_code():
    print(" How are you doing?\n"
          " I am doing very fine!!")

some_code()

age = input("How old are you?")

weight = input("How much do you weigh?")

def func(age, weight):
    if age >= 13 and age <= 17:
        if weight >= 141:
            return "over wieght"
        elif weight <= 140:
            return "perfect weight!!!"
    else:
        return "this program is for 13-17 year olds"

print(func(int(age), int(weight)))