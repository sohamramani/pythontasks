inputparagraph = input("Please enter paragraph: ")
print("\n")
print(inputparagraph)

def myfunction():
    global inputparagraph
    print("Operations:  1) edit  2) delete  3) exit")
    operation = input("please select a operation: ")
    if operation == "1":
        editword = input("Which word do you want to change?: ")
        newword = input("Enter a new word: ")
        inputparagraph = inputparagraph.replace(editword, newword)
        print(inputparagraph)
        myfunction()
    elif operation == "2":
        deleteword = input("Which word do you want to delete: ")
        inputparagraph = inputparagraph.replace(deleteword, "")
        print(inputparagraph)
        myfunction()
myfunction()