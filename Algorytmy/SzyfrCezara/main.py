klucz = "abcdefghijklmnopqrstuvwxyz"

def szyfrCezara(slowo, przesuniecie):
    zaszyfrowane_slowo = ""
    for znak in range(0, len(slowo)):
        litera = slowo[znak]
        if litera == " ":
            zaszyfrowane_slowo += " "
            continue #Przechodzi do następnej litery nie kończącz całkowicie pętli
        zaszyfrowany_index = klucz.index(litera.lower()) - przesuniecie #Zamiana dużych liter na małą
        if slowo[znak].isupper():
            zaszyfrowane_slowo += klucz[zaszyfrowany_index].upper()
        else:
            zaszyfrowane_slowo += klucz[zaszyfrowany_index]


    print(zaszyfrowane_slowo)

szyfrCezara("Ala ma Kota",3)