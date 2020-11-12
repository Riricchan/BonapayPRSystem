from os import listdir

def fix_text_format(user):
    return user.lower().replace(" ", "_").replace(".", "_")

def print_lines():
    print("-" * 50)

def print_dir_contents(folder):
    dir_list = listdir(folder)
    print(dir_list)
    print_lines()

def print_message(msg):
    print(msg)
    print_lines()

def error_message():
    print("Invalid input! Returning to main menu...")
    print_lines()