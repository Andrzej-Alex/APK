"""
Andrzej Aleksandrowicz Laboratorium 2
"""

"""
#Zadanie 1
"""
while True:
    x = int(input("Wprowadź pierwszą liczbę: "))
    y = int(input("Wprowadź drugą liczbę: "))
    if x == 0 or y == 0:
        print("Zatrzymanie programu z powodu: x lub y jest ZEREM")
        break
    product = x * y
    print(f"{x} * {y} = {product}")
    print("Jeszcze raz? (t/n)")
    answer = input()
    if answer == "n":
        print("KONIEC PROGRAMU")

"""
#Zadanie 2
"""
imie = "JAN"
nazwisko = "KOWALSKI"
pin = 24

while True:
    try:
        input_pin = int(input("Enter pin: "))
        if input_pin == pin:
            print("Welcome:", imie, nazwisko)
            break
        else:
            print("Wrong pin!")
    except ValueError:
        print("Only numbers allowed!")

"""
#Zadanie 3
"""

x_input = int(input("Wpisz pierwszą liczbę: "))	-		x
y_input = int(input("Wpisz drugą liczbę: "))	-		y
def calculate_newton(x, y):
    """Oblicza wartość współczynnika Newtona dla danych liczb.

    Args:
        x (int): Pierwsza liczba.
        y (int): Druga liczba.

    Returns:
        float: Wartość współczynnika Newtona.

    Raises:
        ValueError: Jeśli x lub y są mniejsze od zera.
        ValueError: Jeśli y jest większe od x.
    """
    if x < 0 or y < 0:
        raise ValueError("Liczby muszą być większe lub równe zero.")
    if y > x:
        raise ValueError("Druga liczba nie może być większa od pierwszej liczby.")

    return math.factorial(x) / (math.factorial(y) * math.factorial(x - y))

print(calculate_newton(x_input, y_input))

"""
#Zadanie 4
# ########################## Task 4
# # Write a script to filter out only the even items from a list (i.e. made from range(1, 100))
# # using filter() and lambda functions.
# #  The numbers obtained should be printed in a comma-separated sequence on a single line.
"""
numbers = filter(lambda x: x % 2 == 0, range(1, 101))
result = ', '.join(map(str, numbers))
print(result)

"""
#Zadanie 5
######################### Task 5
#### Write a script, using reduce(), which will multiply elements in range (1, 100)
"""
# importing functools for reduce()
import functools
result = reduce(lambda x, y: x * y, range(1, 101))
print(result)



"""
# Zadanie 6
"""
text = 'Wczytywanie do komputera tekstów, ilustracji, fotografii, itp. jest ' \
       'możliwe dzięki urządzeniom zewnętrznym zwanym skanerami. Skaner to ' \
       'urządzenie umożliwiające wprowadzenie do komputera grafiki i tekstu. ' \
       'Dzięki zamianie skanowanej płaszczyzny na postać cyfrową może ona zostać ' \
       'wyświetlona na ekranie monitora i zapisana na dysku w odpowiednim formacie ' \
       'oraz może zostać poddana komputerowej obróbce. Skanery dzielimy na dwie podstawowe ' \
       'grupy: ręczne (np. czytniki kodów paskowych) oraz stacjonarne. Najpopularniejszym ' \
       'typem skanerów są skanery stacjonarne płaskie, które umożliwiają skanowanie ' \
       'dokumentów o formacie A3 lub A4 i ich pochodnych. Są one podłączane do ' \
       'komputerów przez port równoległy, uniwersalną magistralę szeregową lub sterownik SCSI.'

keyList = []
keyList.append("komputera")
keyList.append("skaner")
keyList.append(input("KEY nr 1: "))
keyList.append(input("KEY nr 2: "))
keyList.append(input("KEY nr 3: "))

def keysCount(txt, lst):
    count = sum(txt.count(n) for n in lst)
    return count

print(keysCount(text, keyList))

"""
# Zadanie 7
"""
def ZdanieRozdziel(x, tOrF=True):
    text = input("Wpisz text: ")
    textSplit = text.split(x)
    print(textSplit)
    if tOrF:
        print(text.count(x))
        print(text.count(" ") + 1)


ZdanieRozdziel(",")

"""
# Zadanie 8
"""
import datetime

class Product:
    def __init__(self, name, quantity, date):
        self.name = name
        self.quantity = quantity
        self.date = date

product_list = []

while True:
    option = input("Wybierz: 1 - Dodaj nowy towar | 2 - Wyjdz z programu\n")

    if option == "1":
        towar = input("Wybierz towar: ")
        ilosc = input("Ilość: ")
        base = datetime.today()
        product_list.append(Product(towar, ilosc, base))
        print("Towar dodany do magazynu!")

        for product in product_list:
            print(f"{product.name}: ilość - {product.quantity} | {product.date}")

    elif option == "2":
        break

"""
# Zadanie 9
"""
W pliku pole_prostokata.py:

python
Copy code
def oblicz_pole_prostokata(a, b):
    return a * b
W pliku pole_trojkata.py:

python
Copy code
def oblicz_pole_trojkata(a, h):
    return (a * h) / 2
W pliku globals.py:

python
Copy code
kwadrat = 1
prostokat = 1
trojkat = 1
W pliku pola.py:

python
Copy code
from pole_prostokata import oblicz_pole_prostokata
from pole_trojkata import oblicz_pole_trojkata
import globals

def oblicz_pole_figury(typ, a, b=0):
    if typ == "prostokat":
        if a == 0:
            a = globals.prostokat
        if b == 0:
            b = globals.prostokat
        return oblicz_pole_prostokata(a, b)
    elif typ == "kwadrat":
        if a == 0:
            a = globals.kwadrat
        return a * a
    elif typ == "trojkat":
        if a == 0:
            a = globals.trojkat
        if b == 0:
            b = globals.trojkat
        return oblicz_pole_trojkata(a, b)
    else:
        return "Nieznany typ figury"

"""
# Zadanie 10
"""
def pole_prostokata(a, b):
    return a * b

def pole_trojkata(a, h):
    return (a * h) / 2

def dekorator_oblicz_pole_figury(funkcja):
    def wewnetrzna(*args, **kwargs):
        if "typ" in kwargs:
            typ = kwargs["typ"]
            del kwargs["typ"]
            if typ == "kwadrat":
                return args[0] * args[0]
        return funkcja(*args, **kwargs)
    return wewnetrzna

@dekorator_oblicz_pole_figury
def oblicz_pole_figury(a, b=0):
    return pole_prostokata(a, b)

print(oblicz_pole_figury(2, 3))  # Oblicza pole prostokąta
print(oblicz_pole_figury(2, h=3))  # Oblicza pole trójkąta
print(oblicz_pole_figury(2, typ="kwadrat"))  # Oblicza pole kwadratu

"""
# Zadanie 11
"""
"""
Punkt A):
"""
def logowanie(user='edek2003', password='Wsx123'):
    print(f"Logowanie użytkownika: {user}, hasło: {password}")

def dekorator_dodaj_pola(funkcja):
    def wewnetrzna(*args, **kwargs):
        kwargs['host'] = 'localhost'
        kwargs['port'] = 8080
        return funkcja(*args, **kwargs)
    return wewnetrzna

logowanie = dekorator_dodaj_pola(logowanie)
logowanie()

"""
Punkt B): 
"""

def logowanie(user='edek2003', password='Wsx123', **kwargs):
    print(f"Logowanie użytkownika: {user}, hasło: {password}")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

def dekorator_dodaj_pola(funkcja):
    def wewnetrzna(*args, **kwargs):
        dodatkowe_pola = {'data_base': 'https://pl.wikipedia.org'}
        kwargs.update(dodatkowe_pola)
        return funkcja(*args, **kwargs)
    return wewnetrzna

logowanie = dekorator_dodaj_pola(logowanie)
logowanie(host='localhost', port=8080)

