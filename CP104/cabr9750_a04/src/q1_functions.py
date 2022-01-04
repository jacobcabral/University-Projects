"""
------------------------------------------------------------------------
[functions for q1]
------------------------------------------------------------------------
Author: Jacob Cabral
ID:     190689750
Email:  cabr9750@mylaurier.ca
__updated__ = "2019-10-1"
------------------------------------------------------------------------
"""
def calc_federal_tax(income):
    '''
    ------------------------------------------------------------------------------
    Calculates taxes using federal tax rate
    ------------------------------------------------------------------------------
    Use: calc_federal_tax(income):
    ------------------------------------------------------------------------------
    Paramaters
        income = The user's income, in dollars (float>0)
    Returns
    The amount of tax dollars to be paid
    ------------------------------------------------------------------------------    
    '''
    TAX_RATE = 35
    federal_tax_liability = (income-100000)*(TAX_RATE/100)+21500
    
    return federal_tax_liability

def calc_prov_tax(income):
    '''
    ------------------------------------------------------------------------------
    calculates taxes using the provincal (state) tax rate
    ------------------------------------------------------------------------------
    Use: calc_prov_tax(income):
    ------------------------------------------------------------------------------
    Paramaters
        income = the user's income, in dollars (float>0)
    Returns
    The amount of tax dollars to be paid, also known as tax liability
    ------------------------------------------------------------------------------    
    '''
    TAX_RATE = 5
    
    provincial_tax_liability = (income-50000)*(TAX_RATE/100)
    return provincial_tax_liability
    