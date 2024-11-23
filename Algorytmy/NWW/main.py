def NWD(a,b):
    mniejsza_liczba = a
    if a > b:
        mniejsza_liczba = b
    for i in range(mniejsza_liczba, 0, -1):
        if a % i == 0 and b % i == 0:
            return i


def NWW(a,b):
    return int((a*b)/NWD(a,b)) #Żeby nie było przecinka .0

print(NWW(27,32))