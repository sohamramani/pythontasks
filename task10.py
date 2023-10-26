print("the program is for 3x3 matrix addition and multiplication.")
def for_matrix1():    
    try:
        print() 
        print("please enter matrix-1 value below")

        input_matrix1 = []

        values_for_row1 = []
        for i in range(3):
            values_for_row1.append(int(input("Enter value for first row value-{}: ".format(i + 1))))
        print() 

        values_for_row2 = []
        for i in range(3):
            values_for_row2.append(int(input("Enter value for secound row value-{}: ".format(i + 1))))
        print()   

        values_for_row3 = []
        for i in range(3):
            values_for_row3.append(int(input("Enter value for third row value-{}: ".format(i + 1))))
        print()

        input_matrix1.append(values_for_row1)
        input_matrix1.append(values_for_row2)
        input_matrix1.append(values_for_row3)
        print()   

        return input_matrix1
    except ValueError:
        print() 
        print("Please make sure you are entering integer numbers only!")
        for_matrix1()


def for_matrix2():
    try:
        print() 
        print("please enter matrix-2 value below")
    
        input_matrix2 = []

        values_for_row1 = []
        for i in range(3):
            values_for_row1.append(int(input("Enter value for first row value-{}: ".format(i + 1))))
        print()

        values_for_row2 = []
        for i in range(3):
            values_for_row2.append(int(input("Enter value for secound row value-{}: ".format(i + 1))))
        print()

        values_for_row3 = []
        for i in range(3):
            values_for_row3.append(int(input("Enter value for third row value-{}: ".format(i + 1))))
        print()

        input_matrix2.append(values_for_row1)
        input_matrix2.append(values_for_row2)
        input_matrix2.append(values_for_row3)
        print()
        return input_matrix2
    except ValueError:
         print("Please make sure you are entering integer numbers only!")

def addition():
        for i in range(len(matrix1)):   
            for j in range(len(matrix1[0])):
                matrix3[i][j] = matrix1[i][j] + matrix2[i][j]
        for r in matrix3:
            print(r)


def multiply():
    for i in range(len(matrix1)):  
       for j in range(len(matrix2[0])):  
           for k in range(len(matrix2)):  
               matrix3[i][j] += matrix1[i][k] * matrix2[k][j]  
    for r in matrix3: 
        print(r) 


matrix1 = for_matrix1()

matrix2 = for_matrix2()

print("matrix-1: ",matrix1)
print("matrix-2: ",matrix2)

matrix3 = [
            [0,0,0], 
            [0,0,0], 
            [0,0,0]
            ]

while True:
            print(
                "\n1. addition \n"
                "2. multiplication\n"
                "3. Quit\n"
            )
            operation = input("Choose operation: ")

            if operation == "1":
                add_matrix = addition()
                print(f"addition of two 3x3 matrix: {add_matrix}")
            elif operation == "2":
                multiply_matrix = multiply()
                print(f"multiplication of two 3x3 matrix: {multiply_matrix}")
            elif operation == "3":
                break
            else:
                print("Invalid operation. Use '1', '2', or '3'")