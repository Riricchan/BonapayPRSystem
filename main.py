from os import mkdir
import os
from os.path import exists as fileExists

running = True
while running:
        print("Welcome to Bonapay Payroll Management System")
        print("-" * 50)
        print("Select an action: \n" + "(1) Enroll employee \n" +
              "(2) Read employee data \n" + "(3) Read company data\n"+
              "(4) Delete employee data\n" + "(5) Exit")
        cmd = int(input(">> "))
        print("")

        #   OPT #1 : WRITING DATA
        if cmd == 1:
            employee_fName = input("First Name: ")
            employee_lName = input("Last Name: ")
            employee_idNum = input("Employee I.D.: ")
            filename = "./employees_data/{}.txt".format(employee_idNum.replace(" ", "_").replace(".", "_"))

            #   FILE EXISTENCE CHECK:
            if fileExists(filename):
                print("Employee already exists!")
                print("-" * 50)
                continue
            if not fileExists("employees_data/"):
                mkdir("employees_data/")
                continue

            employee_absences = int(input("Number of Absences: "))
            employee_overtimeHrs = int(input("Number of Overtime Hours: "))
            employee_late = int(input("Number of Times Late (in mins.): "))

            #   COMPUTATION:
            workHrs = 8
            hr_rate = 260
            employee_salary = (((hr_rate * 8) * 26) + employee_overtimeHrs)

            #   DATA WRITING:
            file = open(filename, "w")
            file.write("Employee Name: {}".format(employee_fName + " " + employee_lName))
            file.write("Employee I.D.: {}".format(employee_idNum))
            file.write("Num. of Absences: {}".format(employee_absences))
            file.write("Num. of Overtime Hours: {}".format(employee_overtimeHrs))
            file.write("Num. of Times Late (in mins.): {}".format(employee_late))
            file.write("MONTHLY SALARY: {}".format(employee_salary))
            file.close()

            print("-" * 50)
            print("Employee data saved successfully!")
            print("-" * 50)

        #   READ EMPLOYEE DATA:
        elif cmd == 2:
            print("-" * 50)
            print("Available employee data: ")
            dir_list = os.listdir(path='employees_data/')
            print(dir_list)
            print("-" * 50)

            post_input = input("To read data, enter employee's I.D. Number: ")
            filename = "./employees_data/{}.txt".format(post_input.lower().replace(" ", "_").replace(".", "_"))
            if not fileExists(filename):
                print("Employee data not found!")
                print("-" * 50)
                continue

            file = open(filename, "r")
            contents = file.readlines()
            if len(contents) > 0:
                print("\n".join(contents))
            file.close()

        elif cmd == 3:
            print("-" * 50)
            print("Available Company data: ")
            dir_list = os.listdir(path='company_data/')
            print(dir_list)
            print("-" * 50)

            post_input = input("To read data, enter position name: ")
            filename = "./company_data/{}.txt".format(post_input.lower().replace(" ", "_").replace(".", "_"))
            if not fileExists(filename):
                print("Data not found!")
                print("-" * 50)
                continue

            file = open(filename, "r")
            contents = file.readlines()
            if len(contents) > 0:
                print("\n".join(contents))
            file.close()

        #   DELETE EMPLOYEE DATA:
        elif cmd == 4:
            print("-" * 50)
            print("Available employee data: ")
            dir_list = os.listdir(path='employees_data/')
            print(dir_list)
            print("-" * 50)
            post_input = input("Enter Employee I.D.: ")
            if os.path.exists("employees_data/{}.txt".format(post_input)):
                os.remove("employees_data/{}.txt".format(post_input))
                print("Deleted succesfully!")
                print("-" * 50)
                continue
            else:
                print("File not found!")
                print("-" * 50)

        #   EXIT
        elif cmd == 5:
            running = False


#  MAIN MENU:
        filename = "./company_data/.txt"
        if fileExists(filename):
            continue
        if not fileExists("company_data/"):
            prompt_1 = input("Company data not found! Enroll your company? (Y/N): ")
            if prompt_1 == "Y" or "y":
                mkdir("company_data/")
                company_name = input("Enter Company Name: ")
                prompt_2 = int(input("Enter number of available positions: "))
                positionNum = prompt_2
                for i in range(positionNum):
                    company_positions = input("Enter position: ")
                    post_salary = float(input("Monthly salary: "))
                    filename = "./company_data/{}.txt".format(company_positions.replace(" ", "_").replace(".", "_"))
                    file = open(filename, "w")
                    file.write("Company Position: {}".format(company_positions))
                    file.write("Salary: {}".format(post_salary))
                continue