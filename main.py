import os
import shutil
import sys
import errno
from computation import *
from printfunc import *
from os import mkdir, rmdir
from os.path import exists as fileExists

#   DIRECTORIES
COMPANY_DATA_FOLDER = "company_data/"
EMPLOYEES_DATA_FOLDER = "employees_data/"

#   FUNCTIONS   FOR     DIRECTORIES
def company_file_location(filename):
    return "./{}{}.txt".format(COMPANY_DATA_FOLDER, filename.replace(" ", "_").replace(".", "_"))

def employee_file_location(filename):
    return "./{}{}.txt".format(EMPLOYEES_DATA_FOLDER, fix_text_format(filename))

#   DATA EXTRACTION
def extract_data(contents):
    fields = {}
    for line in contents:
        values = line.replace("\n", "").split(": ")
        if len(values) != 2:
            continue
        fields[values[0]] = values[1]
    return fields

def salary_read(user):
    filename = employee_file_location(user)
    file = open(filename, "r")
    contents = file.readlines()
    fields = extract_data(contents)
    est_salary = int(fields["EST. SALARY"])
    absences = int(fields["Num. of Absences"])
    overtimeHrs = int(fields["Num. of Overtime Hours"])
    late = int(fields["Num. of Times Late (in mins.)"])
    if len(contents) > 0:
        print("".join(contents))
    taxcalculator(est_salary,absences,overtimeHrs,late)
    file.close()

def info_update(user):
    filename = employee_file_location(user)
    file = open(filename, "r")
    contents = file.readlines()
    fields = extract_data(contents)
    if len(contents) > 0:
        print("".join(contents))
        print("Monthly Salary: {}".format(fields["MONTHLY SALARY"]))
    file.close()

#   MENU FUNCTIONS
def company_write():
    if fileExists(COMPANY_DATA_FOLDER) and len(listdir(COMPANY_DATA_FOLDER)) == 0:
        rmdir(COMPANY_DATA_FOLDER)
    if not fileExists(COMPANY_DATA_FOLDER):
        prompt_1 = input("Company data not found! Enroll your company? (Y/N): ").upper()
        if prompt_1 == "Y":
            try:
                mkdir(COMPANY_DATA_FOLDER)
            except OSError as osexc:
                if osexc.errno != errno.EEXIST:
                    return
                pass
            company_name = input("Enter Company Name: ")
            prompt_2 = int(input("Enter number of available positions: "))
            if prompt_2 <= 0:
                try:
                    print_message("Invalid value! Try again.")
                    company_write()
                except KeyError and ValueError:
                    print_message("Invalid value! Try again.")
                    company_write()
            positionNum = prompt_2
            for i in range(positionNum):
                company_positions = input("Enter position: ")
                est_salary = int(input("Monthly salary: "))
                filename = company_file_location(company_positions)
                file = open(filename, "w+")
                file.write("Company Position: {}\n".format(company_positions))
                file.write("Salary: {}\n".format(est_salary))
                file.close()
            print_lines()
        elif prompt_1 == "N":
            sys.exit()
        else:
            print_message("Invalid input! Try again.")
            company_write()

def company_read():
    print_lines()
    print("Available Company data: ")
    print_dir_contents(COMPANY_DATA_FOLDER)
    post_input = fix_text_format(input("To read data, enter position name: "))
    filename = company_file_location(post_input)
    if not fileExists(filename):
        print_message("Data not found!")
        main_menu()

    file = open(filename, "r")
    contents = file.readlines()
    if len(contents) > 0:
        print("".join(contents))
    file.close()
    main_menu()

def company_update():
    print_lines()
    print("Available Company data: ")
    print_dir_contents(COMPANY_DATA_FOLDER)
    post_input = fix_text_format(input("To edit data, enter position name: "))
    filename = company_file_location(post_input)
    if not fileExists(filename):
        print_message("Data not found!")
        main_menu()
    pfile = open(filename, "r+")
    contents = pfile.readlines()
    fields = extract_data(contents)
    if len(fields) == 0:
        pfile.close()
        print_message("Company data is empty!")
        main_menu()
    pfile.seek(0)
    pfile.truncate()
    print("Press enter to skip updating the specific field.")
    for key, value in fields.items():
        new_value = input("{} ({}): ".format(key, value))
        if len(new_value) > 0:
            fields[key] = new_value
        pfile.write("{}: {}\n".format(key, fields[key]))
    pfile.close()
    print_lines()
    print_message("Company data updated successfully!")
    main_menu()

def employee_write():
    if not fileExists(EMPLOYEES_DATA_FOLDER):
        mkdir(EMPLOYEES_DATA_FOLDER)
    employee_fName = input("First Name: ")
    employee_lName = input("Last Name: ")
    employee_idNum = input("Employee I.D.: ")
    filename = employee_file_location(employee_idNum)

    #   FILE EXISTENCE CHECK:
    if fileExists(filename):
        print_message("Employee already exists!")
        main_menu()

    print_dir_contents(COMPANY_DATA_FOLDER)
    employee_position = input("Enter Position: ")
    employee_absences = int(input("Number of Absences: "))
    employee_overtimeHrs = int(input("Number of Overtime Hours: "))
    employee_late = int(input("Number of Times Late (in mins.): "))

    #   DATA WRITING:
    file = open(filename, "w+")
    file.write("Employee Name: {}\n".format(employee_fName+" "+employee_lName))
    file.write("Employee I.D.: {}\n".format(employee_idNum))
    file.write("Employee's Position: {}\n".format(employee_position))
    file.write("Num. of Absences: {}\n".format(employee_absences))
    file.write("Num. of Overtime Hours: {}\n".format(employee_overtimeHrs))
    file.write("Num. of Times Late (in mins.): {}\n".format(employee_late))

    position_filename = company_file_location(employee_position)
    position_file = open(position_filename, "r+")
    contents = position_file.readlines()
    fields = extract_data(contents)
    employee_salary = fields["Salary"]
    file.write("EST. SALARY: {}\n".format(employee_salary))
    file.close()

    print_lines()
    print_message("Employee data saved successfully!")
    main_menu()

def employee_read():
    print_lines()
    print("Available employee data: ")
    print_dir_contents(EMPLOYEES_DATA_FOLDER)

    id_input = input("To read data, enter employee's I.D. Number: ")
    filename = employee_file_location(id_input)
    if not fileExists(filename):
        print_message("Employee data not found!")
        main_menu()

    # Calls function 'salary_read' and uses I.D. as parameter
    salary_read(id_input)
    print_lines()
    main_menu()

def employee_update():
    print_lines()
    print("Available employee data: ")
    print_dir_contents(EMPLOYEES_DATA_FOLDER)
    id_input = input("To update data, enter employee's I.D. Number: ")
    filename = employee_file_location(id_input)
    if not fileExists(filename):
        print_message("Employee data not found!")
        main_menu()
    employee_file = open(filename, "r+")
    contents = employee_file.readlines()
    fields = extract_data(contents)
    if len(contents) == 0 or len(fields) == 0:
        employee_file.close()
        print_message("Employee data is empty!")
        main_menu()
    employee_file.seek(0)
    employee_file.truncate()
    print("Press enter to skip updating the specific field.")
    for key, value in fields.items():
        new_value = input("{} ({}): ".format(key, value))
        if len(new_value) > 0:
            fields[key] = new_value
        employee_file.write("{}: {}\n".format(key, fields[key]))
    employee_file.close()
    print_lines()
    print_message("Employee data updated successfully!")
    main_menu()

def employee_delete():
    print_lines()
    print("Available employee data: ")
    dir_list = os.listdir(path='employees_data/')
    print(dir_list)
    print_lines()
    id_input = input("Enter Employee I.D.: ")
    if os.path.exists("employees_data/{}.txt".format(id_input)):
        os.remove("employees_data/{}.txt".format(id_input))
        print("Deleted succesfully!")
        print_lines()
    else:
        print("File not found!")
        print_lines()
    main_menu()

def confirm_prompt(msg, action):
    try:
        cmd = int(input(msg+"\n"+
                        "(1) Proceed\n"+"(2) Return to Main Menu\n"+">> "))
        if cmd == 1:
            action()
        elif cmd == 2:
            main_menu()
        else:
            raise KeyError
    except KeyError or ValueError:
        error_message()
        main_menu()

def main_menu():
    try:
        company_write()
    except KeyError and ValueError:
        print("Invalid input! Please try again.")
        if fileExists(COMPANY_DATA_FOLDER):
            shutil.rmtree(COMPANY_DATA_FOLDER)
        print_lines()
        company_write()

    #   MAIN MENU
    print_message("Welcome to Bonapay Payroll Management System")
    print("Select an action: \n"+"(1) Review company data \n"+"(2) Update company data \n"+"(3) Enroll employee \n"+
          "(4) Read employee data \n"+"(5) Update employee data\n"+"(6) Delete employee data\n"+
          "(7) Reset program\n"+"(8) Exit")
    cmd = int(input(">> "))
    print("")
    if cmd == 1:
        confirm_prompt("You are about to review your company's data.", company_read)
    elif cmd == 2:
        confirm_prompt("You are about to update your company's data.", company_update)
    elif cmd == 3:
        confirm_prompt("You are about to enroll your employee's data", employee_write)
    #   READ DATA:
    elif cmd == 4:
        confirm_prompt("You are about to enroll your employee's data", employee_read)
    elif cmd == 5:
        confirm_prompt("You are about to update your employee's data.", employee_update)
    #   DELETE EMPLOYEE DATA
    elif cmd == 6:
        confirm_prompt("You are about to delete your employee's data.", employee_delete)
    #   PROGRAM RESET:
    elif cmd == 7:
        print("This will delete all of the enrolled data. Proceed? (Y/N)")
        cmd_1 = input(">> ").upper()
        if cmd_1 == "Y":
            if fileExists(EMPLOYEES_DATA_FOLDER):
                shutil.rmtree(EMPLOYEES_DATA_FOLDER)
                print_message("Employee data deleted succesfully!")
            shutil.rmtree(COMPANY_DATA_FOLDER)
            print_message("Company data deleted succesfully!")
        else:
            error_message()
        main_menu()
    #   EXIT
    elif cmd == 8:
        sys.exit()
    else:
        print_message("Invalid input! Try again.")
        main_menu()
main_menu()
