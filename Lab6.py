

# # Definiowanie funkcji dla każdej operacji
# def dodaj(a, b):
#     return a + b
#
# def odejmij(a, b):
#     return a - b
#
# def pomnoz(a, b):
#     return a * b
#
# def podziel(a, b):
#     return a / b
#
# # Prosty interfejs użytkownika w konsoli
# while True:
#     print("Wybierz operację:")
#     print("1.Dodaj")
#     print("2.Odejmij")
#     print("3.Pomnóż")
#     print("4.Podziel")
#     print("5.Zakończ")
#
#     wybor = int(input("Podaj numer operacji (1/2/3/4/5): "))
#
#     if wybor == 5:
#         break
#
#     num1 = float(input("Podaj pierwszą liczbę: "))
#     num2 = float(input("Podaj drugą liczbę: "))
#
#     if wybor == 1:
#         print("Wynik: ", dodaj(num1, num2))
#     elif wybor == 2:
#         print("Wynik: ", odejmij(num1, num2))
#     elif wybor == 3:
#         print("Wynik: ", pomnoz(num1, num2))
#     elif wybor == 4:
#         print("Wynik: ", podziel(num1, num2))
#     else:
#         print("Nieznana operacja")
#

# ------

# # Importowanie wymaganych modułów
# from math import pow
#
# # Proste funkcje do wykonania operacji matematycznych
#
# def dodaj(a, b):
#     """
#     Funkcja do dodawania dwóch liczb
#
#     Args:
#     a: pierwsza liczba
#     b: druga liczba
#
#     Returns:
#     Suma a i b
#     """
#     return a + b
#
# def odejmij(a, b):
#     """
#     Funkcja do odejmowania dwóch liczb
#
#     Args:
#     a: pierwsza liczba
#     b: druga liczba
#
#     Returns:
#     Różnica a i b
#     """
#     return a - b
#
# def pomnoz(a, b):
#     """
#     Funkcja do mnożenia dwóch liczb
#
#     Args:
#     a: pierwsza liczba
#     b: druga liczba
#
#     Returns:
#     Iloczyn a i b
#     """
#     return a * b
#
# def podziel(a, b):
#     """
#     Funkcja do dzielenia dwóch liczb
#
#     Args:
#     a: pierwsza liczba
#     b: druga liczba
#
#     Returns:
#     Iloraz a i b
#     """
#     return a / b
#
# def kalkulator(operacja, a, b):
#     """
#     Funkcja wyższego rzędu zarządzająca operacjami matematycznymi
#
#     Args:
#     operacja: funkcja reprezentująca operację matematyczną
#     a: pierwsza liczba
#     b: druga liczba
#
#     Returns:
#     Wynik operacji na a i b
#     """
#     return operacja(a, b)
#
#
# # Testowanie funkcji kalkulatora
# print(kalkulator(dodaj, 5, 3))  # Wyświetli 8
# print(kalkulator(odejmij, 5, 3))  # Wyświetli 2
# print(kalkulator(pomnoz, 5, 3))  # Wyświetli 15
# print(kalkulator(podziel, 5, 3))  # Wyświetli 1.6666666666666667
#
# ----------------------------

# import math_operations as mo
#
#
# def kalkulator():
#     """
#     Zarządza wszystkimi operacjami matematycznymi z modułu math_operations.
#     """
#     operacje = {
#         1: mo.dodaj,
#         2: mo.odejmij,
#         3: mo.pomnoz,
#         4: mo.podziel,
#     }
#
#     operacje_string = ['dodaj', 'odejmij', 'pomnoz', 'podziel']
#
#     while True:
#         print("\nWybierz operację: ")
#         for i, oper in enumerate(operacje_string, start=1):
#             print(f"{i}. {oper}")
#
#         print("5. Wyjdź")
#
#         wybor = input("Podaj numer operacji (1/2/3/4/5): ")
#
#         if wybor == '5':
#             break
#
#         a = float(input("Podaj pierwszą liczbę: "))
#         b = float(input("Podaj drugą liczbę: "))
#
#         operacja = operacje.get(int(wybor))
#         if operacja:
#             try:
#                 wynik = operacja(a, b)
#                 print(f"Wynik: {wynik}")
#             except Exception as e:
#                 print(f"Wystąpił błąd: {e}")
#         else:
#             print("Nieznana operacja")
#
#
# if __name__ == "__main__":
#     kalkulator()
# ----------------

# import math_operations as mo
#
#
# def kalkulator(lista_danych):
#     """
#     Zarządza wszystkimi operacjami matematycznymi z modułu math_operations.
#
#     Args:
#     lista_danych: Lista czteroelementowa zawierająca dwie liczby do obliczeń,
#                   numer operacji do wykonania (1 - dodawanie, 2 - odejmowanie, 3 - mnożenie, 4 - dzielenie)
#                   i decyzję o kontynuacji działania kalkulatora (0 - zakończ działanie, 1 - kontynuuj).
#     """
#     operacje = {
#         1: mo.dodaj,
#         2: mo.odejmij,
#         3: mo.pomnoz,
#         4: mo.podziel,
#     }
#
#     # Dane do obliczeń
#     a = lista_danych[0]
#     b = lista_danych[1]
#
#     # Wybór operacji
#     wybor = lista_danych[2]
#
#     # Wybór kontynuacji działania kalkulatora
#     kontynuacja = lista_danych[3]
#
#     operacja = operacje.get(int(wybor))
#     if operacja:
#         try:
#             wynik = operacja(a, b)
#             print(f"Wynik: {wynik}")
#         except Exception as e:
#             print(f"Wystąpił błąd: {e}")
#     else:
#         print("Nieznana operacja")
#
#     # Kontynuacja działania kalkulatora jeżeli kontynuacja = 1
#     if kontynuacja == 1:
#         kalkulator(lista_danych)
#
#
# if __name__ == "__main__":
#     lista_danych = [10, 5, 1, 1]
#     kalkulator(lista_danych)


# # Zadanie 1
# class Egzaminy:
#  typyEgz = ['Android', 'Python', 'JAVA', 'JavaEE']
#  nrTyp = 0
#
#
#    def __init__(self):
#     self.typyEgz[self.nrTyp]
#
#
#    def ustawEgz(self, wpisanyNumer):
#     self.nrTyp = wpisanyNumer
#
#    def wyswietlEgz(self):
#
#        print('Ustawiony egzamin to: ' + self.typyEgz[self.nrTyp])
#
#  mojEgzaminy1 = Egzaminy()
#  mojEgzaminy1.wyswietlEgz()
#  mojEgzaminy1.ustawEgz(3)
#  mojEgzaminy1.wyswietlEgz()
#
#
# ----
# class Egzaminy:
#   typyEgz = ['Android', 'Python', 'JAVA', 'JavaEE']
#   nrTyp = 0
#
#   def __init__(self):
#     self.typyEgz[self.nrTyp]
#
#   def ustawEgz(self, wpisanyNumer):
#     self.nrTyp = wpisanyNumer
#
#   def wyswietlEgz(self):
#       print('Ustawiony egzamin to: ' + self.typyEgz[self.nrTyp])
# ---
#       mojEgzaminy1 = Egzaminy()
#       mojEgzaminy1.wyswietlEgz()
#       mojEgzaminy1.ustawEgz(3)
#       mojEgzaminy1.wyswietlEgz()
#
#
# # # Zadanie 2
# class Wakacje:
#     imie = '-'
#     nazwisko = '-'
#     wiek = '-'
#     liczbaOsob = '-'
#     transport = '-'
#     dzieci = '-'
#
#     def pytanieImieNazwisko(self):
#         imie = input('imie: ')
#         nazwisko = input('nazwisko: ')
#         self.imie = imie
#         self.nazwisko = nazwisko
#
#     def pytanieWiek(self):
#         wiek = input('wiek: ')
#         self.wiek = wiek
#
#     def pytanieLiczbaOsob(self):
#         liczbaOsob = input('liczba osob: ')
#         self.liczbaOsob = liczbaOsob
#
#     def transport(self):
#         transport = input('transport: ')
#         self.transport = transport
#
#     def liczbaDzieci(self):
#         dzieci = input('liczba dzieci: ')
#         self.dzieci = dzieci
#
#     def wyswietlAnkiete(self):
#         print('\nImię: ' + self.imie + '\nNazwisko: ' + self.nazwisko + '\nWiek: ' + self.wiek + '\nliczbaOsob: ' + self.liczbaOsob + '\nTransport: ' + self.transport + '\nliczbaDzieci: ' + self.dzieci)
#
# Dict = []
# wakacje1 = Wakacje()
# wakacje1.pytanieImieNazwisko()
# wakacje1.pytanieWiek()
# wakacje1.pytanieLiczbaOsob()
# wakacje1.transport()
# wakacje1.liczbaDzieci()
# Dict.append(wakacje1)
#
# wakacje2 = Wakacje()
# wakacje2.pytanieImieNazwisko()
# wakacje2.pytanieWiek()
# wakacje2.pytanieLiczbaOsob()
# wakacje2.transport()
# wakacje2.liczbaDzieci()
# Dict.append(wakacje2)
#
# print(Dict[1].wyswietlAnkiete())
#
# class Osoba:
#     liczba_osob = 0
#
#     def __init__(self, plec='unknown'):
#         self.plec = plec
#         Osoba.liczba_osob += 1
#
#     @staticmethod
#     def print_plec(plec):
#         print(plec)
#
#     @staticmethod
#     def get_liczba_osob():
#         return Osoba.liczba_osob
#
#
# class Kobieta(Osoba):
#     def __init__(self):
#         super().__init__('female')
#         Osoba.print_plec(self.plec)
#
#
# class Mezczyzna(Osoba):
#     def __init__(self):
#         super().__init__('male')
#         Osoba.print_plec(self.plec)

#
# Moduł
# "operations.py":
#
# python
# Copy
# code
#
#
# def add(a, b):
#     return a + b
#
#
# def subtract(a, b):
#     return a - b
#
#
# def multiply(a, b):
#     return a * b
#
#
# def divide(a, b):
#     if b != 0:
#         return a / b
#     else:
#         raise ZeroDivisionError("Cannot divide by zero.")
#
#
# Moduł
# "calculator.py":
#
# python
# Copy
# code
# import operations
#
#
# def perform_operation(operation, operands):
#     if not isinstance(operands, list) or len(operands) < 2:
#         raise ValueError("Operands should be a list with a minimum of two elements.")
#
#     if not all(isinstance(num, (int, float)) for num in operands):
#         raise ValueError("Operands should be integers or floats.")
#
#     if operation == 'add':
#         return operations.add(*operands)
#     elif operation == 'subtract':
#         return operations.subtract(*operands)
#     elif operation == 'multiply':
#         return operations.multiply(*operands)
#     elif operation == 'divide':
#         return operations.divide(*operands)
#     else:
#         raise ValueError("Invalid operation.")
#
#
# Przykład
# użycia
# kalkulatora:
#
# python
# Copy
# code
# x = [1, 3, 5, 6]
# y = [2, 11, 5]
#
# try:
#     result = calculator.perform_operation('add', x)
#     print("Addition result:", result)
# except ValueError as e:
#     print("Error:", e)
#
# try:
#     result = calculator.perform_operation('subtract', y)
#     print("Subtraction result:", result)
# except ValueError as e:
#     print("Error:", e)
#
# try:
#     result = calculator.perform_operation('multiply', [2, 'abc'])
#     print("Multiplication result:", result)
# except ValueError as e:
#     print("Error:", e)
#
# try:
#     result = calculator.perform_operation('divide', [10, 0])
#     print("Division result:", result)
# except ValueError as e:
#     print("Error:", e)
# Wynik:
#
# yaml
# Copy
# code
# Addition
# result: 15
# Subtraction
# result: -4
# Error: Operands
# should
# be
# integers or floats.
# Error: Cannot
# divide
# by
# zero.
# Dokumentacja
# modułu
# "operations.py":
#
# python
# Copy
# code
#
#
# def add(a, b):
#     """
#     Adds two numbers.
#
#     Args:
#         a (int or float): First number.
#         b (int or float): Second number.
#
#     Returns:
#         int or float: Sum of the two numbers.
#     """
#     return a + b
#
#
# def subtract(a, b):
#     """
#     Subtracts two numbers.
#
#     Args:
#         a (int or float): First number.
#         b (int or float): Second number.
#
#     Returns:
#         int or float: Difference between the two numbers.
#     """
#     return a - b
#
#
# def multiply(a, b):
#     """
#     Multiplies two numbers.
#
#     Args:
#         a (int or float): First number.
#         b (int or float): Second number.
#
#     Returns:
#         int or float: Product of the two numbers.
#     """
#     return a * b
#
#
# def divide(a, b):
#     """
#     Divides two numbers.
#
#     Args:
#         a (int or float): First number.
#         b (int or float): Second number.
#
#     Returns:
#         int or float: Quotient of the two numbers.
#
#     Raises:
#         ZeroDivisionError: If the second number is zero.
#     """
#     if b != 0:
#         return a / b
#     else
#
#         def add(a, b):
#             return a + b
#
#         def subtract(a, b):
#             return a - b
#
#         def multiply(a, b):
#             return a * b
#
#         def divide(a, b):
#             if b != 0:
#                 return a / b
#             else:
#                 raise ZeroDivisionError("Cannot divide by zero.")
#
#
# import operations
#
#
# def perform_operation(operation, operands):
#     if not isinstance(operands, list) or len(operands) < 2:
#         raise ValueError("Operands should be a list with a minimum of two elements.")
#
#     if not all(isinstance(num, (int, float)) for num in operands):
#         raise ValueError("Operands should be integers or floats.")
#
#     if operation == 'add':
#         return operations.add(*operands)
#     elif operation == 'subtract':
#         return operations.subtract(*operands)
#     elif operation == 'multiply':
#         return operations.multiply(*operands)
#     elif operation == 'divide':
#         return operations.divide(*operands)
#     else:
#         raise ValueError("Invalid operation.")
#
# x = [1, 3, 5, 6]
# y = [2, 11, 5]
#
# try:
#     result = calculator.perform_operation('add', x)
#     print("Addition result:", result)
# except ValueError as e:
#     print("Error:", e)
#
# try:
#     result = calculator.perform_operation('subtract', y)
#     print("Subtraction result:", result)
# except ValueError as e:
#     print("Error:", e)
#
# try:
#     result = calculator.perform_operation('multiply', [2, 'abc'])
#     print("Multiplication result:", result)
# except ValueError as e:
#     print("Error:", e)
#
# try:
#     result = calculator.perform_operation('divide', [10, 0])
#     print("Division result:", result)
# except ValueError as e:
#     print("Error:", e)

import math

def add(a, b):
    """
    Dodaje dwie liczby.

    Argumenty:
        a: Pierwsza liczba.
        b: Druga liczba.

    Zwraca:
        Sumę dwóch liczb.
    """
    return a + b

def subtract(a, b):
    """
    Odejmuje dwie liczby.

    Argumenty:
        a: Pierwsza liczba.
        b: Druga liczba.

    Zwraca:
        Różnica między dwiema liczbami.
    """
    return a - b

def multiply(a, b):
    """
    Mnoży dwie liczby.

    Argumenty:
        a: Pierwsza liczba.
        b: Druga liczba.

    Zwraca:
        Iloczyn dwóch liczb.
    """
    return a * b

def divide(a, b):
    """
    Dzieli dwie liczby.

    Argumenty:
        a: Pierwsza liczba.
        b: Druga liczba.

    Zwraca:
        Iloraz dwóch liczb.
    """
    return math.truediv(a, b)

def calculator(operacja, a, b):
    """
    Wykonuje operację matematyczną na dwóch liczbach.

    Argumenty:
        operation: Operacja do wykonania.
        a: Pierwsza liczba.
        b: Druga liczba.

    Returns:
        Wynik operacji.

    Podnosi:
        ValueError: Jeśli operacja nie jest obsługiwana.
    """
    operations = {
        'add': dodawanie,
        'subtract': odejmowanie,
        'multiply': mnożenie,
        'divide': dziel
    }

    func = operations.get(operation)
    if func:
        return func(a, b)
    else:
        raise ValueError("Nieprawidłowa operacja")

# Przykładowe użycie
result = calculator('add', 5, 3)
print(result) # Wynik: 8