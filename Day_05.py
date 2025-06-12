# Functions

# # without function-----
# Aatif_exp_list = [2100, 1400, 1500]
# Raza_exp_list = [4100, 1500, 1600]
# total = 0
# for item in Aatif_exp_list:
#     total = total + item
# print(f'Aatif total expense is : {total}')
#
# total = 0
# for item in Raza_exp_list:
#     total = total + item
# print(f'Raza total expense is : {total}')
#--------Using a function----------------

# def calculate_total(exp):
#     total = 0
#     for item in exp:
#         total = total+item
#     return  total
#
#
# Aatif_exp_list = [2100, 1400, 1500]
# Raza_exp_list = [4100, 1500, 1600]
#
# Aatif_total = calculate_total(Aatif_exp_list)
# print(f'The total expenses of Aatif : {Aatif_total}')
#
# Raza_total = calculate_total(Raza_exp_list)
# print(f'The total expenses of Raza : {Raza_total}')

#------------🎯 Challenge----------------
#- Write a function that computes the sum and average of a list of numbers

def sum(exp):
    total = 0
    for item in exp:
        total = total + item
    return  total

marks = [84, 56, 77, 83, 89]
total_marks = sum(marks)
avg = total_marks/len(marks)
print(f'Total marks obtains out of 500 / {total_marks}')
print(f'Average marks : {avg}')