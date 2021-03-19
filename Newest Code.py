myList = []

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
6. print contents of list
7. Quit program""")
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
    print(myList(int(indexPos)))
    
def randomSearch():
    print("Random Search?!?")
    print(myList[random.randint(0, len(myList)-1)])

def linearSearch():
    print(" We're gnna check out each item one at a time in your list! This sucks.")
    searchItem = input("what you looking for, partner?  ")
    for x in range(len(myList)):
        if myList[x] == int(searchItem):
            print("Your item is at index position  {}".format(x))
    

if __name__ == "__main__":
    mainProgram()
