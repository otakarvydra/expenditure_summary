This is a description of the script expenditure_summary_script.py:

0. General
	-Use English language, do not use special czech characters!


1. CSV file formatting
	-The csv file must be named file.csv
	-There are different versions of .csv file extensions, if the parsing doesn't work it's likely because of this, 
	 always choose the simplest version. Sometimes the file is stored as CSV UTF-8 and this is wrong.
	-The file must have only two columns, these must be named column_1 and column_2.
	-It is advised to skim the file quickly and look for unorthodox transactions, these might break the program. 


2. Engine (Extracting data)
	-This is the most difficult part of the program and might require further refinement because this engine was built
	 on empirical findings of the formatting.  
	-These are the following assumptions:
		-ATM withdrawals are all integers (whole numbers without a decimal place)
		-Bank transactions (salary, sending money to friends) to and from the account are all integers. 
		-Online payments (As well as online refunds of payments) and card payments at a shop all have the same format. 
		-Because of the nature of the formatting, if the entry in the second column starts with '00 CZK', then the transaction
		 is always a card transaction, and therefore is a withdrawal, shop transaction, online transaction or a card refund.
		-Because of the nature of the formatting, bank transactions never have '00 CZK' in the first entry of the second column.
	-Principle of Operation:
		-The engine first decides via an if function if the first cell of the second column starts with '00 CZK'. If that is the case, then it simply assumes 
		that this expenditure was a card transcation and works with that. There are checks included. One checks whether or not the transaction is reserved and the
		other one prompts the user to manually input the seller, amount, date and the transaction type if something goes wrong (The formatting is different). 
		-If the first cell of the second column is not 00 CZK, then it is either a float card transaction or a bank transfer. The program first checks for known bank
		transfers (salary, katerina, rent) with if functions, if all of these if functions are false, then it proceeds categorising as if the transaction is a card transcation. 
		If that also fails, then the user is also prompted as before to input the important info manually. The check against reserved transaction is also included. 
		-An option to break the engine loop is included. This is there because the program might categorise all the transactions and then it attempts to categorise
		empty excel lines. 


3. Examining Sellers
	-After the engine is complete, the spent transactions at every indiviual seller are printed to the terminal. The user is asked whether or not to inspect a given seler.
	If the user decides to inspect a seller, then all the transactions via this seller get printed. 


4. Assigning categories to new Sellers:
	-If a new seller is encountered, then the program asks the user to categorise this seller. The specific category is then saved in a separate file called categories.csv
	-From this file, the categories are then imported to the program the next time it runs. 


5. Creating a new Category:
	-The user is then asked to manually create a new category. This is useful if I receive money in cash and I decide not to put that money in my account.


6. 1st Data output:
	-The sorted categories get printed out as well as total expenditure and total income. 


7. Splitting Categories:
	-The user is asked to split a category. This is useful if for example at Lidl, the user bought something that is from the household category like cleaning things or whatever. 
	After this whether or not any category is splitted, the expenditure sorted by the categories is printed out. The program waits until the user presses enter which terminates 
	the program. 


	
		 

