# Szukamy słowa "motyw" (wzorzec) w słowie "lokomotywa" (tekst)

def WyszukiwanieWzorca(tekst, wzorzec):
    if len(wzorzec) > len(tekst): # Sprawdzenie czy przypadkiem wzorzec nie jest dluzszy od samego tekstu
        print("Nie znaleziono wzorca")
        return
    for i in range(0, len(tekst)):
        if len(tekst) - i < len(wzorzec): # Zeby nie wyjsc poza index oraz zeby bezsensu nie sprawdzać np. w słowie lokomotywa wzorca ala
            break

        for j in range(0, len(wzorzec)):
            if(tekst[i+j] != wzorzec[j]): # sprawdzanie po literce czy zgadza się ze wzorcem
                break
            if(j == len(wzorzec)-1):
                print(f"Początek jest pod index {i}")
                return
    print("Nie znaleziono wzorca")

WyszukiwanieWzorca(input("Podaj tekst: "), input("Podaj wzorzec: "))