from functools import reduce

s = ('A','N','D','R','E','S')

def conc(a,b):
    return a + b

reduceFunc = reduce(conc, s)

reduceLamb = reduce(lambda x,y: x+y, s)

print ("Con la funcion ",reduceFunc)
print ("Con lambda",reduceLamb)


def genPrincipal(monthly_rate, principal):
    principal *= (1 + monthly_rate)
    while True:
        yield principal
        principal *= (1 + monthly_rate)

def compound_interest(conditions):
    principal, yearly_rate, term_in_years = (conditions['principal'], 
                                             conditions['yearly_rate'], 
                                             conditions['term_in_years']) 
    month = 0
    term_in_months = term_in_years * 12
    payments = [0] * term_in_months
    monthly_rate = yearly_rate / 1200
    gene = genPrincipal(monthly_rate,principal)
    return list(map(lambda x :next(gene),payments))

    # [next(gene) for x in range(len(payments))]
    # list(map(lambda x :next(gene),payments))


def compound_interest2(conditions): #NORMAL
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

conditions = {'principal' : 10_000, 'yearly_rate' : 21, 'term_in_years' :2}
print(compound_interest2(conditions))
print(compound_interest(conditions))