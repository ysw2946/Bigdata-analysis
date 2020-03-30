import math
def f(x): 
    return math.exp(-abs(x)) - x/(1+x*x)

def fqr(x):
    xsqr=x*x
    xsqr1=xsqr+1
    y=(xsqr-1)/xsqr1*xsqr1 + -math.exp(-x) if x>0 else math.exp(x) 
    return(y)


def newton(x,f,y, eps): 
    fx=f(x)
    for k in range(30):
        x=x-fx/y(x)
        fx=f(x)
    if (abs(fx)<eps):
        return(x)        
    print("no solution")
    return()
print(newton(1,f,fqr,0.00001))