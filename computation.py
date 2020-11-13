def taxdeduc(SSS,philHealth,pagIbig,deduc):
    SSS_CONTRIB = SSS
    ph_contrib =  philHealth
    PAG_IBIG_fund = pagIbig
    tax_deduc = deduc
    tax_formula = float(SSS_CONTRIB+PAG_IBIG_fund+ph_contrib+tax_deduc)

    return tax_formula

def taxcalculator(estim_salary,emp_absent, ot_hours,late_num):
    est_salary = estim_salary

    ABSENT_FORM = emp_absent
    LATE_FORM = (late_num/60)/24
    daily_wage = estim_salary/26
    overtime_pay = float(daily_wage*(0.10*ot_hours))
    base_form = float(ABSENT_FORM+LATE_FORM)

    #   HARDCODE the min/max salary. Base it on the salary bracketing table.

    if 0 <= est_salary <= 9999:
        tax_deduc = 0.05
        ph_contrib = 300
        SSS_CONTRIB = 1200
        PAG_IBIG_fund = 0.02

        deductions = base_form+taxdeduc(SSS_CONTRIB,ph_contrib,PAG_IBIG_fund,tax_deduc)
        print("Total Salary Deductions: {}PHP".format(round(deductions,2)))
        print("Total Salary Additions: {}PHP".format(round(overtime_pay,2)))
        fin_salary = (est_salary+overtime_pay)-(deductions)

        print("SALARY OF THE MONTH: {}PHP".format(round(fin_salary,2)))

    elif 10000 <= est_salary <= 29999:
        tax_deduc = 0.1
        ph_contrib = 300
        SSS_CONTRIB = 2400
        PAG_IBIG_fund = 0.02

        deductions = base_form+taxdeduc(SSS_CONTRIB,ph_contrib,PAG_IBIG_fund,tax_deduc)
        print("Total Salary Deductions: {}PHP".format(round(deductions,2)))
        print("Total Salary Additions: {}PHP".format(round(overtime_pay,2)))
        fin_salary = (est_salary+overtime_pay)-(deductions)

        print("SALARY OF THE MONTH: {}PHP".format(round(fin_salary,2)))

    elif 30000 <= est_salary <= 69999:
        tax_deduc = 0.15
        ph_contrib = 1800
        SSS_CONTRIB = 2400
        PAG_IBIG_fund = 0.02

        deductions = base_form+taxdeduc(SSS_CONTRIB,ph_contrib,PAG_IBIG_fund,tax_deduc)
        print("Total Salary Deductions: {}PHP".format(round(deductions,2)))
        print("Total Salary Additions: {}PHP".format(round(overtime_pay,2)))
        fin_salary = (est_salary+overtime_pay)-(deductions)

        print("SALARY OF THE MONTH: {}PHP".format(round(fin_salary,2)))

    elif 70000 <= est_salary <= 139999:
        tax_deduc = 0.2
        ph_contrib = 1800
        SSS_CONTRIB = 2400
        PAG_IBIG_fund = 0.02

        deductions = base_form+taxdeduc(SSS_CONTRIB,ph_contrib,PAG_IBIG_fund,tax_deduc)
        print("Total Salary Deductions: {}PHP".format(round(deductions,2)))
        print("Total Salary Additions: {}PHP".format(round(overtime_pay,2)))
        fin_salary = (est_salary+overtime_pay)-(deductions)

        print("SALARY OF THE MONTH: {}PHP".format(round(fin_salary,2)))

    elif 140000 <= est_salary <= 249999:
        tax_deduc = 0.25
        ph_contrib = 1800
        SSS_CONTRIB = 2400
        PAG_IBIG_fund = 0.02

        deductions = base_form+taxdeduc(SSS_CONTRIB,ph_contrib,PAG_IBIG_fund,tax_deduc)
        print("Total Salary Deductions: {}PHP".format(round(deductions,2)))
        print("Total Salary Additions: {}PHP".format(round(overtime_pay,2)))
        fin_salary = (est_salary+overtime_pay)-(deductions)

        print("SALARY OF THE MONTH: {}PHP".format(round(fin_salary,2)))

    elif 250000 <= est_salary <= 499999:
        tax_deduc = 0.3
        ph_contrib = 1800
        SSS_CONTRIB = 2400
        PAG_IBIG_fund = 0.02

        deductions = base_form+taxdeduc(SSS_CONTRIB,ph_contrib,PAG_IBIG_fund,tax_deduc)
        print("Total Salary Deductions: {}PHP".format(round(deductions,2)))
        print("Total Salary Additions: {}PHP".format(round(overtime_pay,2)))
        fin_salary = (est_salary+overtime_pay)-(deductions)

        print("SALARY OF THE MONTH: {}PHP".format(round(fin_salary,2)))

    elif est_salary >= 500000:
        tax_deduc = 0.32
        ph_contrib = 1800
        SSS_CONTRIB = 2400
        PAG_IBIG_fund = 0.02

        deductions = base_form+taxdeduc(SSS_CONTRIB,ph_contrib,PAG_IBIG_fund,tax_deduc)
        print("Total Salary Deductions: {}PHP".format(round(deductions,2)))
        print("Total Salary Additions: {}PHP".format(round(overtime_pay,2)))
        fin_salary = (est_salary+overtime_pay)-(deductions)

        print("SALARY OF THE MONTH: {}PHP".format(round(fin_salary,2)))