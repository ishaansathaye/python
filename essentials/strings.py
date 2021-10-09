## 2/14/19 ##

sentence = "Learning Python is fun"
print(sentence[5].upper() + "t" + " " + sentence[16] + sentence[17] + " the best in the world")

print(sentence[0:7] + "'")
print(sentence[0:5])
print(sentence[:-13])

sent = '%s %s %s is the President of the US'

print(sent%('Donald', 'J.', 'Trump'))

setOfNumbers = 'there are %d people in this house'

print(setOfNumbers%(4))

sentenceTwo = '%s is %d years old'

print

print(sentenceTwo%('Ishaan', 16))

todolist = ['hw', 'chores', 'reading', 'coding']

print(todolist[0] + " and " + todolist[3] + " are fun.")

print(todolist[1:2])

print

todolist.append('things')

todolist[0] = 'fun'

del todolist[0]
print()
print(todolist)

print(len(todolist) - 1)

shopList = ['Bananas', 'oranges', 'apples']

shopList[0] = 'bananas'

combinedList = todolist + shopList

print(combinedList * 2)

listNum = [1, 2,3,4,5,6,7,8,9,12341234, -1, -10010000]
print

print(max(listNum), min(listNum))

############## SLICING ################

string = "something"
print(string[-1]) # gives you last character
print(string[::-2]) # reverses the string if -1 and anything greater it only prints things for every 2 characters starting with 0,1,2...
print(string[::2]) # skips every how many characters and prints only those so this one would be that it would print every second character starting with 0
print()
print(string[-3::]) #prints last how many characters
print(string[2::]) # prints starting from character 2
print()
print(string[:-2]) # prints everything but last two
print(string[:2]) # prints only first two elements so it excludes element 2
print()
print(string[-2:]) # same as second group **look above**
print(string[2:]) # same as second group **look above**