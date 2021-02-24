import math

x0 = 0.01
maxITER = 100  #please take a huge number like 100

def FP(x0, maxITER):
    print ("Initial Value : ", x0)
    for k in range(maxITER) :
        x0 = math.sqrt(x0)
        print ("Iteration ", k + 1, " : ", x0)
    return x0


FP(x0, maxITER)
