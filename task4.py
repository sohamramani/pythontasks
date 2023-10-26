try:
    first_value = int(input("Enter First Value: "))
    second_value = int(input("Enter Second Value: "))

    # Addition 
    add = first_value + second_value
    print ("Addition : ", add)

    # Subtraction 
    sub = first_value - second_value
    print ("Substraction : ", sub)

    # Multiplication 
    mul = first_value * second_value
    print ("Multiplication : ", mul)

    # Division 
    try:
        div = first_value / second_value
        print ("Division : ", div)
    except Exception as e:
        print("Error: %s" %e)
        
    # Power
    try:
        Power = first_value ** second_value
        print ("Power : ", Power)
    except Exception as e:
        print("Error: %s" %e)

    # Modulo 
    try:
        mod = first_value % second_value
        print ("Modulo : ", mod)
    except Exception as e:
        print("Error: %s" %e)

    #Bitwise Left Shift
    bit_left_first = first_value << second_value
    print ("Left Bitwise Shift : ", bit_left_first)

    #bitwise right shift
    bit_right_second = second_value >> second_value
    print ("Right Bitwise Shift : ", bit_right_second)

    #bitwise AND
    bit_and = first_value & second_value
    print ("AND Operator : ", bit_and)

    #Bitwise OR
    bit_or = first_value | second_value
    print ("OR Operator : ", bit_or)

    #Bitwise NOT
    bit_not = ~first_value
    print ("NOT Operator : ", bit_not)

    #Bitwise XOR
    bit_xor = first_value ^ second_value
    print ("XOR Operator : ", bit_xor)

    #Less than
    less_than = first_value < second_value
    print ("Less Than : ", less_than)

    # Less than or equal to
    Less_than_or_equal = first_value <= second_value
    print ("Less Than Or Equal To : ", Less_than_or_equal)

    # Equal to
    Equal_to = first_value == second_value
    print ("Equal To : ", Equal_to)

    # Not equal to
    Not_equal_to = first_value != second_value
    print ("Not Equal To : ", Not_equal_to)

    # Greater than
    Greater_than = first_value > second_value
    print ("Greater Than : ", Greater_than)

    # Greater than or equal to
    Greater_than_or_equal = first_value >= second_value
    print ("Greater Than Or Equal To : ", Greater_than_or_equal)
except:
    print("Invalid Input")