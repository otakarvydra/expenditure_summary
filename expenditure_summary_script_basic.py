#Imports
import csv
import numpy as np
from matplotlib import pyplot as plt

#User greeting
print('Below is the list of sellers you interacted with this month and the corresponding amount you spent/gained')

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
            tran_type = string_list_1[13].split('(')[0]     

            if tran_type == 'Výb?r z bankomatu':
                seller = 'ATM withdrawal'

            sellers.append(seller)
            amounts.append(amount)
            dates.append(date)
            tran_types.append(tran_type)
            continue

        except:
            print('Unknown transaction, see details below:')
            print(string_list_1)
            print(string_list_2)
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
                tran_type = 'bank transfer'

                sellers.append(seller)
                amounts.append(amount)
                dates.append(date)
                tran_types.append(tran_type)
                continue

            if string_list_2[0] == ' a.s.' and string_list_2[3] == 'Správa domu':
                seller    = 'Správa domu'
                date      = string_list_1[3]
                tran_type = 'bank transfer'

                sellers.append(seller)
                amounts.append(amount)
                dates.append(date)
                tran_types.append(tran_type)
                continue
            
            try:
                if string_list_1[9] == 'Kate?ina Coufalová':
                    seller    = 'Kateřina Coufalová'
                    date      = string_list_1[3]
                    tran_type = 'bank transfer'

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
                    tran_type = string_list_2[12].split('(')[0]
                
                    sellers.append(seller)
                    amounts.append(amount)
                    dates.append(date)
                    tran_types.append(tran_type)
                    continue

                if amount > 0:
                    amount    = amount + (int(string_list_2[0] / 100))
                    seller    = string_list_2[8]
                    date      = string_list_2[12].split('(')[1].strip(')')
                    tran_type = string_list_2[12].split('(')[0]

                    sellers.append(seller)
                    amounts.append(amount)
                    dates.append(date)
                    tran_types.append(tran_type)
                    continue
       
        except:
            print('Unknown transaction, see details below:')
            print(string_list_1)
            print(string_list_2)
            amount    = int(input('Enter amount as an integer or a float '))
            seller    = input('Enter seller ')
            date      = input('Enter a date in the following format: day.month.year (Always use 2 - digit number for the day and month, year is 4 dig. number, 3 is entered as 03) ')
            tran_type = input('Enter transaction type, will probably be a bank transfer ')
                
#Data output
sellers_unique = np.unique(sellers)

sellers_f = []
amounts_f = []

for seller_u in sellers_unique:
    sum_1 = 0
    for i in range(len(sellers)):
        if sellers[i] == seller_u:
            sum_1 += amounts[i]
    print('{sum_1} via {seller_u}'.format(sum_1 = sum_1, seller_u = seller_u))
    sellers_f.append(seller_u)
    amounts_f.append(sum_1)

#Final dict creation
final_dict = {key : value for key, value in zip(sellers_f, amounts_f)}

#Inspectig individual seller

user_input = input('Do you wish to inspect any individual seller? yes/no ')

while user_input == 'yes':
    seller_inspect = input('Name the seller to be inspected ')
    for i in range(len(sellers)):
        if sellers[i] == seller_inspect:
            print('At {date} the sum of {amount} was spent/gained via {seller}'.format(date = dates[i], amount = amounts[i], seller = sellers[i]))

    user_input = input('Do you with to inspect any other individual seller? yes/no ')
