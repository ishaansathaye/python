def duplicate(array):
    length = len(array)
    for i in range(0, length):
        for j in range(i+1, length):
            if(array[i] == array[j]):
                array[i] = ""

    for item in array:
        if(item == ""):
            array.remove(item)

    print(array)



something = ["cat", "dog", "cat", "hamster", "hamster"]

duplicate(something)