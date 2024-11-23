tablica = [2,4,1,6,0,3,7,5]

def minimum(zbior):
    min = zbior[0]
    for n in range (1, len(zbior)):
        if(min > zbior[n]):
            min = zbior[n]
    return min

def maksimum(zbior):
    max = zbior[0]
    for n in range (1, len(zbior)):
        if(max < zbior[n]):
            max = zbior[n]
    return max
print(minimum(tablica))
print(maksimum(tablica))