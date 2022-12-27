# MEG quote processor
# devin dwight
# 2022-11-17
import os
import pandas as pd

#pd.options.display.max_rows = None # toggle this line to display all rows or not

# prerequisites (create path & load files to list for processing)
folder_path = "c:/bin/quotes"
quotes = []

if not os.path.exists(folder_path):
    print(folder_path + " does not exist...creating now...")
    os.makedirs(folder_path, exist_ok=True)

# variables
contents = os.listdir(folder_path)


# loop through quote folder, add Excel files to list
for file in os.listdir(folder_path):
    if file.__contains__(".xls"):
        quotes.append(file)

# for obj in contents:
#     if os.path.isfile(obj):
#         print("file found....")    
#     if obj.__contains__(".xl"):
#         quotes.append(obj) # add full path to quotes list
#         #quotes.append(os.path.abspath(obj)) # add full path to quotes list <- this adds \\ in path...

print(quotes)

#df = pd.read_excel("c:/bin/quotes/sheet.xlsx", header=None)
#print(df)

""" if len(quotes) > 0:
    wb = load_workbook("c:/bin/quotes/sheet.xlsx")
    sheet = wb.active
    for row in sheet["A1:C72"]:
        if [x.value for x in row] == "x":
            print([x.value for x in row]) """



""" if len(quotes) > 0:
    print("Quotes found:")
    for q in quotes:
        print(q + "\n")
else:
    print("No files found...") """