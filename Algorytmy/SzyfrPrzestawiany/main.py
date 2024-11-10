def szyfrPrzestawiany(nazwa):
    if len(nazwa) > 1:
        szyfrowany_tekst = ""
        for i in range(0, len(nazwa) - 1, 2):
            pierwsza_L = nazwa[i]
            druga_L = nazwa[i + 1]
            szyfrowany_tekst += druga_L + pierwsza_L
        if len(nazwa) % 2 != 0:
            szyfrowany_tekst += nazwa[-1]
    print(szyfrowany_tekst)
szyfrPrzestawiany(input("Podaj tekst do zaszyfrowania: "))
