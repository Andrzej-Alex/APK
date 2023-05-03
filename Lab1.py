"""
Andrzej Aleksandrowicz
"""

# 1)
"""
teskt = "Emma i ja dostałyśmy instrukcje, by o 9:30 napisać o oficjalnych danych dotyczących zatrudnienia w Wielkiej Brytanii i wysłać nasze wersje do redaktora. Byłam przekonana, że Emma będzie ode mnie szybsza, ale miałam też szczerą nadzieję, że to ja będę lepsza. Twórca Emmy, start-up o nazwie Stealth, nazywa ją „niezależną sztuczną inteligencją” zaprojektowaną, by świadczyć profesjonalne usługi, takie jak badania i analiza. Odkąd w modzie są prognozy, że sztuczna inteligencja (ang. artificial intelligence, AI) zastąpi pracowników biurowych, w tym również dziennikarzy, chciałam to sprawdzić na własnej skórze. Emma rzeczywiście była szybka – dane wysłała w 12 minut. Mi zajęło to 35. Jej wersja była też lepsza, niż się spodziewałam. Fakty się zgadzały, zawarła nawet trafne treści, takie jak możliwość Brexitu (choć podzielała wątpliwą opinię, że wyjście z Unii Europejskiej byłoby niezwykle korzystne dla brytyjskiej gospodarki)."
print("a: ",teskt.count("Emma"))
print("b: ",teskt.upper())
print("c: ",teskt.split(' '))
print("d: ",len(teskt.split('.')))
print("e: ",teskt.split('.')[0])
"""

# 2)
"""
x = int(input("podaj liczbe x: "))
y = int(input("podaj liczbe y: "))
print((2*x)+(5*y))
"""

# 3)
"""
a = input("podaj imie: ")
b = input("podaj nazwisko: ")
c = int(input("podaj wiek: "))
d = input("podaj kierunek studiow: ")
print(f"Jestem {a} {b} mam {c} lat studiuję {d}")
"""
# 4)
"""
liczba1 = 1+2+10+20000001+4+347586970885
liczba2 = 321784560456434534646
print(liczba1 == liczba2)
"""
# 5)
"""
podana1 = int(input("podaj pierwszą liczbę: "))
podana2 = int(input("podaj drugą liczbę: "))
suma_dwoch = (podana1 + podana2) % 2 #1 - nie parzysta /// 0 - parzysta
print(suma_dwoch)
if (suma_dwoch == 0):
    print(f"suma liczb: {podana1} i {podana2} jest parzysta")
else:
    print(f"suma liczb: {podana1} i {podana2} NIE jest parzysta")
"""
# 6)
"""
petla = True
wybor = ""
while petla == True:
    wybor = input(
        "Wybierz tryb kalkulatora wypisując odpowiedni wyraz (Do wyboru jest 'suma', 'roznica', 'iloczyn', 'iloraz', 'potega')\n: ")
    if (wybor == "suma" or wybor == "roznica" or wybor == "iloczyn" or wybor == "iloraz" or wybor == "potega"):
        petla = False
    else:
        print("nieznany tryb, wpisz jeszcze raz")


kalk1 = int(input("podaj pierwszą liczbę: "))
kalk2 = int(input("podaj drugą liczbę: "))
if (wybor == "suma"):
    print(kalk1 + kalk2)
elif (wybor == "roznica"):
    print(kalk1 - kalk2)
elif (wybor == "iloczyn"):
    print(kalk1 * kalk2)
elif (wybor == "iloraz"):
    print(kalk1 / kalk2)
elif (wybor == "potega"):
    print(kalk1 ** kalk2)
"""

# 7)
"""
dowolnyx = int(input("podaj dowolnego x: "))

print((dowolnyx > 1 and dowolnyx < 13))
print((dowolnyx != 5 or dowolnyx < 0))
"""

