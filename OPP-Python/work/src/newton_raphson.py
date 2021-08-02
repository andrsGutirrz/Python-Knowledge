"""
Demo irrelevante sobre newthon-raphson solo para ejercicio de FP
Se debe implementar todo lo que dice 'todo'
@author loriacrlos@gmail.com
@since II-2018
"""

from todo import todo
from functools import reduce

class Poly(tuple):
    """
        Polynom as coeffcients list
    """
    def __init__(self, *args, var = "x"): #constructor
        """ Creates polynom """
        super(Poly,self).__new__(Poly,args)
        self.var = var
        self.epsilon =1e-5
        self.max = 20
        self.fdx = None
        #todo(self.__init__, "Must be inmutable",
        #                    "args must a list of numbers")


    def __str__(self):
        #todo(self.__str__)
        return super(Poly, self).__str__()

    def __repr__(self):
        #todo(self.__repr__)
        return super(Poly, self).__repr__()
        #"".join([ str(c)+"x^("+str(len(self)-p-1)+")" if p is not len(self)-1 else str(c) for p,c in enumerate(self) ])



    @property
    def dx(self):
        """ Derivates the polynome """
        #todo(self.dx, "Must be property", "Calculated just once if called several times")
        if self.fdx: return self.fdx
        dx = [c*(len(self)-1-i)  for i,c in enumerate(self)]
        self.fdx = tuple(dx[:-1:])
        return self.fdx

    def __call__(self, val):
        """ Evaluates the polynom """
        expr = (c*val**(len(self)-1-i) if i is not len(self)-1 else c for i,c in enumerate(self))
        return reduce(lambda a,b:a+b,expr,0)

    @property
    def degree(self):
        """ Polynom´s degree. Must be aproperty """
        #todo(self.degree, "Must be property")
        return (len(self) - 1)

    def solve(self, r0=None ):
        """ Solves by Newton-raphson starting in r0 """
        #todo(self.solve, "r0 must be a number")
        if not r0:
            return self[-1] / self.degree
        else:
            return r0 - Poly.__call__(self,r0) / Poly.__call__(self.fdx,r0)



    def __floordiv__(self, alpha):
        """ Performs synthetic division by x - alpha """
        #todo(self.__floordiv__,
        #     "alpha must be a number",
        #     "Returns a new poly"
        #    )
        arr = []
        for i,c in enumerate(self):
            if i is 0:
                arr.append(c)
            else:
                arr.append(self[i]+arr[i-1]*alpha)
        return Poly(arr[:-1:])

    def roots(self):
        """ Finds all root by using solve and // repeatedly """

        return ( self.solve() for e in self.fdx)


if __name__ == "__main__":
    p = Poly([1, -7, 7, 15])
    print(p)
    print(p(3))
    print(p.dx)
    print(p.solve(3))
    print(p // 5)
    #print(list(p.roots()))
    print( list( map( lambda n: round(n, 6), p.roots()) ) )
