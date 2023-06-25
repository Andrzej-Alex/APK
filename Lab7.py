# Zadanie1
# Utwórz program kalkulator (operacje: dodawanie, odejmowanie, mnożenie, dzielenie dwu liczb),
# programuj w paradygmacie strukturalnym
# a) wariant bez obsługi wyjątków

# def calculator(operation, num1, num2):
#     """Wykonuje wybraną operację matematyczną na dwóch liczbach.
#
#     Args:
#         operation (str): Operacja do wykonania. Możliwości: 'dodaj', 'odejmij', 'pomnóż' lub 'podziel'.
#         num1, num2 (int | float): Liczby na których wykonujemy operację.
#
#     """
#     if operation == 'dodaj':
#         result = num1 + num2
#     elif operation == 'odejmij':
#         result = num1 - num2
#     elif operation == 'pomnóż':
#         result = num1 * num2
#     elif operation == 'podziel':
#         result = num1 / num2
#     else:
#         result = 'Błąd: nieprawidłowa operacja.'
#
#     print(result)
#
#
# # Test funkcji:
# calculator('dodaj', 10, 20)  # Wyjście: 30
# calculator('odejmij', 10, 20)  # Wyjście: -10
# calculator('pomnóż', 10, 2)  # Wyjście: 20
# calculator('podziel', 10, 2)  # Wyjście: 5.0

# Zadanie2
## ## **Zadanie 2**
# Utwórz program kalkulator (operacje: dodawanie, odejmowanie, mnożenie, dzielenie dwu liczb), programuj w paradygmacie funkcyjnym
#
# a) wariant bez obsługi wyjątków
#
# **Note:**
# * utwórz 4 funkcje proste dla poszczególnych operacji matematycznych
# * utwórz 1 funkcję wyższego rzędu calculator() która zarządza wszystkimi operacjami
# * użyj funkcji wbudowanych, pakietu math
# * wykonaj dokumentację dla funkcji

# import math
#
# def dodaj(num1, num2):
#     """Dodaje dwie liczby.
#
#     Args:
#         num1, num2 (int lub float): Liczby do dodania.
#
#     Returns:
#         Suma num1 i num2.
#     """
#     return math.fsum([num1, num2])
#
# def odejmij(num1, num2):
#     """Odejmuje drugą liczbę od pierwszej.
#
#     Args:
#         num1, num2 (int lub float): Liczby do operacji.
#
#     Returns:
#         Wynik odejmowania num2 od num1.
#     """
#     return math.fsum([num1, -num2])
#
# def pomnóż(num1, num2):
#     """Mnoży dwie liczby.
#
#     Args:
#         num1, num2 (int lub float): Liczby do pomnożenia.
#
#     Returns:
#         Iloczyn num1 i num2.
#     """
#     return math.prod([num1, num2])
#
# def podziel(num1, num2):
#     """Dzieli pierwszą liczbę przez drugą.
#
#     Args:
#         num1, num2 (int lub float): Liczby do operacji.
#
#     Returns:
#         Wynik dzielenia num1 przez num2.
#     """
#     return divmod(num1, num2)[0]  # divmod zwraca krotkę (iloraz, reszta), więc bierzemy tylko iloraz
#
# def calculator(func, num1, num2):
#     """Wykonuje wybraną operację matematyczną na dwóch liczbach.
#
#     Funkcja wyższego rzędu, która przyjmuje jako argumenty funkcję (dodaj, odejmij, pomnóż, podziel)
#     oraz dwie liczby.
#
#     Args:
#         func (function): Funkcja do wykonania.
#         num1, num2 (int lub float): Liczby na których wykonujemy operację.
#
#     Returns:
#         Wynik działania funkcji func na num1 i num2.
#     """
#     return func(num1, num2)
#
#
# # Testy funkcji:
# print(calculator(dodaj, 10, 20))  # Wyjście: 30.0
# print(calculator(odejmij, 10, 20))  # Wyjście: -10.0
# print(calculator(pomnoz, 10, 2))  # Wyjście: 20
# print(calculator(podziel, 10, 2))  # Wyjście: 5.0

# Zadanie3
# a) wariant z obsługą wyjątków
#
# Note:
#
# utwórz 2 moduły: pierwszy zawiera 4 funkcje proste dla poszczególnych operacji matematycznych drugi moduł zawiera 1 funkcję która zarządza wszystkimi operacjami
# wykonaj dokumentację dla 1 modułu

# Moduł 1 (operacje.py):
import math

def dodaj(num1, num2):
    """Dodaje dwie liczby.

    Args:
        num1, num2 (int lub float): Liczby do dodania.

    Returns:
        Suma num1 i num2.

    Raises:
        TypeError: Jeżeli num1 lub num2 nie jest liczbą.
    """
    if isinstance(num1, (int, float)) and isinstance(num2, (int, float)):
        return math.fsum([num1, num2])
    else:
        raise TypeError('Both num1 and num2 must be numbers.')

def odejmij(num1, num2):
    """Odejmuje drugą liczbę od pierwszej.

    Args:
        num1, num2 (int lub float): Liczby do operacji.

    Returns:
        Wynik odejmowania num2 od num1.

    Raises:
        TypeError: Jeżeli num1 lub num2 nie jest liczbą.
    """
    if isinstance(num1, (int, float)) and isinstance(num2, (int, float)):
        return math.fsum([num1, -num2])
    else:
        raise TypeError('Oba parametry muszą być liczbami')

def pomnoz(num1, num2):
    """Mnoży dwie liczby.

    Args:
        num1, num2 (int lub float): Liczby do pomnożenia.

    Returns:
        Iloczyn num1 i num2.

    Raises:
        TypeError: Jeżeli num1 lub num2 nie jest liczbą.
    """
    if isinstance(num1, (int, float)) and isinstance(num2, (int, float)):
        return math.prod([num1, num2])
    else:
        raise TypeError('Oba parametry muszą być liczbami')

def podziel(num1, num2):
    """Dzieli pierwszą liczbę przez drugą.

    Args:
        num1, num2 (int lub float): Liczby do operacji.

    Returns:
        Wynik dzielenia num1 przez num2.

    Raises:
        TypeError: Jeżeli num1 lub num2 nie jest liczbą.
        ZeroDivisionError: Jeżeli num2 jest zerem.
    """
    if isinstance(num1, (int, float)) and isinstance(num2, (int, float)):
        if num2 != 0:
            return divmod(num1, num2)[0]
        else:
            raise ZeroDivisionError('Nie można dzielić przez ZERO')
    else:
        raise TypeError('Oba parametry muszą być liczbami')

# Moduł 2 (calculator.py):

from operations import dodaj, odejmij, pomnoz, podziel

def calculator(func, num1, num2):
    """Wykonuje wybraną operację matematyczną na dwóch liczbach.

    Funkcja wyższego rzędu, która przyjmuje jako argumenty funkcję (dodaj, odejmij, pomnóż, podziel)
    oraz dwie liczby.

    Args:
        func (function): Funkcja do wykonania.
        num1, num2 (int lub float): Liczby na których wykonujemy operację.

    Returns:
        Wynik działania funkcji func na num1 i num2.
    """
    return func(num1, num2)

# Testy funkcji:
print(calculator(dodaj, 10, 20))  # Wyjście: 30.0
print(calculator(odejmij, 10, 20))  # Wyjście: -10.0
print(calculator(pomnoz, 10, 2))  # Wyjście: 20
print(calculator(podziel, 10, 2))  # Wyjście: 5.0





# import math
#
# def printIntro():
#     print("This is a simple calc.")
# print("Select an operation:\n1) Add\n2) Subtract\n3) Divide\n4) Multiply")
#
# while True:
#     operator = input("Enter your choice of + - / *: \n")
#
#     if operator in('+', '-', '/', '*'):
#         #continue asking for numbers until user ends
#         #store numbers in an array
#
#         list = []
#         num = float(input("What are your numbers?: "))
#         for n in range(num):
#             numbers = float(input("What are your numbers?: "))
#         list.append(numbers)
#         if n == '':
#             break
#
#         if operator == '+':
#             print(add(list))
#
#         if operator == '-':
#             print(subtract(list))
#
#         if operator == '/':
#             print(divide(list))
#
#         if operator == '*':
#             print(multiply(list))
#     else:
#         break
#


# # 3
# # import math_operations as mo
# #
# #
# # def kalkulator(lista_danych):
# #     """
# #     Zarządza wszystkimi operacjami matematycznymi z modułu math_operations.
# #
# #     Argument:
# #     lista_danych: Lista czteroelementowa zawierająca dwie liczby do obliczeń,
# #                   numer operacji do wykonania (1 - dodawanie, 2 - odejmowanie, 3 - mnożenie, 4 - dzielenie)
# #                   i decyzję o kontynuacji działania kalkulatora (0 - zakończ działanie, 1 - kontynuuj).
# #     """
# #     operacje = {
# #         1: mo.dodaj,
# #         2: mo.odejmij,
# #         3: mo.pomnoz,
# #         4: mo.podziel,
# #     }
# #
# #     # Dane do obliczeń
# #     a = lista_danych[0]
# #     b = lista_danych[1]
# #
# #     # Wybór operacji
# #     wybor = lista_danych[2]
# #
# #     # Wybór kontynuacji działania kalkulatora
# #     kontynuacja = lista_danych[3]
# #
# #     operacja = operacje.get(int(wybor))
# #     if operacja:
# #         try:
# #             wynik = operacja(a, b)
# #             print(f"Wynik: {wynik}")
# #         except Exception as e:
# #             print(f"Wystąpił błąd: {e}")
# #     else:
# #         print("Nieznana operacja")
# #
# #     # Kontynuacja działania kalkulatora jeżeli kontynuacja = 1
# #     if kontynuacja == 1:
# #         kalkulator(lista_danych)
# #
# #
# # if __name__ == "__main__":
# #     lista_danych = [10, 5, 1, 1]
# #     kalkulator(lista_danych)
#
#
# # # Definiowanie funkcji dla każdej operacji
# # def dodaj(a, b):
# #     return a + b
# #
# # def odejmij(a, b):
# #     return a - b
# #
# # def pomnoz(a, b):
# #     return a * b
# #
# # def podziel(a, b):
# #     return a / b
# #
# # # Prosty interfejs użytkownika w konsoli
# # while True:
# #     print("Wybierz operację:")
# #     print("1.Dodaj")
# #     print("2.Odejmij")
# #     print("3.Pomnóż")
# #     print("4.Podziel")
# #     print("5.Zakończ")
# #
# #     wybor = int(input("Podaj numer operacji (1/2/3/4/5): "))
# #
# #     if wybor == 5:
# #         break
# #
# #     num1 = float(input("Podaj pierwszą liczbę: "))
# #     num2 = float(input("Podaj drugą liczbę: "))
# #
# #     if wybor == 1:
# #         print("Wynik: ", dodaj(num1, num2))
# #     elif wybor == 2:
# #         print("Wynik: ", odejmij(num1, num2))
# #     elif wybor == 3:
# #         print("Wynik: ", pomnoz(num1, num2))
# #     elif wybor == 4:
# #         print("Wynik: ", podziel(num1, num2))
# #     else:
# #         print("Nieznana operacja")
# #
#
# ------
#
# # # Importowanie wymaganych modułów
# # from math import pow
# #
# # # Proste funkcje do wykonania operacji matematycznych
# #
# # def dodaj(a, b):
# #     """
# #     Funkcja do dodawania dwóch liczb
# #
# #     Argument:
# #     a: pierwsza liczba
# #     b: druga liczba
# #
# #     Zwraca:
# #     Suma a i b
# #     """
# #     return a + b
# #
# # def odejmij(a, b):
# #     """
# #     Funkcja do odejmowania dwóch liczb
# #
# #     Argument:
# #     a: pierwsza liczba
# #     b: druga liczba
# #
# #     Zwraca:
# #     Różnica a i b
# #     """
# #     return a - b
# #
# # def pomnoz(a, b):
# #     """
# #     Funkcja do mnożenia dwóch liczb
# #
# #     Argument:
# #     a: pierwsza liczba
# #     b: druga liczba
# #
# #     Zwraca:
# #     Iloczyn a i b
# #     """
# #     return a * b
# #
# # def podziel(a, b):
# #     """
# #     Funkcja do dzielenia dwóch liczb
# #
# #     Argument:
# #     a: pierwsza liczba
# #     b: druga liczba
# #
# #     Zwraca:
# #     Iloraz a i b
# #     """
# #     return a / b
# #
# # def kalkulator(operacja, a, b):
# #     """
# #     Funkcja wyższego rzędu zarządzająca operacjami matematycznymi
# #
# #     Argument:
# #     operacja: funkcja reprezentująca operację matematyczną
# #     a: pierwsza liczba
# #     b: druga liczba
# #
# #     Zwraca:
# #     Wynik operacji na a i b
# #     """
# #     return operacja(a, b)
# #
# #
# # # Testowanie funkcji kalkulatora
# # print(kalkulator(dodaj, 5, 3))  # Wyświetli 8
# # print(kalkulator(odejmij, 5, 3))  # Wyświetli 2
# # print(kalkulator(pomnoz, 5, 3))  # Wyświetli 15
# # print(kalkulator(podziel, 5, 3))  # Wyświetli 1.6666666666666667
# #
# ----------------------------
#
# # import math_operations as mo
# #
# #
# # def kalkulator():
# #     """
# #     Zarządza wszystkimi operacjami matematycznymi z modułu math_operations.
# #     """
# #     operacje = {
# #         1: mo.dodaj,
# #         2: mo.odejmij,
# #         3: mo.pomnoz,
# #         4: mo.podziel,
# #     }
# #
# #     operacje_string = ['dodaj', 'odejmij', 'pomnoz', 'podziel']
# #
# #     while True:
# #         print("\nWybierz operację: ")
# #         for i, oper in enumerate(operacje_string, start=1):
# #             print(f"{i}. {oper}")
# #
# #         print("5. Wyjdź")
# #
# #         wybor = input("Podaj numer operacji (1/2/3/4/5): ")
# #
# #         if wybor == '5':
# #             break
# #
# #         a = float(input("Podaj pierwszą liczbę: "))
# #         b = float(input("Podaj drugą liczbę: "))
# #
# #         operacja = operacje.get(int(wybor))
# #         if operacja:
# #             try:
# #                 wynik = operacja(a, b)
# #                 print(f"Wynik: {wynik}")
# #             except Exception as e:
# #                 print(f"Wystąpił błąd: {e}")
# #         else:
# #             print("Nieznana operacja")
# #
# #
# # if __name__ == "__main__":
# #     kalkulator()
# ----------------
#
# # import math_operations as mo
# #
# #
# # def kalkulator(lista_danych):
# #     """
# #     Zarządza wszystkimi operacjami matematycznymi z modułu math_operations.
# #
# #     Argument:
# #     lista_danych: Lista czteroelementowa zawierająca dwie liczby do obliczeń,
# #                   numer operacji do wykonania (1 - dodawanie, 2 - odejmowanie, 3 - mnożenie, 4 - dzielenie)
# #                   i decyzję o kontynuacji działania kalkulatora (0 - zakończ działanie, 1 - kontynuuj).
# #     """
# #     operacje = {
# #         1: mo.dodaj,
# #         2: mo.odejmij,
# #         3: mo.pomnoz,
# #         4: mo.podziel,
# #     }
# #
# #     # Dane do obliczeń
# #     a = lista_danych[0]
# #     b = lista_danych[1]
# #
# #     # Wybór operacji
# #     wybor = lista_danych[2]
# #
# #     # Wybór kontynuacji działania kalkulatora
# #     kontynuacja = lista_danych[3]
# #
# #     operacja = operacje.get(int(wybor))
# #     if operacja:
# #         try:
# #             wynik = operacja(a, b)
# #             print(f"Wynik: {wynik}")
# #         except Exception as e:
# #             print(f"Wystąpił błąd: {e}")
# #     else:
# #         print("Nieznana operacja")
# #
# #     # Kontynuacja działania kalkulatora jeżeli kontynuacja = 1
# #     if kontynuacja == 1:
# #         kalkulator(lista_danych)
# #
# #
# # if __name__ == "__main__":
# #     lista_danych = [10, 5, 1, 1]
# #     kalkulator(lista_danych)
#
#
# # # Zadanie 1
# # class Egzaminy:
# #  typyEgz = ['Android', 'Python', 'JAVA', 'JavaEE']
# #  nrTyp = 0
# #
# #
# #    def __init__(self):
# #     self.typyEgz[self.nrTyp]
# #
# #
# #    def ustawEgz(self, wpisanyNumer):
# #     self.nrTyp = wpisanyNumer
# #
# #    def wyswietlEgz(self):
# #
# #        print('Ustawiony egzamin to: ' + self.typyEgz[self.nrTyp])
# #
# #  mojEgzaminy1 = Egzaminy()
# #  mojEgzaminy1.wyswietlEgz()
# #  mojEgzaminy1.ustawEgz(3)
# #  mojEgzaminy1.wyswietlEgz()
# #
# #
# # ----
# # class Egzaminy:
# #   typyEgz = ['Android', 'Python', 'JAVA', 'JavaEE']
# #   nrTyp = 0
# #
# #   def __init__(self):
# #     self.typyEgz[self.nrTyp]
# #
# #   def ustawEgz(self, wpisanyNumer):
# #     self.nrTyp = wpisanyNumer
# #
# #   def wyswietlEgz(self):
# #       print('Ustawiony egzamin to: ' + self.typyEgz[self.nrTyp])
# # ---
# #       mojEgzaminy1 = Egzaminy()
# #       mojEgzaminy1.wyswietlEgz()
# #       mojEgzaminy1.ustawEgz(3)
# #       mojEgzaminy1.wyswietlEgz()
# #
# #
# # # # Zadanie 2
# # class Wakacje:
# #     imie = '-'
# #     nazwisko = '-'
# #     wiek = '-'
# #     liczbaOsob = '-'
# #     transport = '-'
# #     dzieci = '-'
# #
# #     def pytanieImieNazwisko(self):
# #         imie = input('imie: ')
# #         nazwisko = input('nazwisko: ')
# #         self.imie = imie
# #         self.nazwisko = nazwisko
# #
# #     def pytanieWiek(self):
# #         wiek = input('wiek: ')
# #         self.wiek = wiek
# #
# #     def pytanieLiczbaOsob(self):
# #         liczbaOsob = input('liczba osob: ')
# #         self.liczbaOsob = liczbaOsob
# #
# #     def transport(self):
# #         transport = input('transport: ')
# #         self.transport = transport
# #
# #     def liczbaDzieci(self):
# #         dzieci = input('liczba dzieci: ')
# #         self.dzieci = dzieci
# #
# #     def wyswietlAnkiete(self):
# #         print('\nImię: ' + self.imie + '\nNazwisko: ' + self.nazwisko + '\nWiek: ' + self.wiek + '\nliczbaOsob: ' + self.liczbaOsob + '\nTransport: ' + self.transport + '\nliczbaDzieci: ' + self.dzieci)
# #
# # Dict = []
# # wakacje1 = Wakacje()
# # wakacje1.pytanieImieNazwisko()
# # wakacje1.pytanieWiek()
# # wakacje1.pytanieLiczbaOsob()
# # wakacje1.transport()
# # wakacje1.liczbaDzieci()
# # Dict.append(wakacje1)
# #
# # wakacje2 = Wakacje()
# # wakacje2.pytanieImieNazwisko()
# # wakacje2.pytanieWiek()
# # wakacje2.pytanieLiczbaOsob()
# # wakacje2.transport()
# # wakacje2.liczbaDzieci()
# # Dict.append(wakacje2)
# #
# # print(Dict[1].wyswietlAnkiete())
# #
# # class Osoba:
# #     liczba_osob = 0
# #
# #     def __init__(self, plec='unknown'):
# #         self.plec = plec
# #         Osoba.liczba_osob += 1
# #
# #     @staticmethod
# #     def print_plec(plec):
# #         print(plec)
# #
# #     @staticmethod
# #     def get_liczba_osob():
# #         return Osoba.liczba_osob
# #
# #
# # class Kobieta(Osoba):
# #     def __init__(self):
# #         super().__init__('female')
# #         Osoba.print_plec(self.plec)
# #
# #
# # class Mezczyzna(Osoba):
# #     def __init__(self):
# #         super().__init__('male')
# #         Osoba.print_plec(self.plec)

# 17 - Czerwiec -
# #
# def plus(a, b):
#     """
#     Funkcja do dodawania dwóch liczb
#
#     Argument:
#     a: pierwsza liczba
#     b: druga liczba
#
#     Zwraca:
#     Suma a i b
#     """
#     return a + b
#
# def minus(a, b):
#
#     return a - b
#
#
# def test_minus():
#     assert (minus(5, 2) == 3)
#
#
# def pomnoz(a, b):
#     return a * b
#
#
# def podziel(a, b):
#     return a / b
#
#
# while True:
#     print("Wybierz:")
#     print("1. +")
#     print("2. -")
#     print("3. *")
#     print("4. /")
#     print("5. stop")
#
#     wybor = int(input("(1/2/3/4/5): "))
#
#     if wybor == 5:
#         break
#
#     number1 = float(input("Podaj pierwszą liczbę: "))
#     number2 = float(input("Podaj drugą liczbę: "))
#
#     if wybor == 1:
#         print("=: ", plus(number1, number2))
#     elif wybor == 2:
#         print("=: ", minus(number1, number2))
#     elif wybor == 3:
#         print("=: ", pomnoz(number1, number2))
#     elif wybor == 4:
#         if number2 != 0:
#             print("=: ", podziel(number1, number2))
#         else:
#             print("Nie można ------ podzielić przez zero. ------")
#     else:
#         print("Zły wybór.")
#
# print("Koniec.")
#
# import math
#
#
# def plus(a, b):
#     """
#     Funkcja do dodawania dwóch liczb
#
#     Argument:
#     a: pierwsza liczba
#     b: druga liczba
#
#     Zwraca:
#     Suma a i b
#     """
#     return a + b
#
#
# def minus(a, b):
#     """
#     Funkcja do odejmowania dwóch liczb
#
#     Argument:
#     a: pierwsza liczba
#     b: druga liczba
#
#     Zwraca:
#     Różnica a i b
#     """
#     return a - b
#
#
# def pomnoz(a, b):
#     """
#     Funkcja do mnożenia dwóch liczb
#
#     Argument:
#     a: pierwsza liczba
#     b: druga liczba
#
#     Zwraca:
#     Iloczyn a i b
#     """
#     return a * b
#
#
# def podziel(a, b):
#     """
#     Funkcja do dzielenia dwóch liczb
#
#     Argument:
#     a: pierwsza liczba
#     b: druga liczba
#
#     Zwraca:
#     Iloraz a i b
#     """
#     return a / b
#
#
# def kalkulator(operacja, a, b):
#     """
#     Funkcja wyższego rzędu zarządzająca operacjami matematycznymi
#
#     Argument:
#     operacja: funkcja reprezentująca operację matematyczną
#     a: pierwsza liczba
#     b: druga liczba
#
#     Zwraca:
#     Wynik operacji na a i b
#     """
#     return operacja(a, b)
#
#
# # Testowanie
# print(kalkulator(plus, 25, 3))  # Wyświetli 28
# print(kalkulator(minus, 25, 3))  # Wyświetli 22
# print(kalkulator(pomnoz, 35, 25))  # Wyświetli 275
# print(kalkulator(minus, 55, 33))  # Wyświetli 22
# print(kalkulator(pomnoz, 5, 37))  # Wyświetli 165
# print(kalkulator(podziel, 590, 3))  # Wyświetli 165
# #

#
# import math
#
#
# def dodawanie(a, b):
#     """Dodaje dwie liczby.
#
#     Argument:
#         a (float): Pierwsza liczba.
#         b (float): Druga liczba.
#
#     Zwraca:
#         float: Suma dwóch liczb.
#     """
#     return a + b
#
#
# def odejmowanie(a, b):
#     """Odejmuje dwie liczby.
#
#     Argument:
#         a (float): Pierwsza liczba.
#         b (float): Druga liczba.
#
#     Zwraca:
#         float: Różnica dwóch liczb.
#     """
#     return a - b
#
#
# def mnozenie(a, b):
#     """Mnoży dwie liczby.
#
#     Argument:
#         a (float): Pierwsza liczba.
#         b (float): Druga liczba.
#
#     Zwraca:
#         float: Iloczyn dwóch liczb.
#     """
#     return a * b
#
#
# def dzielenie(a, b):
#     """Dzieli dwie liczby.
#
#     Argument:
#         a (float): Dzielna.
#         b (float): Dzielnik.
#
#     Zwraca:
#         float: Wynik dzielenia dwóch liczb.
#
#     Raises:
#         Exception: Gdy dzielenie przez 0.
#     """
#     if b == 0:
#         raise Exception("Dzielenie przez 0")
#
#     return a / b
#
#
# def pierwiastek(a):
#     """Oblicza pierwiastek kwadratowy liczby.
#
#     Argument:
#         a (float): Liczba.
#
#     Zwraca:
#         float: Pierwiastek kwadratowy liczby.
#     """
#     return math.sqrt(a)
#
#
# def calc(operacja, a, b=None):
#     """Wykonuje operację na dwóch liczbach lub jednej liczbie.
#
#     Argument:
#         operacja (function): Funkcja operacji matematycznej.
#         a (float): Pierwsza liczba.
#         b (float, optional): Druga liczba. Domyślnie None.
#
#     Zwraca:
#         float: Wynik operacji na dwóch liczbach lub jednej liczbie.
#     """
#     if b is None:
#         return operacja(a)
#     else:
#         return operacja(a, b)
#
#
# def run_calc():
#     """Uruchamia kalkulator."""
#     while True:
#         operacja = int(input("Wybierz operację: \n"
#                              "1. Dodawanie \n"
#                              "2. Odejmowanie \n"
#                              "3. Mnożenie \n"
#                              "4. Dzielenie \n"
#                              "5. Pierwiastek kwadratowy \n"
#                              "0. Koniec \n"))
#
#         if operacja == 0:
#             exit(0)
#
#         a = float(input("Podaj wartość A: "))
#
#         if operacja != 5:
#             b = float(input("Podaj wartość B: "))
#
#         if operacja == 1:
#             wynik = calc(dodawanie, a, b)
#             print("{} + {} = {}".format(a, b, wynik))
#         elif operacja == 2:
#             wynik = calc(odejmowanie, a, b)
#             print("{} - {} = {}".format(a, b, wynik))
#         elif operacja == 3:
#             wynik = calc(mnozenie, a, b)
#             print("{} * {} = {}".format(a, b, wynik))
#         elif operacja == 4:
#             wynik = calc(dzielenie, a, b)
#             print("{} / {} = {}".format(a, b, wynik))
#         elif operacja == 5:
#             wynik = calc(pierwiastek, a)
#             print("sqrt({}) = {}".format(a, wynik))
#         else:
#             print("Błędna opcja")
#
#
# run_calc()
#
# import math
#
# def dodawanie(a, b):
#     """Dodaje dwie liczby.
#
#     Argument:
#         a (float): Pierwsza liczba.
#         b (float): Druga liczba.
#
#     Zwraca:
#         float: Suma dwóch liczb.
#     """
#     return a + b
#
#
# def odejmowanie(a, b):
#     """Odejmuje dwie liczby.
#
#     Argument:
#         a (float): Pierwsza liczba.
#         b (float): Druga liczba.
#
#     Zwraca:
#         float: Różnica dwóch liczb.
#     """
#     return a - b
#
#
# def mnozenie(a, b):
#     """Mnoży dwie liczby.
#
#     Argument:
#         a (float): Pierwsza liczba.
#         b (float): Druga liczba.
#
#     Zwraca:
#         float: Iloczyn dwóch liczb.
#     """
#     return a * b
#
#
# def dzielenie(a, b):
#     """Dzieli dwie liczby.
#
#     Argument:
#         a (float): Dzielna.
#         b (float): Dzielnik.
#
#     Zwraca:
#         float: Wynik dzielenia dwóch liczb.
#
#     Raises:
#         Exception: Gdy dzielenie przez 0.
#     """
#     if b == 0:
#         raise Exception("Dzielenie przez 0")
#
#     return a / b
#
#
# def pierwiastek(a):
#     """Oblicza pierwiastek kwadratowy liczby.
#
#     Argument:
#         a (float): Liczba.
#
#     Zwraca:
#         float: Pierwiastek kwadratowy liczby.
#     """
#     return math.sqrt(a)
#
#
# def potega(a, b):
#     """Podnosi liczbę a do potęgi b.
#
#     Argument:
#         a (float): Liczba podstawy.
#         b (float): Liczba wykładnik.
#
#     Zwraca:
#         float: Wynik potęgowania.
#     """
#     return a ** b
#
#
# def logarytm(a, b):
#     """Oblicza logarytm liczby a o podstawie b.
#
#     Argument:
#         a (float): Liczba.
#         b (float): Podstawa logarytmu.
#
#     Zwraca:
#         float: Wynik logarytmu.
#     """
#     return math.log(a, b)
#
#
# def calc(operacja, a, b=None):
#     """Wykonuje operację na dwóch liczbach lub jednej liczbie.
#
#     Argument:
#         operacja (function): Funkcja operacji matematycznej.
#         a (float): Pierwsza liczba.
#         b (float, optional): Druga liczba. Domyślnie None.
#
#     Zwraca:
#         float: Wynik operacji na dwóch liczbach lub jednej liczbie.
#     """
#     if b is None:
#         return operacja(a)
#     else:
#         return operacja(a, b)
#
#
# def run_calc():
#     """Uruchamia kalkulator."""
#     while True:
#         operacja = int(input("Wybór operacji matematycznej. Wybierz opcję z listy podanych wyœwietlając jej numer "
#                              "operację: \n"
#                              "1. +Dodawanie \n"
#                              "2. -Odejmowanie \n"
#                              "3. *Mnożenie \n"
#                              "4. /Dzielenie \n"
#                              "5. Pierwiastek kwadratowy \n"
#                              "6. Potęga \n"
#                              "7. Logarytm \n"
#                              "0. Koniec \n"))
#         a = float(input("Wartość A: "))
#
#         # if operacja != 5 and operacja != 6 and operacja != 7:
#         #     b = float(input("Wartość B: "))
#
#         # if operacja != 5 and operacja != 6:
#         # b = float(input("Podaj wartość B: "))
#
#         if operacja == 1:
#             # b = float(input("Podaj wartość B: "))
#             a = float(input("Podaj wartość A: "))
#             b = float(input("Podaj wartość B: "))
#             operacja = int(input("WybÓr operacji matematycznej. Wybierz opcję z listy podanych wyœwietlając jej numer "
#                                  "operację: \n"
#                                  "1. +Dodawanie \n"
#                                  "2. -Odejmowanie \n"
#                                  "3. *Mnoœenie \n"
#                                  "4. /Dzielenie \n"
#                                  "5. Pierwiastek kwadratowy \n"
#                                  "6. Potęga \n"
#                                  "7. Logarytm \n"
#                                  "0. Koniec \n"))
#             rownasie = calc(dodawanie, a, b)
#             print("{} + {} = {}".format(a, b, rownasie))
#         elif operacja == 2:
#             rownasie = calc(odejmowanie, a, b)
#             print("{} - {} = {}".format(a, b, rownasie))
#         elif operacja == 3:
#             rownasie = calc(mnozenie, a, b)
#             print("{} * {} = {}".format(a, b, rownasie))
#         elif operacja == 4:
#             rownasie = calc(dzielenie, a, b)
#             print("{} / {} = {}".format(a, b, rownasie))
#             # try:
#             #     rownasie = calc(dzielenie, a, b)
#             #     print("{} / {} = {}".format(a, b, rownasie))
#             # except Exception as e:
#
#             # try:
#             #
#             #     rownasie = calc(dzielenie, a, b)
#             #     print("{} / {} = {}".format(a, b, rownasie))
#             # except Exception as e:
#             # print("Błąd: {}".format(e))
#             # print("Błąd: Dzielenie przez 0")
#             #
#             # print("Dzielenie przez 0")
#
#         elif operacja == 5:
#             rownasie = calc(pierwiastek, a)
#             print("sqrt({}) = {}".format(a, rownasie))
#         elif operacja == 6:
#             wynik = calc(potega, a, b)
#             print("{} ^ {} = {}".format(a, b, wynik))
#         elif operacja == 7:
#             wynik = calc(logarytm, a, b)
#             print("log({}, {}) = {}".format(a, b, wynik))
#         else:
#             print("Błędna opcja")
#             break
#
# run_calc()
#
#
# mport math
#
# def add(a, b):
#     """
#     Dodaje dwie liczby.
#
#     Argumenty:
#         a: Pierwsza liczba.
#         b: Druga liczba.
#
#     Zwraca:
#         Sumę dwóch liczb.
#     """
#     return a + b
#
# def subtract(a, b):
#     """
#     Odejmuje dwie liczby.
#
#     Argumenty:
#         a: Pierwsza liczba.
#         b: Druga liczba.
#
#     Zwraca:
#         Różnica między dwiema liczbami.
#     """
#     return a - b
#
# def multiply(a, b):
#     """
#     Mnoży dwie liczby.
#
#     Argumenty:
#         a: Pierwsza liczba.
#         b: Druga liczba.
#
#     Zwraca:
#         Iloczyn dwóch liczb.
#     """
#     return a * b
#
# def divide(a, b):
#     """
#     Dzieli dwie liczby.
#
#     Argumenty:
#         a: Pierwsza liczba.
#         b: Druga liczba.
#
#     Zwraca:
#         Iloraz dwóch liczb.
#     """
#     return math.truediv(a, b)
#
# def calculator(operacja, a, b):
#     """
#     Wykonuje operację matematyczną na dwóch liczbach.
#
#     Argumenty:
#         operation: Operacja do wykonania.
#         a: Pierwsza liczba.
#         b: Druga liczba.
#
#     Returns:
#         Wynik operacji.
#
#     Podnosi:
#         ValueError: Jeśli operacja nie jest obsługiwana.
#     """
#     operations = {
#         'add': dodawanie,
#         'subtract': odejmowanie,
#         'multiply': mnożenie,
#         'divide': dziel
#     }
#
#     func = operations.get(operation)
#     if func:
#         return func(a, b)
#     else:
#         raise ValueError("Nieprawidłowa operacja")
#     # if operation == 'add':
#
# # Przykładowe użycie
# result = calculator('add', 5, 3)
# print(result) # Wynik: 8
# result = calculator('divide', 5, 3)
# print(result) # Wynik: 1.6666666666666667
# result = calculator('divide', 5, 0)
# print(result) # Wynik: ValueError: Nieprawidłowa operacja