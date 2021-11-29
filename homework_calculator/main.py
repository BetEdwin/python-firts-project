
print("basic calculator-----(+)(-)(*)(/)---- ")
num=float(input("enter a number1"))
num1=float(input("enter a number2"))
operation=float(input("what operation do you want to perform\n1- addition\n2- subtraction\n3- -multiplication\n4- division\n--- and write the term that accompanies the math operation\n"))
#\n is
if operation == 1:
    print("result")
    print(float(num+num1))

elif operation == 2:
    print("result")
    print(float(num-num1))

elif operation == 3:
    print("result")
    print(float(num * num1))

elif operation !=0:
    print("result is ")
    print(float(num/num1))
else:
    print("the operation is not possible")











