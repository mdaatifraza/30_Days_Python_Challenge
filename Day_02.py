# Variable
from traceback import print_tb
from xml.dom.minidom import ProcessingInstruction

Rent = 7300
Light_bill = 500
groceries = 1000

print(Rent)

total = Rent+Light_bill+groceries
print(total)

Rent = 8000  #We can change the variable values

# Storing the string in variable
item1 = "Rent"
item2 = "Light_bill"
item3 = "groceries"

print(f'Expenses items are {item1}, {item2} and {item3}')

# Data Type
# Integer, Float, String, Boolean
age = 23
print("you are " + str(age) +" year old")
print("you are", str(age) ,"year old")  # this will add the space automatically
print(f"you are {age} year old")



#-------Challenge -> Calculate the area of a rectangle using user-input length and width-------
try:
    l = float(input("please enter the length : "))
    b = float(input("please enter the breath : "))
    ar_of_rec = l*b
    print(f'Area of the rectangle =  {ar_of_rec}')
except:
    print(f'❌ Invalid input. (please enter integer or float)')