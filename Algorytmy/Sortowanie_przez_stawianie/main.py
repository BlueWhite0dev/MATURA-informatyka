tab = [8,2,1,9,5]
print(tab)
def sortowanie(tablica):
    i = 1
    while i < len(tablica):
        element = tablica[i]
        j = i-1
        while j >=0 and element < tablica[j]:
            tablica[j+1] = tablica[j]
            j-=1
        tablica[j+1] = element
        i+=1
        print(tab)

sortowanie(tab)
