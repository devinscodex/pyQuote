# MEG quote processor
# devin dwight
# started: 2022-11-17
# ended: 
import os
import pandas as pd
#pd.options.display.max_rows = None # toggle this line to display all rows or not

# main program loop
while True:
    # prerequisites & variables (validate/create path > add files to list for processing)
    folder_path = 'c:/bin/quotes'
    files = []
    if not os.path.exists(folder_path):
        print(f'\n{folder_path} does not exist...creating now...')
        os.makedirs(folder_path, exist_ok=True)

    # loop thru folder, add Excel files to list
    for file in os.listdir(folder_path):
        if file.__contains__('.xls'):
            files.append(file)

    # no files...
    if len(files) == 0:
        print(f'There are no Excel files in "{folder_path}", please add at least one to continue...')
        quit()

    # only one file
    if len(files) == 1:
        selected_file = files[0]
        selected_file = folder_path + '/' + selected_file
        print(f'\nOnly 1 file found in {folder_path}, processing {selected_file}...')

    # multiple files
    if len(files) > 1:
        selection_made = False
        invalid_input = 'Invalid selection, please select from the provided options:'
        while not selection_made:
            # print selections and collect input
            print(f'\nFiles in "{folder_path}":')
            print('0: Exit program...')
            for i, file in enumerate(files):
                print(f'{i + 1}: {file}')
            input = input("Please select one: ")    
            input = int(input)

            # validate input
            if input == 0:
                print('Have a nice day!')
                quit()
            if 1 <= input <= len(files):
                selected_file = folder_path + '/' + files[input - 1]
                print(f'\nSelected: {selected_file}')
                selection_made = True
            else:
                print(invalid_input)


    # process selected file
    df = pd.read_excel(selected_file)
    print(df)



print('\nend of program...\n')