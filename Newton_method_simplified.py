x0 = 5
maxITER = 20
tol = 1e-16
m = 2  #square multiplicity order

def f(x):
    return (x**2-x)**2  #your function
    
def fp(x):
    return 2*(2*x-1)*(x**2-x)  #derivative of f(x) !!please put the factorised form!!

def Newton2(x0, tol, maxITER):
    xk = x0
    k = 0
    fx = f(x0)
    print ("Initial value : ", xk)
    while ((abs(fx) > tol) and (k < maxITER)):
        xk = xk - m*f(xk)/fp(xk)
        fx = f(xk)
        k += 1
        print ("Iteration ", k, " : ", xk)
    return xk
    

Newton2(x0, tol, maxITER)
