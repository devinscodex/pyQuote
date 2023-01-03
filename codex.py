# MEG quote processor - helper functions
# devin dwight
import pandas as pd

quote_path = 'c:/bin/quotes'

# functions
def print_dataframe(filepath, print_all_rows = False):
    print(f'\nConverting "{filepath}" into a dataframe...\n')
    df = pd.read_excel(filepath)
    if print_all_rows: pd.set_option('display.max_rows', None)
    print(df)


def get_file_selection(files):
    #valid_input = False
    invalid_input = 'Invalid selection, please select from the provided options:'
    while True:
        # print selections & collect input
        print(f'\nFiles in "{quote_path}":')
        for i, file in enumerate(files):
            print(f'{i + 1}: {file}')
        print('0: Exit')
        user_input = input("Please select one: ")    
        user_input = int(user_input)

        # validate input
        if user_input == 0:
            terminate_program()
        if 1 <= user_input <= len(files):
            selected_file = quote_path + '/' + files[user_input - 1]
            return selected_file
            #print(f'\nSelected: {selected_file}')
            #valid_input = False
        else:
            print(invalid_input)


def user_end_program():
    user_input = input(f'\nAny key to continue or "0" to exit...')
    if user_input == "0":
        return True
    else:
        return False


def terminate_program():
    print('\nGoodbye.\n')
    quit()