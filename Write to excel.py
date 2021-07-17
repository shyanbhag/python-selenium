import openpyxl

path="E:\Software\Pyhton-Sel\EXCEL1.xlsx"

Workbook=openpyxl.load_workbook(path)
sheet=Workbook.active

for r in range(1,6):
    for c in range(1,4):
        sheet.cell(row=r,column=c).value="welcome"

    Workbook.save(path)