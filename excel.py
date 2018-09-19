import openpyxl
import datetime

# load the workbook called 'example.xlsx'
wb = openpyxl.load_workbook('example.xlsx')

# define the sheet within the workbook
sheet = wb.get_sheet_by_name('Sheet1')

# define the cell within the sheet
sheet['C2']

# define the cell as a value
sheet['C2'].value

# print the content of the cell 'C2'
print (sheet['C2'].value)

# define 'c'
c = sheet['B2']

# get the value of 'c'
c.value

# print the value of 'c'
print(c.value)