a=6#sum of number
b=7
c= a+b
print(c)
a=34 #To find the average of 2 numbers
b=5
print('Remainder when a is divided by b is: ',a%b)
a= input('Enter the value of a :') # To find the data type by input
c= type(a)
print(c)
a= int(input("Enter your number 1:")) #To find the greater number by inputy
b= int(input("Enter your number 2:"))
print('A is greater than b ',a>b)
a= int(input("Enter your number 1:"))  #To find the average of 2 numbers
c= int(input("Enter your number 1:"))
d= (a+c)/2
print("The average of a and c is :",d)
a= int(input('Enter your number :'))   #To find cube of number
print('The square of your number is :', a**3)
name=['zarafahad']
nameshort= name[0:2]
print(nameshort)
#'''Even Numbers from List
#Given a list of numbers, extract and print only the even numbers.
list= [1,2,3,4,5]
even_numbers=[]
if (list[0]%2)==0:
    even_numbers.append(list[0])
elif (list[1]%2)==0:
    even_numbers.append(list[1])
elif (list[2]%2)==0:
    even_numbers.append(list[2])
elif (list[3]%2)==0:
    even_numbers.append(list[3])
elif (list[4]%2)==0:
    even_numbers.append(list[4])
print('Even numbers in list:',even_numbers)