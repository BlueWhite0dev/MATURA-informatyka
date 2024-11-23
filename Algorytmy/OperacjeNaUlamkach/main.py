def NWD(a,b):
    while b:
        a,b = b, a%b
    return a

def suma(a,b,c,d):
    NWW = b*d // NWD(b,d)
    e = a * NWW // b+c * NWW // d
    f = NWW
    print(f"{str(e)}/{str(f)}")

licznik_1 = 3
mianownik_1 = 7
licznik_2 = 6
mianownik_2 = 5

suma(licznik_1, mianownik_1, licznik_2, mianownik_2)