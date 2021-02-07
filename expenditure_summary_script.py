#Imports

import csv

#Define empty categories for summing expenditure
food      = 0
fuel      = 0
household = 0
parking   = 0
education = 0
apps      = 0
hygiene   = 0
tea       = 0
social    = 0
tools     = 0
car       = 0
bike      = 0

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
        amount           = int(string_list[1].strip('-'))
        seller           = string_list[9]
        transaction_list = string_list[13].split('(')
        transaction_type = transaction_list[0]
        transaction_date = transaction_list[1].strip(')')
    
    else:
        string           = column_2[i]
        string_list      = string.split(';')
        amount           = int(column_1[i].split(';')[1].strip('-')) + int(string_list[0].strip('0')) / 100
        seller           = string_list[8] 
        transaction_list = string_list[12].split('(')
        transaction_type = transaction_list[0]
        transaction_date = transaction_list[1].strip(')')




