import math

print("beliebige Seite gesucht drücke: 1")
print("Hypotenuse gesucht drücke: 2")

choose = int(input("Auswahl: "))

if choose == 1:
    a = float(input("Hypotenuse: "))
    b = float(input("beliebige Seite: "))

    c = (a*a)-(b*b)
    Lösung = math.sqrt(c)

    print("beliebige Seite:")
    print(round(Lösung, 2))

input()

if choose == 2:
    a = float(input("beliebige Seite:"))
    b = float(input("beliebige Seite:"))

    c = (a*a)+(b*b)
    Lösung = math.sqrt(c)

    print("Hypotenuse:")
    print(round(Lösung, 2))

input()

