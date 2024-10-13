def sortowanie(tablica):
   najmniejsza = 0
   for n in range(0, len(tablica)):
       for mniejsza in range(n, len(tablica)):
           if(tablica[najmniejsza] > tablica[mniejsza]):
            najmniejsza = mniejsza
       przechowywanie = tablica[najmniejsza]
       tablica[najmniejsza] = tablica[n]
       tablica[n] = przechowywanie
   return tablica

dlugosc_tablicy = int(input("Podaj dlugosc tablicy: "))
elementy = [True for _ in range(0, dlugosc_tablicy)]
for index in range(0, dlugosc_tablicy):
    elementy[index] = int(input(f"{index+1}. Podaj element: "))
print(sortowanie(elementy))