# MEG quote processor
# devin dwight
# 2022-11-17
import os
import pandas as pd

#pd.options.display.max_rows = None # toggle this line to display all rows or not

# prerequisites & variables (validate/create path > add files to list for processing)
folder_path = "c:/bin/quotes"
files = []

if not os.path.exists(folder_path):
    print(folder_path + " does not exist...creating now...")
    os.makedirs(folder_path, exist_ok=True)


# loop folder, add Excel files to list, user selects file to read into Pandas
for file in os.listdir(folder_path):
    if file.__contains__(".xls"):
        files.append(file)

#print(quotes)

print('Please select a file:')
for i, file in enumerate(files):
    print(f'{i + 1}: {file}')

selection_made = False

invalid_input = "Invalid selection, please select from the provide options:"

while not selection_made:
    selection = input('Enter a number: ')
    try:
        selection = int(selection)
        # validate selection
        if 1 <= selection <= len(files):
            selected_file = os.path.abspath(files[selection - 1])
            print(os.path.abspath(selected_file)
            #df = pd.read_excel(selected_file)
            selection_made = True
        else:
            print(invalid_input)
    except ValueError:
        print(invalid_input)
    #except FileNotFoundError:
    #selected_file = selected_file.replace('\\','/')

#print(df)
















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