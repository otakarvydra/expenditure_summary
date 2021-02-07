#Imports
import csv
import numpy as np

#Define empty lists
sellers = []
amounts = []

#Import the csv file and parse
column_1 = []
column_2 = []

with open('file.csv', newline='') as file_1:
    file_1_parsed = csv.DictReader(file_1)

    for line in file_1_parsed:
        column_1.append(line['column_1'])
        column_2.append(line['column_2'])

#Engine
for i in range(len(column_1)):
    string = column_2[i]
    string = string.strip(';')
    string_list = string.split(';')
    if string_list[0] == '00 CZK':
        string           = column_1[i]
        string_list      = string.split(';')
        amount           = int(string_list[1])
        if amount > 0:
            sellers.append('income')
            amounts.append(amount)
            continue
        seller           = string_list[9]
        transaction_list = string_list[13].split('(')
        transaction_type = transaction_list[0]
        transaction_date = transaction_list[1].strip(')')
    
    else:
        string           = column_2[i]
        string_list      = string.split(';')
        amount_1         = int(column_1[i].split(';')[1])
        if amount_1 > 0:
            try:
                amount = amount_1 + int(column_2[i].split(';')[0]) / 100
            except ValueError:
                amount = amount_1
            sellers.append('income')
            amounts.append(amount)
            continue
        amount = amount_1 - int(column_2[i].split(';')[0]) / 100
        seller           = string_list[8] 
        transaction_list = string_list[12].split('(')
        transaction_type = transaction_list[0]
        transaction_date = transaction_list[1].strip(')')

    if transaction_type == 'Výb?r z bankomatu':
        seller = 'bankomat'

    sellers.append(seller)
    amounts.append(amount)

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
