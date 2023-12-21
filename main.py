from art import logo
import os
clear = lambda: os.system('cls')
 


def add(num1,num2):
    return num1+num2

def subtract(num1,num2):
    return num1-num2
    
def multiply(num1,num2):
    return num1*num2
    
def divide(num1,num2):
    return num1/num2
    
def start_calculator():   
    print(logo)
    first_num=float(input("What's the first number?: "))
    print("+\n-\n*\n/")
    result=0
    do_calc(first_num,result)
    
def perform_operation(operation,first_num,second_num):
    operations={"+":add,"-":subtract,"*":multiply,"/":divide}   
    if operation in operations:
        result=operations[operation](first_num,second_num)
        print(f"{first_num} {operation} {second_num} = {result}")
        return result
    else:
        print("Please pick an appropriate operation")
        return None
    
def do_calc(first_num,result):
    while True:
        operation=input("Pick an operation: ")
        second_num=float(input("What's the next number?: "))
        
        result=perform_operation(operation,first_num,second_num)
        if result is not None:
            while True:
               continue_calc=input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ").lower()
               if continue_calc in ["y","n"]:
                    break
               else:
                   print("Invalid input.Please enter 'y' or 'n'")
            if continue_calc=='y':
                first_num=result
                continue
            else:
                clear()
                break
    
    start_calculator()
        
start_calculator()      
    
    