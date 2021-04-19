#Imports
import csv
import numpy as np
from matplotlib import pyplot as plt

#User greeting
print('''Expenditure summary running
                                ''')

#Selecting a month
month_input = input('Select month as a number with two places (february = 02) ')

#Import the csv file and parse
column_1 = []
column_2 = []

with open('file.csv', newline='') as file_1:
    file_1_parsed = csv.DictReader(file_1)

    for line in file_1_parsed:
        column_1.append(line['column_1'])
        column_2.append(line['column_2'])

#Define empty lists
sellers    = []
amounts    = []
dates      = []
tran_types = []

#Engine
for i in range(len(column_1)):
   
    #Adjust and split the strings to be further processed 
    string_1 = column_1[i]
    string_2 = column_2[i]
    string_1_stripped = string_1.strip(';')
    string_2_stripped = string_2.strip(';')
    string_list_1 = string_1_stripped.split(';')
    string_list_2 = string_2_stripped.split(';')

    if string_list_2[0] == '00 CZK':
        amount = int(string_list_1[1])
        try:
            seller    = string_list_1[9]
            date      = string_list_1[13].split('(')[1].strip(')')
            month     = date.split('.')[1]
            tran_type = string_list_1[13].split('(')[0]     

            if tran_type == 'Výb?r z bankomatu':
                seller = 'ATM withdrawal'

            if month == month_input:
                sellers.append(seller)
                amounts.append(amount)
                dates.append(date)
                tran_types.append(tran_type)
            
            continue

        except:
            if 'RESERVED' in string_1.split(';') or 'RESERVED' in string_2.split(';'):
                continue
            print('Unknown transaction, see details below:')
            print(string_list_1)
            print(string_list_2)
            break_value = input('Do you wish to break the loop and proceed with the program? yes/no')
            if break_value == 'yes':
                break
            amount    = input('Enter amount as an integer or a float ')
            seller    = input('Enter seller as a string ')
            date      = input('Enter a date as a string in the following format: day.month.year (Always use 2 - digit number, 3 is entered as 03) ')
            tran_type = input('Enter transaction type as a string, will probably be a bank transfer ')

    else:
        try:
            amount = int(string_list_1[1])
            if string_list_2[0] == ' SPOL. S R.O.' and string_list_1[9] == 'AREKO':
                seller    = 'AREKO'
                date      = string_list_1[3]
                month     = date.split('-')[1]
                tran_type = 'bank transfer'

                if month == month_input:
                    sellers.append(seller)
                    amounts.append(amount)
                    dates.append(date)
                    tran_types.append(tran_type)
                continue

            if string_list_2[0] == ' a.s.' and string_list_2[3] == 'Správa domu':
                seller    = 'Správa domu'
                date      = string_list_1[3]
                month     = date.split('-')[1]
                tran_type = 'bank transfer'

                if month == month_input:
                    sellers.append(seller)
                    amounts.append(amount)
                    dates.append(date)
                    tran_types.append(tran_type)
                continue
            
            try:
                if string_list_1[9] == 'Kate?ina Coufalová':
                    seller    = 'katerina'
                    date      = string_list_1[3]
                    month     = date.split('-')[1]
                    tran_type = 'bank transfer'

                    if month == month_input:
                        sellers.append(seller)
                        amounts.append(amount)
                        dates.append(date)
                        tran_types.append(tran_types)
                    continue

            except:
                if amount < 0:           
                    amount    = amount - (int(string_list_2[0]) / 100)
                    seller    =  string_list_2[8]
                    date      = string_list_2[12].split('(')[1].strip(')')
                    month     = date.split('.')[1]
                    tran_type = string_list_2[12].split('(')[0]
                
                    if month == month_input:
                        sellers.append(seller)
                        amounts.append(amount)
                        dates.append(date)
                        tran_types.append(tran_type)
                    continue

                if amount > 0:
                    amount    = amount + (int(string_list_2[0] / 100))
                    seller    = string_list_2[8]
                    date      = string_list_2[12].split('(')[1].strip(')')
                    month     = date.split('.')[1]
                    tran_type = string_list_2[12].split('(')[0]

                    if month == month_input:
                        sellers.append(seller)
                        amounts.append(amount)
                        dates.append(date)
                        tran_types.append(tran_type)
                    continue
       
        except:
            if 'RESERVED' in string_1.split(';') or 'RESERVED' in string_2.split(';'):
                continue
            print('Unknown transaction, see details below:')
            print(string_list_1)
            print(string_list_2)
            break_value = input('Do you wish to break the loop and proceed with the program? yes/no')
            if break_value == 'yes':
                break
            amount    = int(input('Enter amount as an integer or a float '))
            seller    = input('Enter seller')
            date      = input('Enter a date in the following format: day.month.year (Always use 2 - digit number for the day and month, year is 4 dig. number, 3 is entered as 03) ')
            tran_type = input('Enter transaction type, will probably be a bank transfer ')
                
#Data output
print('''
This is the list of transactions in the desired period:
                                                            ''')
sellers_unique = np.unique(sellers)

sellers_f = []
amounts_f = []

for seller_u in sellers_unique:
    sum_1 = 0
    for i in range(len(sellers)):
        if sellers[i] == seller_u:
            sum_1 += amounts[i]
    print('     {sum_1} via {seller_u}'.format(sum_1 = sum_1, seller_u = seller_u))
    sellers_f.append(seller_u)
    amounts_f.append(sum_1)

#Final dict creation
final_dict = {key : value for key, value in zip(sellers_f, amounts_f)}

#Inspecting individual seller
user_input = input('''
Do you wish to inspect any individual seller? yes/no ''')

while user_input == 'yes':
    seller_inspect = input('Name the seller to be inspected ')
    for i in range(len(sellers)):
        if sellers[i] == seller_inspect:
            print('At {date} the sum of {amount} was spent/gained via {seller}'.format(date = dates[i], amount = amounts[i], seller = sellers[i]))

    user_input = input('Do you with to inspect any other individual seller? yes/no ')

#Opening file with existing categories and saving these into sellers_c and categories_c
sellers_c    = []
categories_c = []

with open('categories.csv', newline = '') as categories_file:
    categories_file_parsed = csv.DictReader(categories_file)

    for line in categories_file_parsed:
        sellers_c.append(line['seller'])
        categories_c.append(line['category'])

#Looping through the sellers we have this month and checking if they are categorised in categories_c. If not, then the user is asked to provide a category for them 
#and the new sellers with their categories are saved in sellers_n and categories_n.
sellers_n    = []
categories_n = []

for i in sellers_f:
    if not i in sellers_c:
        category = input('Seller {seller} not categorized, please enter a category  '.format(seller = i))
        sellers_n.append(i)
        categories_n.append(category)

#Writing the new sellers to categories.csv 
log = []
for i in range(len(sellers_n)):
    log.append({'seller': sellers_n[i], 'category': categories_n[i]})
    
with open('categories.csv', 'a') as file_1:
    fields = ['seller', 'category']
    file_1_instance = csv.DictWriter(file_1, fieldnames=fields)
    for line in log:
        file_1_instance.writerow(line)

#Import the updated sellers with their categories into sellers_all and categories_all
sellers_all    = []
categories_all = []

with open('categories.csv', newline = '') as file_1:
    file_1_parsed = csv.DictReader(file_1)

    for line in file_1_parsed:
        sellers_all.append(line['seller'])
        categories_all.append(line['category'])

#Categorising Expenditures
lst = []
for i in range(len(sellers_f)):
    for j in range(len(sellers_all)):
        if sellers_f[i] == sellers_all[j]:
            lst.append(categories_all[j])


lst   = np.unique(lst)
zeros = [0 for i in lst]
dict_1 = {key: value for key, value in zip(lst, zeros)}              

for i in range(len(sellers_f)):
    for j in range(len(sellers_all)):
        if sellers_f[i] == sellers_all[j]:
            cat = categories_all[j]
            dict_1[cat] += amounts_f[i]

#Manually creating a new category (will be mainly used for gifts or cash income)
user_input = input('''
Do you wish to create a new category? yes/no ''')

while user_input == 'yes':
    cat_input         = input('Name the category you wish to create ')
    amount_input      = float(input('State the desired amount this category will contain '))
    dict_1[cat_input] = amount_input
    user_input        = input('Do you wish to create a new category? yes/no ')

print('''
Expenditure sorted via categories:
                              ''')
for key, value in dict_1.items():
    print('     ' + str(key) + ' ' + str(value))

#Showing total expenditure and savings

income_tot      = 0
expenditure_tot = 0
for i in amounts_f:
    if i > 0:
        income_tot += i
    else:
        expenditure_tot += i

print('''
Totals:
    ''')

print('     Total expenditure: {amount}'.format(amount = expenditure_tot))
print('     Total income: {amount}'.format(amount = income_tot))
print('     Balance: {balance}'.format(balance = (income_tot + expenditure_tot)))

#Splitting Categories

user_input = input('''
Do you wish to split any category into multiple categories? yes/no ''')

while user_input == 'yes':
    cat_input           = input('''Name the category you wish to split ''')
    where_input         = input('''Name the category where the money will be transferred ''')
    amount_input        = float(input('State the amount to be transferred '))
    dict_1[cat_input]   = dict_1[cat_input] - amount_input
    dict_1[where_input] = dict_1[where_input] + amount_input

    user_input = input('Do you wish to split any further category into multiple categories? yes/no ')

# Printing the updated expenditure

print('''
Expenditure sorted via categories
                             ''') 

for key, value in dict_1.items():
    print('     ' + str(key) + ' ' + str(value))

#Creating Graphs
expenditures_values     = [] 
expenditures_categories = []
incomes_values          = []
incomes_categories      = []

for key, value in dict_1.items():
    if value < 0:
        expenditures_values.append(value)
        expenditures_categories.append(key)
    else:
        incomes_values.append(value)
        incomes_categories.append(key)

    #Creating pie graphs
plt.figure('Pie Graphs')

plt.subplot(2,1,1)
plt.pie([abs(i) for i in expenditures_values], labels = expenditures_categories)
plt.axis('equal')
plt.title('Expenditures')

plt.subplot(2,1,2)
plt.pie([abs(i) for i in incomes_values], labels = incomes_categories)
plt.axis('equal')
plt.title('Incomes')

plt.show()

#Simple prompt included to keep the terminal open and to make the program look professional.

ans = input('''
Press enter to exit ''')