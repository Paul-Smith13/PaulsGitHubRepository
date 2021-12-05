def fin101():
    """
1) Basic functions:
    PV: pv_f, (pvannuity, pv_perpetuity)
    
    FV: fv_f, fv_annuity, fv_annuity_due

2) How to use pv_f?
    >>> help(pv_f)
"""

def pv_f(fv, r, n):
    """
Objective: estimate present value
fv: Future Value
r: Periodic discount rate
n: number of periods
Formula: fv/(1+r)**n
"""
    return fv/(1+r)**n

def fv_f(pv, r, n):
    """
Objective: estimate future value
pv: Present Value
r: Periodic discount rate
n: number of periods
Formula:  pv*(1+r)**n
"""
    return pv*(1+r)**n

def npv_f(rate, cashflows):
    """
    Objective: estimate Net Present Value
NPV: Net Present Value
rate: Periodic discount rate
cashflows: Cashflows to be passed into function.
Fomula: NPV = (Cashflow at time t/(1+ rate)**t)
"""
    total = 0.0
    for i, cashflow in enumerate(cashflows):
        total += cashflow / (1+rate)**i
    return total

def IRR_f(cashflows, iterations=100):
    """
Objective: estimate the Internal Rate of Return
IRR: Internal Rate of Return
cashflows: Cashflows to be passed into function.
Iterations: how many times this will be done over to determine the IRR.
Fomula: IRR = (1 - NPV(rate, cashflows)/investment).
"""
    rate = 1.0
    investment=cashflows[0]
    for i in range(1, iterations+1):
        rate*=(1-npv_f(rate, cashflows)/investment)
    return rate

def pv_perpetuity_f(c, r):
    """
Objective: estimate the Present Value of a Perpetuity.
c: Coupon payment.
r: Periodic Discount rate.
Formula: PV of a Perpetuity = Coupon Payment / Discount rate.
"""
    return c/r

def pv_g_perpetuity_f(c, r, g):
    """
Objective: estimate the Present Value of a Growing Perpetuity.
c: Coupon Payment
r: Periodic Discount Rate
g: Growth rate
Formula: Present Value of a Growing Perptuity = Coupon Payment/(Discount rate - Growth Rate)
"""
    return c/(r-g)

def pv_annuity_f(PMT, r, n):
    return (PMT/r)*(1-1/(1+r)**n)
"""
Objective: Estimate the Present Value of an Annuity
PMT: Periodic Payment
r: Periodic Discount rate
n: Number of periods
Formula: Present Value of Annuity = (Payment/discount rate)* (1 - (1/(1+Discount Rate)**Number of Periods))
"""

def fv_annuity_f(PMT, r, n):
    """
Objective: Estimate the future value of an Annuity
PMT: Payment
r: Periodic Discount rate
n: Number of Periods
Formula: FV of Annuity = (Payment/Discount Rate) * ((1+Discount Rate)**Number of Periods-1)
"""
    return (PMT/r)*((1+r)**n-1)

def pv_perpetuity_due_f(c, r):
    """
Objective: Estimate the Present Value of a Perpetuity due.
c: Coupon Payment.
r: Periodic Discount rate.
Formula: PV of Perpetuity Due = (Coupon Payment/Discount rate) * (1 + Discount Rate)
"""
    return (c/r)*(1+r)

def pv_annuity_due_f(PMT, r, n):
    """
Objective: Estimate the Present Value of an Annuity due.
PMT: Periodic Payment.
r: Periodic Discount rate.
Formula: PV of Annuity Due = (Coupon Payment/Discount rate) * (1 - (1/(1 + Discount Rate)**Number of Periods)*(1 + Discount Rate)
"""
    return (PMT/r)*(1-1/(1+r)**n)*(1+r)

def pv_bond_f(c, r, n, FV):
    """
Objective: Estimate the Present Value of a bond.
c: Coupon Payment.
r: Periodic Discount rate.
n: Number of Periods.
FV: Future Value of the Bond.
Formula: PV Bond = (Coupon Payment/Discount rate) * (1 - (1/(1+Discount Rate)**Number of Periods) + Future Value/(1 + Discount rate)**Number of Periods
"""
    return (c/r) * (1-1/(1+r)**n) + FV/(1+r)**n


def EAR_f(APR, m):
    """
Objective: Convert Annual Percentage Rate to Effective Annual Rate.
EAR: Equivalent Annual Rate.
APR: Annual Percentage Rate.
m: Compounding Frequency
Formula: EAR = (1 + Annual Percentage Rate/Compounding Frequency)**Compounding Frequency - 1
"""
    return (1 + APR/m)**m - 1
