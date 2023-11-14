from openpyxl import load_workbook
file_name = "student.xls"
exel = load_workbook(file_name)
list_1 = exel["list1"]
list_1 ["A2"] = "Aichu"
list_1 ["B2"] = 77
list_1 ["A2"] = "Aich"
list_1 ["B2"] = 79
exel.save(file_name)