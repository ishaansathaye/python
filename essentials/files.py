## 6/25/19 ##

########### Creating, Reading, Writing Files ############

testFile = open("Test.txt", 'w') # overwrite/write into the file
testFile.write("Python is an interpreted, high-level, general-purpose programming language\n")
testFile.write("Created by Guido van Rossum and first released in 1991\n")
testFile.write("Python's design philosophy emphasizes code readability with its notable use of significant whitespace\n")
testFile.write("Its language constructs and object-oriented approach aim to help programmers write clear, logical code for small and large-scale projects")
testFile.close()

# file = open("Test.txt", "r") # read the file
# text = file.read()
# print(text)
# file.close()

newFile = open("Test.txt", "a") # append a file and "a+" is to read and append
newFile.write("\nPython is a great language overall!")
newText = newFile.read()
# print(newText) # only use this with a+
newFile.close()



