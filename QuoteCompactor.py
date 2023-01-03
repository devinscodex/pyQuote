# MEG quote processor
# devin dwight
# 2022-11-17

# python solution for toggling the "hidden" state of rows of Excel files
# inteded for our company's sales team, but may be extended for further uses
# dependencies [pandas, windows-curses]
import os
import codex

# program vars
quote_path = 'c:/bin/quotes'
print_all_rows = False

# main program loop
while True:
    files = []
    selected_file = ''

    print(f'\npyQuote is scanning "{quote_path}" for Excel files...')
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

    # one file
    if len(files) == 1:
        selected_file = files[0]
        selected_file = quote_path + '/' + selected_file
        print(f'Only 1 file found in {quote_path}, processing {selected_file}...')

    # multiple files
    if len(files) > 1:
        selected_file = codex.get_file_selection(files)

    codex.print_dataframe(selected_file, print_all_rows)

    # continue program?
    if codex.user_end_program(): break 

# loop is broken, end program
codex.terminate_program()