# 1 value error and tyoe eroor exception
print("Exception number 1 :", end="")
try: 
   x = int(input("enter: "))
except ValueError :
    print("ValueError") 

try:
    x = 4
    y = "hi"
    z = x + y
except TypeError:
    print ("Type Error")

# 2 ZeroDivisionError exception
print("Exception number 2 :", end="")
x = 5
y = 0
try:
    z = x / y
except ZeroDivisionError:
    print("Error: division by zero is not allowed.")

#3 IndexError exception
print("Exception number 3 :", end="")
y = [4,6,3,7]
try:
    print(y[8])
except IndexError:
    print("Error: Index out of range.")

#4 NameError exception
print("Exception number 4 :", end="")
y = [4,6,3,7]
try:
    print(z)
except NameError as e:
    print("Error: %s" %e)

#5 KeyError exception
print("Exception number 5 :", end="")
x = {1: "soham", 2: "raj", 3: "nick"}
try:   
    print(x[4])
except KeyError:
    print("Error: Key does not exist in the dictionary.")

#6 AttributeError exception
print("Exception number 6 :", end="")
try:
    class dog(object): 
        pass
    object = dog() 
    print (object.speak) 
except AttributeError:
    print ("Error: 'dog' object has no attribute 'speak'")

#7 GeneratorExit exception
print("Exception number 7 :")
def my_genrater():
    try:
        yield 1
        yield 2
        yield 3
    except GeneratorExit:
        print('Generator exited')
x = my_genrater()
print(next(x))
print(next(x))
del x

#8 User-defined exception with Zero Division Errorand value error
print("Exception number 8 :")
try:
    x = int(input("enter a number: "))
    if x == 0:
        raise ZeroDivisionError
except ZeroDivisionError:
    print("Error: input value is zero, try again")
except ValueError:
   print("invalid literal for int()") 

#9 User-defined exception
print("Exception number 9 :")
class MyError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return(self.value)
try:
    a = int(input("enter first number: "))
    b = int(input("enter second number: "))
    raise(MyError(a*b))
except MyError as error:
    print('Exception is: ', error.value)
except ValueError:
    print("invalid literal for int()")

#10 zero division error with else and finally
print("Exception number 10 :", end="")
x = 8
y = 6
try:
    z = x / y
except ZeroDivisionError:
    print("Error: division by zero is not allowed.")
else:
    print(z)
finally:
    print("This is Final Answer")