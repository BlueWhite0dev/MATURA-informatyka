
def WpisanieLiczb():
    ilosc = int(input("Podaj ilość elementów: "))
    tab = [True for _ in range(ilosc)]
    for i in range(0, ilosc):
        tab[i] = int(input(f"{i+1}. "))
    print(f"Podsumowanie tablicy: {tab}")
    print(Szukaj(tab))

def Szukaj(tablica):
    szukanaLiczba = int(input("Podaj szukaną liczbę: "))
    return szukanaLiczba in tablica

WpisanieLiczb()