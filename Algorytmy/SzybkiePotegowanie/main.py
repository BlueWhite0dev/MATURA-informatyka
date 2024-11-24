def potegowanie(a,b): #a^b
    wynik=1
    c=a
    while b>0:
        bit = b % 2
        b = b // 2
        if(bit == 1):
            wynik = wynik * c
        c=c*c
    return wynik

print(potegowanie(2,3))