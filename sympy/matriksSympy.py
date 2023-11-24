#%%

from sympy.interactive.printing import init_printing
#init_printing(use_unicode=False, wrap_line=False)
from sympy.matrices import Matrix, Transpose
from sympy import symbols, sin, cos
from mpmath import radians

alpha, beta, gamma = symbols('alpha beta gamma')
Ixx, Iyy, Izz = symbols('I_xx, I_yy, I_zz')
Ixy, Ixz, Iyz = symbols('I_xy, I_xz, I_yz')

I = Matrix([[Ixx, Ixy, Ixz], \
           [Ixy, Iyy, Iyz], \
           [Ixz, Iyz, Izz]])

Rx = Matrix([[1, 0, 0], \
            [0, cos(gamma), -sin(gamma)], \
            [0, sin(gamma), cos(gamma)]])

Ry = Matrix([[cos(beta), 0, sin(beta)], \
            [0, 1, 0], \
            [-sin(beta), 0, cos(beta)]])

Rz = Matrix([[cos(alpha), -sin(alpha), 0], \
            [sin(alpha), cos(alpha), 0], \
            [0, 0, 1]])

R = Rz*Ry*Rx

Irot = R*I*Transpose(R)

Irot.subs([(alpha, radians(45)), (beta, radians(45)), (gamma, radians(45))])


# represents a rotation whose yaw, pitch, and roll angles are α, β and γ, respectively. 
# %%





#%%
# https://reliability.readthedocs.io/en/latest/Solving%20simultaneous%20equations%20with%20sympy.html

# Los op die volgende vergelyking:

import sympy as sym
a,b = sym.symbols('a,b')
eq1 = sym.Eq(a*1000000**b,119.54907)
eq2 = sym.Eq(a*1000**b,405)
result = sym.solve([eq1,eq2],(a,b))
print(result)

'''
[(1372.03074854535, -0.176636273742481)] #these are the solutions for a,b
'''
# %%
# Eie voorbeeld:

Ixy, Iyz, Izx = sym.symbols('I_xy, I_yz, I_zx')

eq1 = sym.Eq(3*Ixy + 4*Iyz + Izx,15.7)
eq2 = sym.Eq(15*Ixy - 0.5*Iyz + 2*Izx,300)
eq3 = sym.Eq(20*Ixy - 23*Iyz - 12*Izx,100)
result = sym.solve([eq1,eq2, eq3],(Ixy,Iyz, Izx))
print(result)

# %%

# https://docs.sympy.org/latest/guides/solving/solve-system-of-equations-algebraically.html

from sympy import solve
from sympy.abc import x, y, z
solve([x + y - 2*z, y + 4*z], [x, y], dict=True)
# %%

