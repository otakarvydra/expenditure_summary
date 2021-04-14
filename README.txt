This is a description of the script expenditure_summary_script.py:

0. General
	-Use English language, do not use special czech characters!

1. CSV file formatting
	-The csv file must be named file.csv
	-There are different versions of .csv file extensions, if the parsing doesn't work it's likely because of this, 
	 always choose the simplest version. Sometimes the file is stored as CSV UTF-8 and this is wrong.
	-The file must have only two columns, these must be named column_1 and column_2.
	-No RESERVED transactions can be present, this would break down the program.
	-It is advised to skim the file quickly and look for unorthodox transactions, these might break the program. 


2. Engine (Extracting data)
	-This is the most difficult part of the program and might require further refinement because this engines was built
	 on empirical findings of the formatting.  
	-These are the following assumptions:
		-ATM withdrawals are all integers (whole numbers without a decimal place)
		-Bank transactions (salary, sending money to friends) to and from the account are all integers. 
		-Online payments (As well as online refunds of payments) and card payments at a shop all have the same format. 
		-Because of the nature of the formatting, if the entry in the second column starts with '00 CZK', then the transaction
		 is always a card transaction, and therefore is a withdrawal, shop transaction, online transaction or a card refund.
		-Because of the nature of the formatting, bank transactions never have '00 CZK' in the first entry of the second column.

	
		 

