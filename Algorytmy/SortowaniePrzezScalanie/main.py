tab = [8, 2, 1, 9, 5]

def mergeSort(tab):
    if len(tab) > 1: #Bez sensu byłoby sortować tablicę 1 elementową, cn?
        mid = len(tab) // 2 #Bez części ułamkowej 5//2 = 2
        LewaStrona = tab[:mid] #Od elementu pierwszego do środka
        PrawaStrona = tab[mid:] #Od środka do ostatniego elementu
        print(f"Lewa: {LewaStrona}\nPrawa: {PrawaStrona}")
        mergeSort(LewaStrona)
        mergeSort(PrawaStrona)

        i = j = k = 0 #Zmienne pomocnicze

        while i < len(LewaStrona) and j < len(PrawaStrona):
            if LewaStrona[i] < PrawaStrona[j]:
                tab[k] = LewaStrona[i]
                i += 1
            else:
                tab[k] = PrawaStrona[j]
                j+=1
            k += 1

        while i < len(LewaStrona):
            tab[k] = LewaStrona[i]
            i +=1
            k +=1

        while j < len(PrawaStrona):
            tab[k] = PrawaStrona[j]
            j += 1
            k += 1
        print(f"_PO: {tab}")

mergeSort(tab)