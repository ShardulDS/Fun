# %%
from sympy import (exp, im, re, cos, sin, tan, sec,Lambda, sympify, 
Abs, simplify, diff, Matrix, init_printing, Function, Derivative, dsolve,
atanh, Symbol, pprint, latex, Integer)
from sympy.polys import apart
from sympy.solvers import solve
from sympy import csc as cosec
from sympy import integrate as intg
from sympy.abc import x, i

init_printing()

# %%
f = list(map(int, input('Enter coeffs of lhs of cauchy-legnedre diff eq: ').split()))
rhs = input('Enter rhs of eqn: ')
for i in range(len(f)):
    f[i] = Integer(f[i])
q = sympify(rhs)

# %%
y = Function('y')
d1 = Derivative(y(x), x)
d2 = Derivative(y(x), x, x)
y = dsolve(f[0]*(x**2)*d2 + f[1]*x*d1 + f[2]*y(x) - q, y(x))

#%%
y
