import json

def calculate(input):
    with open(input) as file:       #opening the input file
        data = json.load(file)

    #extracting data from input file
    revenue = data["revenueData"]
    expenses = data["expenseData"]

    balance_sheet = {}

    for entry in revenue:
        startDate = entry.get("startDate")
        amount =  entry.get("amount",0)
        date = startDate[:7]          #taking only year-mpnth from startDate since the day and time remain constant

        #adding the revenue amount to balance sheet
        if date in balance_sheet:
            balance_sheet[date] += amount
        else:
            balance_sheet[date] = amount

    for entry in expenses:
        startDate = entry.get("startDate")
        amount =  entry.get("amount",0)
        date = startDate[:7]

        #deleting the expenses from balance sheet
        if date in balance_sheet:
            balance_sheet[date] -= amount
        else:
            balance_sheet[date] =  -amount
    
    #getting min_month, min_year and max_month, max_year.
    min_date = min(balance_sheet.keys())
    max_date = max(balance_sheet.keys())
    #print(f"{min_date} and {max_date}")

    min_year, min_month = map(int,min_date.split('-'))
    max_year, max_month = map(int,max_date.split('-'))

    #if a month is missing from both expensesData and revenueData, appending 0 in it.
    while min_year < max_year or (min_year == max_year and min_month <= max_month):
        current_month = f"{min_year}-{min_month:02}"    #string representation of year-month ('02' is to indicate month will have two digits)
        if current_month not in balance_sheet:  #appending 0 if the month is not present
            balance_sheet[current_month] = 0

        min_month += 1
        if min_month > 12:
            min_month = 1
            min_year += 1
        
    #sorting the items in balance sheet
    balance_sheet = sorted(balance_sheet.items())

    for date, balance in balance_sheet:
        print(f"{date} : {balance}")


calculate("1-input.json")
