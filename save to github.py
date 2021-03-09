def mainProgram():
    myList = []
    print("Hello, there! Let's work with lists!")
    print("Choose from the following options. Type a number below!")
    choice = input("1. Add to a list , 2. Return the value at an index position!"  )
    if choice == "1":
        addToList()
    elif choice == "2":
        indexValues()
    #TO ADD: 1. A way to loop the action, 2. A way to quit, 3. Think of respond.

def addToList():
    print("Addint to a list! Great Choice!")
    newItem = input("type an integer here!   ")
    myList.append(int(newItem))

def indexValues():

if__name__=="__main__":
    mainProgram()
