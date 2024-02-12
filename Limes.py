import sympy as sp
from sympy import *
import math

def filter(number):
    if number == 'inf':
        print("plus except")
        return math.inf
    elif number == '-inf':
        print("minus execpt")
        return -math.inf
    else:
        return int(number)

def func_return(expr, gw):
    x = symbols('x')
    return expr.subs(x, gw)

def limes(func_return, geg, approach, expr, h=1e-6):
        if approach == 'beide':
            left_limit = func_return(expr, geg - h)
            right_limit = func_return(expr, geg + h)
            if geg == '-inf':
                return -(left_limit + right_limit)/2
            else:
                return (left_limit + right_limit)/2
    
        elif approach == 'links':
            return func_return(expr, geg + h)

        elif approach == 'rechts':
            return func_return(expr ,geg + h)
