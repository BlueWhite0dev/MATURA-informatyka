def Sortowanie_Babelkowe(tablica):
    posortowane = False
    while posortowane == False:
        for n in range(0, len(tablica)-1):
            if(tablica[n] > tablica[n+1]):
                posortowane = False
                przechowywanie = tablica[n+1]
                tablica[n+1] = tablica[n]
                tablica[n] = przechowywanie
                n -=1
            else:
                if(n==0):
                    posortowane = True
    return tablica

dlugosc_tablicy = int(input("Podaj dlugosc tablicy: "))
elementy = [True for _ in range(0, dlugosc_tablicy)]
for index in range(0, dlugosc_tablicy):
    elementy[index] = int(input(f"{index+1}. Podaj element: "))
print(Sortowanie_Babelkowe(elementy))