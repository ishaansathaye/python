def validPalindrome(s):
    reverse = s[::-1]
    if(reverse == s):
        print("Palindrome")
    else:
        print("Nope")

word = input("Type a word: ")
stringWord = str(word)
validPalindrome(stringWord)







