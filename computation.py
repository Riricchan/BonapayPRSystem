def taxcalculator(estim_salary,emp_absent, ot_hours,late_num,civstat,dependents):
    #   BASE COMPUTATION. Variables in CAPS mean it's CONSTANT. DO NOT CHANGE!
    #   Modify HR_RATE variable. Refer to DAVAO'S MINIMUM WAGE RATE.

    HR_RATE = 260
    WORK_HOURS = 8
    WORK_DAYS = 26
    ABSENT_FORM = 24*emp_absent
    LATE_FORM = late_num/60
    base_form = (((HR_RATE*WORK_HOURS)*WORK_DAYS)+ot_hours)-(ABSENT_FORM+LATE_FORM)

    #   TAX (PLEASE EDIT BASED ON THE BRACKETING)
    SSS_CONTRIB = 581.30
    ph_contrib =  275
    PAG_IBIG_fund = 100
    tax_deduc = 0
    tax_form = SSS_CONTRIB+PAG_IBIG_fund+ph_contrib+tax_deduc

    #   DEPENDENTS
    civil_stat = civstat
    emp_depend = dependents


    est_salary = estim_salary
    #   HARDCODE the min/max salary. Base it on the salary bracketing table.

    if 0 <= est_salary <= 9999:
        # I-CHANGE IF NEED
        tax_deduc = 0.05
        ph_contrib = 275
        SSS_CONTRIB = 100
        fin_salary = base_form-tax_form

    elif 10000 <= est_salary <= 29999:
        # I-CHANGE IF NEED
        tax_deduc = 0.05
        ph_contrib = 275
        SSS_CONTRIB = 100
        fin_salary = base_form-tax_form

    print("SALARY OF THE MONTH: {}".format(fin_salary))