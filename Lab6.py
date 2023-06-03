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

class Student:
 znizka_kino = 50 # atrybut klasy, cecha wszystkich obiektów klasy Student
 def _init_(self, nazwisko, nrindeksu):
 self._nazwisko = nazwisko # pole "prywatne", nie widoczne poza klasą
 self.nrindeksu = nrindeksu # pole "publiczne"

 def lubisz_informatyke(self):
 print('Nie wiem')

 def moje_nazwisko(self):
 print('Moje nazwisko to: ',self._nazwisko)

 def zmien_nazwisko(self, nazwisko):
 self._nazwisko = nazwisko

 class SuperStudent(Student):  # klasa SuperStudent dziedziczy po klasie Student


def _init_(self, nazwisko, nrindeksu, stypendium):
 Student._init_(self, nazwisko, nrindeksu)  # wywołanie konstruktora z Student
 self.stypendium = stypendium  # wzbogacamy go o dodatkowe dane tj. stypendium


def lubisz_studia(self):
 Student.lubisz_informatyke(self)
 print('Oczywiście')


class SlabyStudent(Student):
 def _init_(self, nazwisko, nrindeksu, powtarzany_przedmiot):

  Student._init_(self, nazwisko, nrindeksu)  # uniwersal student

 self.powtarzany_przedmiot = powtarzany_przedmiot  # dodatkowe dane

 def lubisz_studia(self):
  Student.lubisz_informatyke(self)

 print('Lubię, bo muszę !')

 student = Student("kowalski", '0001')
 # print(student.__nazwisko) # to zmienna prywatna takie odwołanie nie jest możliwe,
 # błąd: AttributeError: 'Student' object has no attribute '__nazwisko'
 # nie chcemy, aby zeby ktos ją zmienił poza klasą,
 student.moje_nazwisko()
 print(student.nrindeksu)
 student.nrindeksu = '0002'
 student.__nazwisko = "Kowalski"
 l = []
 l.append(SuperStudent('SuperKowalski', '0003', 'tak'))
 l.append(SlabyStudent('SlabyKowalski', '0004', 'Python'))
 for student in l: student.lubisz_studia()
