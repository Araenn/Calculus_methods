#calculates the maximum height z that a ball of mass m can reach, taking into account friction k, initial velocity v0 and accuracy p.

m = float(input("Choose the mass of the ball :"))
v0 = float(input("Choose v0 :"))
k = float(input("The friction :"))
p = float(input("And finally the precision :"))
dt = 0.1
z1 = 0

while (True):
    z = 0
    v = v0
    counter = 0

    while (True):
        z = z + v*dt
        v = v - a*dt
        a = 9.81 + (k/m) * (v*v)
        counter = counter + 1
        if (v <= 0):
            print("The maximum altitude is ", z, "m.")
            break
    if abs(z - z1) < p:
        break
    else:
        z1 = z
        dt = dt/10
print("The number of iterations is ", counter, "for a scale of ", dt, ".")
