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

class Osoba:
    liczba_osob = 0

    def __init__(self, plec='unknown'):
        self.plec = plec
        Osoba.liczba_osob += 1

    @staticmethod
    def print_plec(plec):
        print(plec)

    @staticmethod
    def get_liczba_osob():
        return Osoba.liczba_osob


class Kobieta(Osoba):
    def __init__(self):
        super().__init__('female')
        Osoba.print_plec(self.plec)
        print(Osoba.get_liczba_osob())
        print(super().get_liczba_osob())


class Mezczyzna(Osoba):
    def __init__(self):
        super().__init__('male')
        Osoba.print_plec(self.plec)
        print(Osoba.get_liczba_osob())
        print(super().get_liczba_osob())