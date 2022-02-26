

print("Berechnung von Oberflächeninhalt und Volumen")
print("Ao und V für Gleichseitiges Dreiecks Prisma: 1")
print("Ao und V für  Dreiecks Prisma: 2")
print("Ao und V für Trapez Prisma: 3")

choose = int(input("Auswahl: "))
if choose == 1:
    g = float(input("Die entsprechende Seite: "))
    hd = float(input("Die entsprechende Höhe: "))
    AG = g * hd / 2
    print("AG:")
    print(round(AG, 2))
    h = float(input("Höhe vom Körper: "))
    AM = AG * h * 3
    print("AM:")
    print(AM)
    AO = 2 * AG + AM
    print("AO: ")
    print(AO)
    V = AG * h
    print("V: ")
    print(V)

if choose == 2:
    a = float(input("Seite a (Hypothenuse): "))
    b = float(input("Seite b (Kathete): "))
    c = float(input("Seite c (Kathete): "))
    hd = float(input("Die entsprechende Höhe: "))
    h = float(input("Höhe vom Körper: "))
    AG = a * hd / 2
    print("AG: ")
    print(AG)

    A1 = a * h
    print("A1: ")
    print(A1)

    A2 = b * h
    print("A2: ")
    print(A2)

    A3 = c * h
    print("A3: ")
    print(A3)

    AM = a + c + b
    print(AM)

    AO = 2 * AG + AM
    print("AO: ")
    print(AO)

    V = AG * h
    print("V: ")
    print(V)

if choose == 3:
    a = float(input("Seite a: "))
    b = float(input("seite b: "))
    c = float(input("Seite c: "))
    d = float(input("Seite d: "))
    ht = float(input("Höhe vom Trapez: "))
    h = float(input("Höhe Vom Körper: "))

    AG = (a + c) / 2 * ht
    print("AG:")
    print(AG)
    a1 = a * h
    print("A1")
    print(a1)
    a2 = b * h
    print("A2")
    print(a2)
    a3 = c * h
    print("A3")
    print(a3)
    a4 = d * h
    print("A4")
    print(a4)

    AM = a1 + a2 + a3 + a4
    print("AM:")
    print(AM)

    AO = 2 * AG + AM
    print("AO: ")
    print(AO)

    V = AG * h
    print("V: ")
    print(V)

input("Enter Drücken")
