import math

def TworzenieTablicy():
    iloscElementow = int(input("Podaj ilosc elementów: "))
    tab = [True for _ in range(0, iloscElementow)]
    for i in range(0, iloscElementow):
        tab[i] = int(input(f"{i+1}. "))

    print(f"Podsumowanie tablicy: {tab}")
    n = int(input("Szukana liczba: "))
    Wyszukiwanie(tab, n)
def Wyszukiwanie(tablica, szukana):
    iloscKrokow = 0
    l = 0
    p = len(tablica)-1
    s = math.floor(int((l + p) / 2)) #zaokrąglamy zawsze w dół, można również zamiast math.floor zastąpić '/' na '//'
    while True:
        iloscKrokow+=1
        print(f"{iloscKrokow}. krok")
        if(tablica[l] > szukana and tablica[p] < szukana):
            print("Nie ma w tablicy tej liczby")
            break
        elif(tablica[s] == szukana):
            print(f"Znajduje się pod indexem {s}")
            break
        elif(tablica[s] > szukana): #Jeżeli środek jest za duży to przesuwamy prawą stronę o 1 mniejszą wartość środka
            p = s-1
        elif(tablica[s] < szukana): #Jeżeli środek jest za mały to przesuwamy lewą stronę o 1 większą wartość środka
            l = s+1

        #Wyznaczamy nowy środek
        s = math.floor(int((l + p) / 2))

TworzenieTablicy()