### Problem statement
Write a file which will take a json object containing the revenue and expense data of a company, and output its balance sheet month wise. The revenue and expense may be fixed or variable amounts payable in installments.

The program should output the answer/ balance sheet to the console. The balance for any month is the sum of all revenue for the month - sum of all expense for the month (`revenue.amount - expense.amount`). Sort the balancesheet in ascending order by timestamp.


#### Output
The program will calculate the balance sheet and display it in the terminal. The balance sheet will be sorted in ascending order by timestamp.

The output will be in the following format:
```
YYYY-MM : balance amount
YYYY-MM : balance amount
....
```
