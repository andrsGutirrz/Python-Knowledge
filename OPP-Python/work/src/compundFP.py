"""
Demo irrelevante sobre interes compuesto solo para ejercicio de FP
@author Loria-Grupo 3
@since II-2018
"""
from functools import reduce


def genPrincipal(monthly_rate, principal):
    """"  Genera el valor del interes compuesto a lo largo de los meses   """
    principal *= (1 + monthly_rate)
    while True:
        yield principal
        principal *= (1 + monthly_rate)

def compound_interest(conditions):
    """  Realiza el todo calculo del interes compuesto, devuelve la lista con los pagos de todos los meses  """
    principal, yearly_rate, term_in_years = (conditions['principal'], 
                                             conditions['yearly_rate'], 
                                             conditions['term_in_years']) 
    month = 0
    term_in_months = term_in_years * 12
    """ payments es una lista """
    payments = [0] * term_in_months 
    monthly_rate = yearly_rate / 1200
    gene = genPrincipal(monthly_rate,principal)
    """ Usando el generador, se hace una lista """
    return list(map(lambda x :next(gene),payments))

    """ Tambien se puede hacer por medio de una lista por comprension """
    # [next(gene) for x in range(len(payments))]
    
def total_amount(payments):
    """ Sumamos todos los elementos de payments, aunque esta funcion no se llama en ninguna parte """
    total = reduce(lambda x,y: x+y,payments)
    return total
    
def growth(payments, conditions):
    return payments[-1] - conditions['principal']
    
def print_table(conditions):
    """ Impreme los resultados en formato de columnas """
    payments = compound_interest(conditions)
    total_growth = growth(payments, conditions)
    margin = " " * 3
    separation = " " * 3
    print(">> Conditions: principal=${principal:0,.2f}; rate={yearly_rate:0.2f}annually%;  term={term_in_years:0,.2f}years <<".format(**conditions))
    header = f"{margin}Month{separation}Principal"
    underline = "-" * ( len(header) + len(margin) )
    print(underline)
    print(header)
    print(underline)
    n = len(payments)
    """  se imprime cada elemento de payments, utilizando map para poder acceder a cada indice """
    list(map(lambda i :  print(f"{margin}{(i+1):^5d}{separation}{payments[i]:>8,.2f}") , range(n)))
    print(underline)
    footer = f"{margin}{n:^5d}{separation}{total_growth:,>0,.2f}"
    print(footer)
    print("FP")
   
    
def test():
    print("*** Simple Compound Interest FP***")
    conditions = {'principal' : 10_000, 'yearly_rate' : 21, 'term_in_years' :2}
    print_table(conditions)

if __name__ == "__main__":
    test()