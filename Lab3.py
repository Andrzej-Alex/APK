# 1)
## You should to document your code by using python docstrings (google) ZROBIĆ!!!
def lab2_1(password):
    male_litery = "a ą b c ć d e ę f g h i j k l ł m n ń o ó p r s ś t u w y z ź ż".split(" ")
    duze_litery = "A Ą B C Ć D E Ę F G H I J K L Ł M N Ń O Ó P R S Ś T U W Y Z Ź Ż".split(" ")
    cyfry = "1 2 3 4 5 6 7 8 9 0".split(" ")

    for lower in password:
        if lower in male_litery:
            break
    else:
        return "Hasło nie posiada żadnych małych liter"

    for upper in password:
        if upper in duze_litery:
            break
    else:
        return "Hasło nie posiada żadnych dużych liter."

    for number in password:
        if number in cyfry:
            break
    else:
        return "Hasło nie posiada żadnych cyfr"

    if len(password) >= 4 and len(password) <= 8:
        return f"Hasło: '{password}' jest poprawne."
    else:
        return "Hasło jest za krótkie/długie."
"""
Haslo = "testT123"

plik = open("zad1.txt","w")
plik.write(lab2_1(Haslo))
plik.close()
"""

# 2)
## (dokumentacja kodu styl google) ZROBIĆ!!!
def lab2_2(x,y):
    complete = ""
    try:
        for z in range(x,y+1,1): #(both included)
            if z % 7 == 0:
                if z % 5 != 0:
                    complete += f"{z}, "
        return complete
    except TypeError:
        return "Jedna z podanych wartości nie jest liczbą całkowitą"

"""
x = 1000
y = 2101

plik = open("zad2.pkl","w")
plik.write(lab2_2(x,y))
plik.close()
"""

# 3)
## Requirements:  ZROBIĆ!!!
## You should to document your code by using python docstrings (google)

def lab2_3(list):
    return_list = ""
    if len(list) > 0 and len(list) <= 99:
        for element in list:
            return_list += f"{element**element}, "
        return f"Wynik: {return_list}"

    return f"Error liczba wpisanych parametrów przerosła 100 i wynosi {len(list)}"

"""
lista = input("Podaj listę liczb po przecinku (np: 1,3,5,7,8): ") #liczby wypisane przez użytkownika
lista = lista.split(",") #string zostaje podzielony na podzielne cyfry
lista = [int(x) for x in lista] #zamieniamy te cyfry na prawdziwe inty

print(lab2_3(lista))
"""

# 4)
## Requirements:  ZROBIĆ!!!
## You should to document your code by using python docstrings (google)
## Name of input parameters: x1, x2, ..., xn ????
def lab2_4():
    try:
        list = globals()['lista_zadanie4'] #globals()
    except KeyError:
        return "Zmienna 'lista_zadanie4' potrzebna do działania programu nie istnieje"
    except TypeError:
        return "Zmienna 'lista_zadanie4' zwraca zły typ danych"
    except ValueError:
        return "Zmienna 'lista_zadanie4' zwraca zły tekst zamiast liczb"

    return_list = ""
    if len(list) > 0 and len(list) <= 99:
        for element in list:
            return_list += f"{element**element}, "
        globals()['lista'] = return_list
        return f"Wynik: {return_list}"

    return f"Error liczba wpisanych parametrów przerosła 100 i wynosi {len(list)}"

"""
lista_zadanie4 = input("Podaj listę liczb po przecinku (np: 1,3,5,7,8): ") #liczby wypisane przez użytkownika
lista_zadanie4 = lista_zadanie4.split(",") #string zostaje podzielony na podzielne cyfry
lista_zadanie4 = [int(x) for x in lista_zadanie4] #zamieniamy te cyfry na prawdziwe inty
print(lab2_4())
"""


# 5)

import os

def lab2_5(folder_dir,copy_folder_dir):
    for nazwa_pliku in os.listdir(folder_dir):
        if 'ABC' in nazwa_pliku:
            plik = os.path.join(folder_dir, nazwa_pliku)
            with open(plik, 'r') as x:
                zawartosc = x.read()
                ilosc_slow = 0
                for slowo in zawartosc.split():
                    if len(slowo) > 3: #więcej niz 3
                        ilosc_slow+=1
                print(f"Nazwa pliku z folderu: {nazwa_pliku}, posiada on: {ilosc_slow} posiądających więcej niż 3 litery słów")
        elif 'EF.txt' in nazwa_pliku:
                plik2 = os.path.join(folder_dir, nazwa_pliku)
                sciezka_nowego_folderu = os.path.join(folder_dir, copy_folder_dir)
                if not os.path.exists(sciezka_nowego_folderu):
                    os.makedirs(sciezka_nowego_folderu)
                sciezka_nowego_pliku = os.path.join(sciezka_nowego_folderu, nazwa_pliku)
                with open(plik2, 'r') as zrodlo, open(sciezka_nowego_pliku, 'w') as cel:
                    cel.write(zrodlo.read())
        elif '0' in nazwa_pliku:
            plik3 = os.path.join(folder_dir, nazwa_pliku)
            with open(plik3, 'r') as file:
                zawartosc2 = file.read()
                ilosc_slow = 0
                for slowo in zawartosc2.split():
                        ilosc_slow += 1
                print(f"Nazwa pliku z folderu: {nazwa_pliku}, posiada on: {ilosc_slow} słów")

    else:
            print(f"Nazwa pliku z folderu: {nazwa_pliku}")

"""
lab2_5("DocumentLab5","DocumentLab5copy")

"""