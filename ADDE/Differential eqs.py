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
f = list(map(int, input('Enter coeffs of lhs of diff eq: ').split()))
rhs = input('Enter rhs of eqn: ')
for i in range(len(f)):
    f[i] = Integer(f[i])
q = sympify(rhs)
extra = input("Enter value of f(0) and f'(0):")

#%%
y = Function('y')
d1 = Derivative(y(x), x)
d2 = Derivative(y(x), x, x)
if extra != '':
    extra = extra.split()
    y = dsolve(f[0]*d2 + f[1]*d1 + f[2]*y(x) - q, y(x), ics = {y(0): Integer(extra[0]), y(x).diff(x).subs(x, 0): Integer(extra[1])})
else:
    y = dsolve(f[0]*d2 + f[1]*d1 + f[2]*y(x) - q, y(x))
# %%
y
# %%
lhs = sympify(f[0]*(x**2) + f[1]*x + f[2])
m = solve(lhs, x)
if len(m) == 1:
    y1 = exp(m[0]*x)
    y2 = x*exp(m[0]*x)
elif im(m[0]) != 0:
    y1 = exp(Abs(re(m[0]))*x)*cos(Abs(im(m[0]))*x)
    y2 = exp(Abs(re(m[0]))*x)*sin(Abs(im(m[0]))*x)
elif m[0] != m[1]:
    y1 = exp(m[0]*x)
    y2 = exp(m[1]*x)

# %%
y1
# %%
y2
# %%
w = simplify(Matrix([[y1, y2], [diff(y1), diff(y2)]]).det())
if w != 0:
    yp = simplify((-y1*intg(y2*q/w, x) + y2*intg(y1*q/w, x)))
    C1 = Symbol('C1')
    C2 = Symbol('C2')
    sol = C1*y1 + C2*y2 + yp
else:
    sol = 'No solution available for this diff eq.'
    
# %%
sol
