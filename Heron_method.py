import math

A = 2
maxITER = 5
xk = 2


def methodHERON(A, xk, maxITER):
    print ("Valeur initiale : ", xk)
    for k in range(maxITER):
        xk = 0.5*(A/xk + xk)
        print ("Iteration ", k + 1, " : ", xk)
    return xk
    
methodHERON(A, xk, maxITER)
