# x = input("enter a value for x :")
# y = input("enter a value for y :")
# try:
#     z = int(x)/int(y)
# except Exception as e:    # General way  - for specific except ZeroDivisionError as e:
#     print(f'exception occured: {e}')     #          - print("Division by zero exception")
#     z = None
# print(f'Division is : {z}')

#------------------------------------------------------------

# try:
#     z = x/int(y)        # If forget to convert it into integer
# except ZeroDivisionError as e:
#     print(f'Division by zero exception')
#     z = None
# except Exception as e:
#     print(f'Error type is : {type(e).__name__}')    # by the help of this we know the type of error
#     z = None                                        # so that we can then handle it specifically as handle zerobydivison
# print(f'Division is : {z}')


#------------------After knowing type of error handling specifically------------------------------
# try:
#     z = x/int(y)
# except ZeroDivisionError as e:
#     print(f'Division by zero exception')
#     z = None
# except TypeError as e:
#     print(f'Type error exception')
#     z = None
# print(f'Division is : {z}')

#-----------🎯 Challenge--------------
#-------------- Read numbers from a file and handle errors gracefully--------------

with open("./Day_07/MyData", "r") as f:
    text = f.read()
    word = text.split()
    number = []
    for w in word:
        try:
            n = float(w)
            number.append(n)
        except ValueError as e:
            # print(f'Value Error exception')
            continue



print(number)
