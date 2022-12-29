# MEG quote processor
# devin dwight
# started: 2022-11-17
import os
import pandas as pd
import codex

# program vars
quote_path = 'c:/bin/quotes'
program_loop = True


# main program
while program_loop:
    selected_file = ''
    print(f'\npyQuote: scanning "{quote_path}" for Excel files...')
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
        print(f'Only 1 file found in {quote_path}, processing {selected_file}...')

    # multiple files
    if len(files) > 1:
        selected_file = codex.get_file_selection(files)
        if not selected_file: continue # if empty, next iteration

    # process selected file
    print(f'Attempting to convert "{selected_file}" into a dataframe...\n')
    df = pd.read_excel(selected_file)
    print(df)

    # continue program?
    if codex.user_end_program(): break 


codex.terminate_program()