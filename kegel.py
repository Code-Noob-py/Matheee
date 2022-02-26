import math

print("V und Ao")

r = float(input("r:"))
s = float(input("s:"))
h = float(input("h:"))
pi = 3.141592654

Ao = (pi*(r*r))+pi*r*s

print("Ao:")
print(round(Ao, 2))

V = (r*r)/3*h
print("V")
print(round(V, 2))

input()