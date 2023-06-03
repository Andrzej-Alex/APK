# # Utwórz klasę o nazwie Egzamin w której:
# # zdefiniujemy pole Przedmioty, które będzie listą zawierającą nazwy przedmiotów które zdajesz w tym semestrze oraz pole nrPrzedmiotu, wartość tego pola odpowiada nr przedmiotu który zdajesz jako pierwszy w sesji
# # zdefiniujemy konstruktor który ustawi/wyświetli początkowy przedmiot który będziesz zdawał w sesji
# # zdefiniujemy 2 metody ustawPrzedmiot, wyswietlPrzedmiot do zmiany wartości w/w pola i wyświetlania wyniku
# # wstaw odpowiedni komentarz dla wyświetlanej odpowiedzi, przetestuj swój program.
#
# class Egzamin:
#  def __init__(self):
#   self.Przedmioty = ["Matematyka", "Fizyka", "Chemia", "Informatyka"]
#   self.nrPrzedmiotu = 0  # pierwszy
#
#   self.wyswietlPrzedmiot()
#
#  def ustawPrzedmiot(self, nr):
#   if nr < len(self.Przedmioty):
#    self.nrPrzedmiotu = nr
#    print("Zmieniono przedmiot na:", self.Przedmioty[nr])
#   else:
#
#    print("Podano nieprawidłowy numer przedmiotu!")
#
#  def wyswietlPrzedmiot(self):
#   print("Aktualny przedmiot:", self.Przedmioty[self.nrPrzedmiotu])
#
#
# # Obiekt klasy Egzamin
# egzamin = Egzamin()
#
#
# # Przykładowe użycie metod
# egzamin.ustawPrzedmiot(2)  # Zmieniono przedmiot na: Chemia
# egzamin.wyswietlPrzedmiot()  # Aktualny przedmiot: Chemia
#





# from tkinter import *
# root = Tk()  # obiekt okno
# root.configure(background='red') # kolor tła
# root.configure(cursor='circle') # kursor
# root.configure(bd=20) # krawędœ
# root.configure(relief='sunken') # efekt
# root.title('OOOkkknnoo') # tytuł okna
# root.geometry('450x200') # rozmiar okna
# root.mainloop()

'''
root.resizable(0,0) # nie moliwe zmiany rozmiaru okna
root.minsize(100,100) # minimalna wielkość okna
'''
import self as self


# import a as a
# # import b as b
# #
# # a.a()
# # b.b()
#
# class A(object):
#
#  def _init_(self, b, c):
#  self.y = b
#  self.z = c
# class B(A):
#  def _init_(self, a, *args, **kwargs):
#  super(B, self)._init_(*args, **kwargs)
#  self.x = a
#
# class Student:
#  znizka_kino = 50 # atrybut klasy, cecha wszystkich obiektów klasy Student
#  def _init_(self, nazwisko, nrindeksu):
#  self._nazwisko = nazwisko # pole "prywatne", nie widoczne poza klasą
#  self.nrindeksu = nrindeksu # pole "publiczne"
#
#  def lubisz_informatyke(self):
#  print('Nie wiem')
#
#  def moje_nazwisko(self):
#  print('Moje nazwisko to: ',self._nazwisko)
#
#  def zmien_nazwisko(self, nazwisko):
#  self._nazwisko = nazwisko
#
#  class SuperStudent(Student):  # klasa SuperStudent dziedziczy po klasie Student
#
#
# def _init_(self, nazwisko, nrindeksu, stypendium):
#  Student._init_(self, nazwisko, nrindeksu)  # wywołanie konstruktora z Student
#  self.stypendium = stypendium  # wzbogacamy go o dodatkowe dane tj. stypendium
#
#
# def lubisz_studia(self):
#  Student.lubisz_informatyke(self)
#  print('Oczywiście')
#
#
# class SlabyStudent(Student):
#  def _init_(self, nazwisko, nrindeksu, powtarzany_przedmiot):
#
#   Student._init_(self, nazwisko, nrindeksu)  # uniwersal student
#
#  self.powtarzany_przedmiot = powtarzany_przedmiot  # dodatkowe dane
#
#  def lubisz_studia(self):
#   Student.lubisz_informatyke(self)
#
#  print('Lubię, bo muszę !')
#
#  student = Student("kowalski", '0001')
#  # print(student.__nazwisko) # to zmienna prywatna takie odwołanie nie jest możliwe,
#  # błąd: AttributeError: 'Student' object has no attribute '__nazwisko'
#  # nie chcemy, aby zeby ktos ją zmienił poza klasą,
#  student.moje_nazwisko()
#  print(student.nrindeksu)
#  student.nrindeksu = '0002'
#  student.__nazwisko = "Kowalski"
#  l = []
#  l.append(SuperStudent('SuperKowalski', '0003', 'tak'))
#  l.append(SlabyStudent('SlabyKowalski', '0004', 'Python'))
#  for student in l: student.lubisz_studia()

class Egzaminy:
 typyEgz = ['Android', 'Python', 'JAVA', 'JavaEE']
 nrTyp = 0

   def __init__(self):
    self.typyEgz[self.nrTyp]

   def ustawEgz(self, wpisanyNumer):
    self.nrTyp = wpisanyNumer

   def wyswietlEgz(self):
       print('Ustawiony egzamin to: ' + self.typyEgz[self.nrTyp])

 mojEgzaminy1 = Egzaminy()
 mojEgzaminy1.wyswietlEgz()
 mojEgzaminy1.ustawEgz(3)
 mojEgzaminy1.wyswietlEgz()

 # print('Ustawiony typ muzyki to: ' + self.typyEgz[self.nrTyp])