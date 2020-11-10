def taxcalculator(estim_salary,emp_absent, ot_hours,late_num):
    #   BASE COMPUTATION
    HR_RATE = 260
    WORK_HOURS = 8
    WORK_DAYS = 26
    ABSENT_FORM = 24*emp_absent
    LATE_FORM = late_num/60
    base_form = (((HR_RATE*WORK_HOURS)*WORK_DAYS)+ot_hours)-(ABSENT_FORM+LATE_FORM)

    #   TAX
    SSS_CONTRIB = 581.30
    ph_contrib =  275
    PAG_IBIG_fund = 100
    tax_form = SSS_CONTRIB+PAG_IBIG_fund+ph_contrib

    est_salary = estim_salary
    minSalary = 0
    maxSalary = 20000


    #if minSalary <= est_salary <= maxSalary:

    fin_salary = base_form-tax_form
    print(fin_salary)