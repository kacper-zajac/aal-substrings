"""
Kacper Zając, 293178
AAL - Podobne najdłuższe podciągi
"""
import filecreation
import algorithm
from texttable import Texttable
import datetime



def mean(numbers):
    return float(sum(numbers)) / max(len(numbers), 1)


def main():
    table = Texttable()
    data_collection = []
    table.header(["n", "m", "q(n)", "czas"])

    mode = -1
    file = 0
    while mode < 0 or mode > 3:
        mode = int(input("Wybierz tryb:\n0 - tryb testowy / predefiniowane ustawienia (ustawienia te umozliwiaja "
                         "przetestowanie szybkosci i zlozonosci algorytmu)\n1 - tryb testowy / generator (umozliwiajacy"
                         " spersonalizowanie obliczen)\n2 - ustawienia wlasne (pozwalaja wygenerowac wlasny ciag)\n"
                         "3 - wlasne dane umieszczone w pliku plikzdanymi.txt (mozna wykorzystac do otrzymania wyniku "
                         "dla ostatnio uzytych danych)\n"))

    loop = 1
    if mode == 0:
        file = open(filecreation.createfile2(), "r")
        loop = int(input("Ile razy sprawdzone maja byc te same dane? "))
        mode = 1
    elif mode == 1:
        file = open(filecreation.createfile2_1(), "r")
        loop = int(input("Ile razy sprawdzone maja byc te same dane? "))
    elif mode == 2:
        file = open(filecreation.createfile(), "r")
    elif mode == 3:
        file = open(filecreation.createfile3(), "r")

    data_line = file.readline()
    if mode == 1:
        while data_line != "":
            data_line = data_line.strip("\n")
            data = data_line.split(" ")
            if len(data) < 3:
                input("Nie mozna znalezc podciagu znakow dla ciagu o dlugosci 0")
            else:
                iterator = loop
                complexity = 0
                time = []
                while iterator > 0:

                    start = datetime.datetime.now()
                    complexity = algorithm.use(data, mode)
                    time.append((datetime.datetime.now() - start).total_seconds())
                    iterator -= 1
                time = mean(time)
                data_collection.append([len(data[1]), data[0], complexity, time])
                data_line = file.readline()

        mediana = int((len(data_collection)) / 2)
        complexity = float(data_collection[mediana][2])
        time = (data_collection[mediana][3])

        for x in data_collection:
            x[2] = x[3] * complexity / (x[2] * max(0.0001, time))

        table.add_rows(data_collection, False)
        print(table.draw())
        table_file = open("tablica.txt", "w")
        table_file.write(table.draw())
    else:
        while data_line != "":
            data_line = data_line.strip("\n")
            data = data_line.split(" ")
            if len(data) < 3:
                input("Nie mozna znalezc podciagu znakow dla ciagu o dlugosci 0")
            else:
                print("Najdluzsze znalezione podciagi ciagow:\n", data[1], "\n", data[2], "\n")
                print("to: ", algorithm.use(data, mode))
            data_line = file.readline()

    input("\n\nNacisnij Enter, aby zakonczyc")


if __name__ == "__main__":
    main()
