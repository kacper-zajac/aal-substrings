import random
import string
import os.path
from os import path

def randomstring(string_length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(string_length))


def randomstring1(string_length):
    letters = 'a'
    return ''.join(random.choice(letters) for i in range(string_length))


def createfile():
    name = "plikzdanymi.txt"
    howmany = int(input("Ile literek - "))
    howmany2 = int(input("Ile rozniacych sie znakow - "))
    new_file = open(name, "w")
    str1 = str(howmany2) + " " + str(randomstring(howmany)) + " " + str(randomstring(howmany))
    new_file.write(str1)
    new_file.close()
    return name


def createfile2():
    name = "plikzdanymi.txt"
    n = 4600
    new_file = open(name, "w")
    while n < 15000:
        m = 0
        while m < 16:
            str1 = str(m) + " " + str(randomstring(int(n))) + " " + str(randomstring(int(n)))
            new_file.write(str1 + "\n")
            m *= 4
            m += 3
        n *= 1.2
    new_file.close()
    return name

def createfile2_1():
    name = "plikzdanymi.txt"
    print("Musisz podac dane niezbedne do utworzenia bazy problemu")
    n = int(input("Od jakiej liczby n chcesz rozpoczac (wieksze od 0) - "))
    if n == 0:
        exit()
    q = int(input("Podaj iloraz (ile razy wieksze ma byc kolejne n) - "))
    it = int(input("Ile ciagow chcesz zbadac - "))
    base_m = int(input("Od jakiej ilosci dozwolonych blednych znakow (m) chcesz zaczac (wieksze/rowne 0 - "))
    plus_m = int(input("Podaj roznica (ile wieksze maja byc kolejne m) - "))
    max_m = int(input("Podaj maksymalna akceptowalna wartosc m - "))
    new_file = open(name, "w")
    while n < n + q * it:
        m = base_m
        while m <= max_m:
            str1 = str(m) + " " + str(randomstring(int(n))) + " " + str(randomstring(int(n)))
            new_file.write(str1 + "\n")
            m += plus_m
        n *= q
    new_file.close()
    return name


def createfile3():
    if path.exists("plikzdanymi.txt"):
        return "plikzdanymi.txt"
    else:
        input("Plik musi istniec!")
        exit()