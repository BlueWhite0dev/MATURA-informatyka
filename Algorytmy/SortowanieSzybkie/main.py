tab = [8,2,1,9,5]

def podziel(tab, start, end):
    wskaznik = tab[end]
    low = start
    high = end - 1
    while True:
        while low <= high and tab[low] <= wskaznik:
            low += 1

        while low <= high and tab[high] >= wskaznik:
            high -= 1

        if low <= high:
            tab[low], tab[high] = tab[high], tab[low] #Zamiana miejscami
        else:
            break
    tab[end], tab[low] = tab[low], tab[end]
    return low

def quickSort(tab, start, end):
    if start < end:
        wskaznik = podziel(tab, start, end)
        quickSort(tab, start, wskaznik-1)
        quickSort(tab, wskaznik+1, end)
        print(tab)

quickSort(tab, 0, len(tab)-1)
print(tab)