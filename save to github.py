myList = []

def mainProgram():
    while True:
        try:
            print("Hello, there! Let's work with lists!")
            print("Choose from the following options. Type a number below!")
            choice = input("""
1. Add to a list ,
2. Return the value at an index position!,
3.Exit program   """)
            if choice == "1":
                addToList()
            elif choice == "2":
                indexValues()
            elif choice == "3":
                random.Search()
            else:
                break
        except:
            print("You made a whoopsie")

def addToList():
    print("Addint to a list! Great Choice!")
    newItem = input("type an integer here!   ")
    myList.append(int(newItem))

def indexValues():
    print("Ohhh! I heard you need a particular piece of data!")
    indexPos = input("what index postition are you curious about  ")
    print(myList(int(indexPos)))

if __name__ == "__main__":
    mainProgram()
