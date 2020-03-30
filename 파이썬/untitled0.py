from sympy import Symbol, solve
x=Symbol('x')
y=Symbol('y')
z=Symbol('z')
equation1 = 2*x+2*y+z-8
equation2 = 2*x+3*y+z-9
equation3 = x+3*y+2*z-2
solve((equation1,equation2,equation3),dict=True)
