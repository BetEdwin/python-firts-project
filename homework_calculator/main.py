
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

def print_welcome_message():
    print("basic calculator-----(+)(-)(*)(/)---- ")

def menu_options():
    print("what operation do you want to perform\n1. addition\n2. subtraction\n3. multiplication\n4. division\n")

def request_user_option():
    print("write the term that accompanies the math operation")
    return int(input())

def operation_add(num, num1):
    print("result  " + str(num + num1))

def operation_sub(num,num1):
    print("result  " + str(num - num1))

def operation_mul(num, num1):
    print("result  " + str(num * num1))

def operation_div(num, num1):
    print("result  " + str(num / num1))

print_welcome_message()
menu_options()
options=request_user_option()

num = float(input("enter a number1"))
num1 = float(input("enter a number2"))

if options == 1:
    operation_add(num, num1)

elif options == 2:
    operation_sub(num, num1)

elif options == 3:
    operation_mul(num, num1)

elif options == 4:
    if num1 == 0:
        print("cannot be divided by 0")
    else:
        operation_div(num, num1)
else:
    print("---end---")









