x0 = 1   #choose a value
maxITER = 10  #you can take a huge number, because of the tolerance under
tol = 1e-16  #tolerance digits

def Newton(x0, tol, maxITER):
    xk = x0
    k = 0 #iteration indice
    fx = f(x0)
    print ("Valeur initiale : ", xk)
    while ((abs(fx) > tol) and (k < maxITER)):
        xk = xk - f(xk)/fp(xk)  #write the phi here
        fx = f(xk)
        k += 1
        print ("Iteration ", k, " : ", xk)
    return xk
    
def f(x):
    return x - (1.1)**1/3  #function
    
def fp(x):
    return 1  #derivative of f(x)
    
Newton(x0, tol, maxITER)
