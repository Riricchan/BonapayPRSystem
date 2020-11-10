import shutil
import sys
from os import mkdir, listdir
from os.path import exists as fileExists

COMPANY_DATA_FOLDER = "company_data/"
EMPLOYEES_DATA_FOLDER = "employees_data/"
running = True

#   FUNCTIONS
def company_file_location(filename):
    return "./{}{}.txt".format(COMPANY_DATA_FOLDER, filename)

def employee_file_location(filename):
    return "./{}{}.txt".format(EMPLOYEES_DATA_FOLDER, fix_text_format(filename))

def fix_text_format(user):
    return user.lower().replace(" ", "_").replace(".", "_")

def extract_data(contents):
    fields = {}
    for line in contents:
        values = line.split(": ")
        fields[values[0]] = values[1]
    return fields

def print_lines():
    print("-" * 50)

def print_dir_contents(folder):
    dir_list = listdir(folder)
    print(dir_list)
    print_lines()

def print_message(msg):
    print(msg)
    print_lines()

def salary_read(user):
    filename = employee_file_location(user)
    file = open(filename, "r")
    contents = file.readlines()
    fields = extract_data(contents)    

    est_salary = fields["EST. SALARY"]
    salary_bracketing(est_salary)

    if len(contents) > 0:
        print("".join(contents))
        print("Estimated Salary: {}".format(fields["EST. SALARY"]))

        salary_bracketing(est_salary)

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

def salary_bracketing(emp_salary):
    global employee_position
    est_salary = emp_salary
    fields = extract_data(contents)
    employee_position = fields["Company Position"]

    if est_salary <=20000:
        filename = company_file_location(employee_position.replace(" ", "_").replace(".", "_"))
        company_fields = extract_data(contents)
        employee_position = fields["Deductions"]

while running:
    #   PROGRAM EXISTENCE CHECK:
    filename = "./{}/.txt".format(COMPANY_DATA_FOLDER)
    if fileExists(filename):
        continue

    if not fileExists(COMPANY_DATA_FOLDER):
        prompt_1 = input("Company data not found! Enroll your company? (Y/N): ").upper()
        if prompt_1 == "Y":
            mkdir(COMPANY_DATA_FOLDER)
            company_name = input("Enter Company Name: ")
            prompt_2 = int(input("Enter number of available positions: "))
            positionNum = prompt_2
            for i in range(positionNum):
                company_positions = input("Enter position: ")
                est_salary = int(input("Monthly salary: "))
                filename = company_file_location(company_positions.replace(" ", "_").replace(".", "_"))
                file = open(filename, "w")
                file.write("Company Position: {}\n".format(company_positions))
                file.write("Salary: {}\n".format(est_salary))

                if est_salary <= 20000:
                    salary_deductions = {"SSS": 300, "PhilHealth": 500, "PAG-IBIG": 100}
                    file.write("Deductions {}\n".format(salary_deductions))

            continue
        elif prompt_1 == "N":
            sys.exit()

    #   MAIN MENU
    print_message("Welcome to Bonapay Payroll Management System")
    print("Select an action: \n"+"(1) Review company data \n"+"(2) Enroll employee \n"+
          "(3) Read employee data \n"+"(4) Delete employee data\n"+"(5) Reset program\n"+
          "(6) Exit")
    cmd = int(input(">> "))
    print("")

    if cmd == 1:
        print_lines()
        print("Available Company data: ")
        print_dir_contents(COMPANY_DATA_FOLDER)

        post_input = fix_text_format(input("To read data, enter position name: "))
        filename = company_file_location(post_input)
        if not fileExists(filename):
            print_message("Data not found!")
            continue

        file = open(filename, "r")
        contents = file.readlines()
        if len(contents) > 0:
            print("".join(contents))
        file.close()

    #   OPT #2 : WRITING DATA
    elif cmd == 2:
        if not fileExists(EMPLOYEES_DATA_FOLDER):
            mkdir(EMPLOYEES_DATA_FOLDER)
        employee_fName = input("First Name: ")
        employee_lName = input("Last Name: ")
        employee_idNum = input("Employee I.D.: ")
        filename = employee_file_location(employee_idNum)

        #   FILE EXISTENCE CHECK:
        if fileExists(filename):
            print_message("Employee already exists!")
            continue
        
        employee_position = (input("Enter Position: "))
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

        filename = company_file_location(fix_text_format(employee_position))
        contents = file.readlines()
        fields = extract_data(contents)
        employee_salary = fields["Salary"]

        file.write("EST. SALARY: {}\n".format(employee_salary))
        file.close()

        print_lines()
        print_message("Employee data saved successfully!")

    #   READ DATA:
    elif cmd == 3:
        print_lines()
        print("Available employee data: ")
        print_dir_contents(EMPLOYEES_DATA_FOLDER)

        id_input = input("To read data, enter employee's I.D. Number: ")
        filename = employee_file_location(id_input)
        if not fileExists(filename):
            print_message("Employee data not found!")
            continue

        # Calls function 'salary_read' and uses I.D. as parameter
        salary_read(id_input)

    #   DELETE EMPLOYEE DATA
    elif cmd == 4:
        print_lines()
        print("Available Company data: ")
        print_dir_contents(COMPANY_DATA_FOLDER)

        post_input = fix_text_format(input("To read data, enter position name: "))
        filename = company_file_location(post_input)
        if not fileExists(filename):
            print_message("Data not found!")
            continue

        file = open(filename, "r")
        contents = file.readlines()
        if len(contents) > 0:
            print("\n".join(contents))
        file.close()

    #   PROGRAM RESET:
    elif cmd == 5:
        print("This will delete all of the enrolled data. Proceed? (Y/N)")
        cmd_1 = input(">> ").upper()
        if cmd_1 == "Y":
            if fileExists("employees_data"):
                shutil.rmtree("employees_data")
                print_message("Employee data deleted succesfully!")
            shutil.rmtree("company_data")
            print_message("Company data deleted succesfully!")

    #   EXIT
    elif cmd == 6:
        running = False

    else:
        print("Invalid input! Try again.")
        continue