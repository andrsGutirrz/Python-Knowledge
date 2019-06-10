"""
Demo irrelevante sobre interes compuesto solo para ejercicio de FP
@author loriacrlos@gmail.com
@since II-2018
"""
def compound_interest(conditions):
    principal, yearly_rate, term_in_years = (conditions['principal'], 
                                             conditions['yearly_rate'], 
                                             conditions['term_in_years']) 
    month = 0
    term_in_months = term_in_years * 12
    payments = [None] * term_in_months
    monthly_rate = yearly_rate / 1200
    while month < term_in_months:
        principal *= (1 + monthly_rate)
        payments[month] = principal
        month += 1
    return payments
    
def total_amount(payments):
    total = 0
    for i in range(len(payments)):
        total += payments[i]
    return total
    
def growth(payments, conditions):
    return payments[-1] - conditions['principal']
    
def print_table(conditions):
    #
    payments = compound_interest(conditions)
    total_growth = growth(payments, conditions)
    #
    margin = " " * 3
    separation = " " * 3
    print(">> Conditions: principal=${principal:0,.2f}; rate={yearly_rate:0.2f}annually%;  term={term_in_years:0,.2f}years <<".format(**conditions))
    header = f"{margin}Month{separation}Principal"
    underline = "-" * ( len(header) + len(margin) )
    print(underline)
    print(header)
    print(underline)
    n = len(payments)
    for i in range(n):
        print(f"{margin}{(i+1):^5d}{separation}{payments[i]:>8,.2f}")
    print(underline)
    footer = f"{margin}{n:^5d}{separation}{total_growth:,>0,.2f}"
    print(footer)
   
    
def test():
    print("*** Simple Compound Interest ***")
    conditions = {'principal' : 10_000, 'yearly_rate' : 21, 'term_in_years' :2}
    print_table(conditions)

if __name__ == "__main__":
    test()