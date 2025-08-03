
def divide(x,y):
    return x/y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def addition(x,y):
    return x+y
get_user_input=input('Enter your operation add/sub/div/mul :')
num1=int(input('Enter your num1:'))
num2=int(input('Enter your num2:'))

if get_user_input == 'add':
   print('Result :',addition(num1,num2))
elif get_user_input == 'subtract':
   print('Result :',subtract(num1,num2))
elif get_user_input == 'mul':
   print('Result :',multiply(num1,num2))
elif get_user_input == 'div':
    if num2 !=0:
        print('Result :',divide(num1,num2))
    else:
        print('Error cannot be divide by 0')
        
else:
    print('invalid operation')