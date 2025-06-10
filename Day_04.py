# #Control Structure
# av = 5
# x = int(input("How many condies do you want ?"))
#
# i = 1
# while  i<=x:
#     if i > av:
#         print("Out of stocks")
#         break          # It will help to come out from the loop if i > av
#     print("Candy")
#     i += 1
#
# print("Bye")
#----------------------------------------------------------------------------------
# for i in range(1, 21):
#     if i%2 ==0 or i%3==0:   #if i%2 ==0 and i%3==0
#         continue        # It will help to just skip these number not jup out from the loop
#     else:
#         print(i)
#
# print("Bye")
#------------------------------------------------------------------------------------
# for i in range(1, 21):
#     if i%2==0:
#         pass               # It will just do nothing for this case just like continue
#     else:
#         print(i)

#---------------🎯 Challenge----------------------
#-------------- Check if a user-entered number is prime-------------------

num = int(input("Please enter the number to check prime or not."))
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):  # check up to sqrt(n)
        if n % i == 0:
            return False
    return True

if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")
