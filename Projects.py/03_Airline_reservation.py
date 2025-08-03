
price = 0
actual_price=0
total_price=0
pass_amt = int(input('how many passengers are going with you?'))
for i in range (pass_amt):
    name = input("enter your name?")
    age = int(input("enter your age?"))
    destination = input("enter your destination?")  # add a line for easy readibility
    if destination == 'lahore' :
       price = 10000
    elif destination == 'dubai' :
       price =70000
    elif destination == 'karachi' :
       price = 50000
    print('price:',price)
    if age <= 5 :
       discount = 0.5* price
       actual_price= price - discount
       print('actual_price:', actual_price)
    if age <= 5 :
       discount = 0.9* price
       actual_price= price - discount
       print('actual_price:', actual_price)
       
    if age <= 15 and age >15 :
       discount = 0.8* price
       actual_price= price - discount
       print('actual_price:', actual_price)  
    if age >60 :
       discount = 0.4* price
       actual_price= price - discount
       print('actual_price:', actual_price)
       total_price= total_price+actual_price
       print('total_price:',total_price)
       
