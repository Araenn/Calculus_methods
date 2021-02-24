x0 = 2
tol = 1e-16
maxITER = 2
xm1 = 5/2
def f(x):
    return x**2 - 2  #function


def Secant(xm1, x0, tol, maxITER):  #secant : for simple roots, allows to avoid having to derive the functions
    xk = x0
    xkm1 = xm1
    k = 0 # indice d'iteration
    fx = f(x0)
    print ("Initial value : ", xk)
    while ((abs(fx) > tol) and (k < maxITER)):
        xkp1 = xk - (f(xk)*(xk-xkm1))/(f(xk)-f(xkm1))
        xkm1 = xk
        xk = xkp1
        fx = f(xkp1)
        k += 1
        print ("Iteration ", k, " : ", xk)
    return (xk)


Secant(xm1, x0, tol, maxITER)
