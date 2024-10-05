#Palindrom - wyraz, który czytany z lewej do prawej jest taki sam jak z prawej do lewej, np. kajak

def palindrom(tekst):
    spak = ""
    for i in range(0, len(tekst)):
        spak += tekst[len(tekst)-i-1]
    if tekst.lower() == spak.lower(): #Zamieniamy wszystko na małe litery, bo inaczej słowo Kajak zamieni na kajaK, czego nie chcemy
        print("Wyraz jest palindromem")
    else:
        print("Wyraz nie jest palindromem")

palindrom(input("Podaj wyraz do sprawdzenia: "))

