import random
myList = []
unique_list = []


def mainProgram():
    while True:
        try:
            print("Hello, there! Let's work with lists!")
            print("Choose from the following options. Type a number below!")
            choice = input("""
1. Add to a list
2. Add a bunch o numbers
3. Return the value at an index position!
4. Random Search
5. Linear Search
6. Sort list
7. print contents of list
8. Quit program""")
            if choice == "1":
                addToList()
            elif choice == "2":
                addABunch()
            elif choice == "3":
                indexValues()
            elif choice == "4":
                randomSearch()
            elif choice == "5":
                linearSearch()
            elif choice == "6":
                sortList
            elif choice == "8":
                binSearch = input("What number are you looking for?  ")
                recursiveBinarySearch(unique_list, 0, len(unique_list)-1, int(binSearch))
            elif choice == "9":
                binSearch = input("What number are you looking for?  ")
                result = iterativeBinarySearch(unique_list, int(binSearch))
                if result != -1:
                    print("Your number is at index position {}".format(result))
                    else:
                        print("Your number is not found in that list, bud!")
            elif choice == "7":
                print(myList)
            else:
                break
        except:
            print("You caught an error!")

def addToList():
    print("Addint to a list! Great Choice!")
    newItem = input("type an integer here!   ")
    myList.append(int(newItem))

def addaBunch():
    print("we're gonna adda bunvh of integers here!")
    numToAdd = input("how many new integers would you like to add?  ")
    numRange = input("And how high would you like these numbers to go?  ")
    for x in range(0, int(numToAdd)):
        myList.append(random.randint(0, int(numRange)))
    print("your list is now complete.")

def indexValues():
    print("Ohhh! I heard you need a particular piece of data!")
    indexPos = input("what index postition are you curious about  ")
    print(myList[int(indexPos)])

def sortList(myList):
    print("A little birdie told me you want some data")
    for x in myList:
        if x not in unique_list:
            unique_list.append(x)
    unique_list.sort()
    showM = input("wanna see your new list?  Y/N")
    if showMe.lower() == "y":
        print(unique_list)
        
    
def randomSearch():
    print("Random Search?!?")
    print(myList[random.randint(0, len(myList)-1)])

def linearSearch():
    print(" We're gnna check out each item one at a time in your list! This sucks.")
    searchItem = input("what you looking for, partner?  ")
    for x in range(len(myList)):
        if myList[x] == int(searchItem):
            print("Your item is at index position  {}".format(x))

def printLists():
    if len(unique_list) == 0:
        print(myList)
    else:
        whichOne = input("Which list? Sorted or unsorted?  ")
        if whichOne.lower() == "sorted":
            print(unique_list)
        else:
            print(myList)
            
def recursiveBinarySearch(unique_list, low, high, x):
    if high >= low:
        mid = (high + low) // 2

        if unique_list[mid[ == x:
            print("Your number is at index postion {}".format(mid))

        elif unique_list[mid] > x:
            return recursiveBinarySearch(unique_list, low, mid - 1, x)

        else:
            return recursiveBinarySearch(unique_list, mid + 1, high, x)
    else:
        print("Your number isn't here!")

def iterativeBinary search(unique_list, x):
    low = 0
    high = len(uniqeu_list)-1
    mid = 0

    while low <= high:
        mid = (high + low)

        if unique_list[mid] < x:
            low = mid + 1

        elif unique_list[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1

if __name__ == "__main__":
    mainProgram()
