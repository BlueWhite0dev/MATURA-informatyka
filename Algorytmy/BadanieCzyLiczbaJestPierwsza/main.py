from math import sqrt

n = int(input("Podaj liczbę: "));
def czy_pierwsza():
    if n < 2:
        return False
    else:
        for i in range(2, int(sqrt(n))+1): # od 2 do pierwiastek n
            if n % i == 0:
                return False
        return True
print(czy_pierwsza())

def sito_Eratostenesa():
    numbers = [True for _ in range(n)]
    liczby_pierwsze = []
    for i in range(len(numbers)):
        if i < 2:
            numbers[i] = False
        else:
            if numbers[i]:
                liczby_pierwsze.append(i)
                for j in range(i, len(numbers), i):
                    numbers[j] = False
    return  liczby_pierwsze

print(sito_Eratostenesa())