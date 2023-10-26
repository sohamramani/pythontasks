userinput = input("Enter text : ")
if userinput.isupper():
    print (userinput, "The entered text is in uppercase")
elif userinput.islower():
    print(userinput, "The entered text is in lowercase")
else :
    print(userinput, "The entered text is a mix of both upper and lower case letters.")

for value in userinput :
    if value.islower():
         print("The ASCII value of '" + value + "' is", ord(value))
