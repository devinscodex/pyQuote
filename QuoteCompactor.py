# MEG quote processor
# devin dwight
# started: 2022-11-17
# ended: 
import os
import pandas as pd

# global vars
quote_path = 'c:/bin/quotes'
program_loop = True


# functions
def get_file_selection(files):
    #valid_input = False
    invalid_input = 'Invalid selection, please select from the provided options:'
    while True:
        # print selections & collect input
        print(f'\nFiles in "{quote_path}":')
        for i, file in enumerate(files):
            print(f'{i + 1}: {file}')
        print('0: Go Back')
        input = input("Please select one: ")    
        input = int(input)

        # validate input
        if input == 0:
            return
        if 1 <= input <= len(files):
            selected_file = quote_path + '/' + files[input - 1]
            return selected_file
            #print(f'\nSelected: {selected_file}')
            #valid_input = False
        else:
            print(invalid_input)


def end_program():
    input = input(f'\nAny key to continue or "0" to exit...')
    return input == 0


# main program
while program_loop:
    selected_file = ''
    print(f'\npyQuote init...scanning "{quote_path}" for Excel files...')
    # prerequisites & variables (validate/create path > add files to list for processing)
    files = []
    if not os.path.exists(quote_path):
        print(f'{quote_path} does not exist...creating now...')
        os.makedirs(quote_path, exist_ok=True)

    # loop thru folder, add Excel files to list
    for file in os.listdir(quote_path):
        if file.__contains__('.xls'):
            files.append(file)

    # no files...
    if len(files) == 0:
        print(f'\nThere are no Excel files in "{quote_path}", please add at least one to continue...\n')
        continue

    # only one file
    if len(files) == 1:
        selected_file = files[0]
        selected_file = quote_path + '/' + selected_file
        print(f'\nOnly 1 file found in {quote_path}, processing {selected_file}...')

    # multiple files
    if len(files) > 1:
        selected_file = get_file_selection(files)
        if not selected_file: continue # if empty, next iteration

    # process selected file
    print(f'Attempting to convert "{selected_file}" into a dataframe...\n')
    df = pd.read_excel(selected_file)
    print(df)

    # continue program?
    if end_program(): 
        break 

print('\nend of program...\n')
