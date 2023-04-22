import csv
import openpyxl

wb = openpyxl.Workbook()
ws = wb.active

with open("my_csv.csv", "r") as my_csv:
    reader = csv.reader(my_csv, delimiter=",")
    for row in reader:
        ws.append(row)

ws.delete_rows(4)
wb.save("my_excel.xlsx")
