import math
import time


# dodawanie kolejnych wartości na podstawie klucza do podanego słownika
def add_values_in_dict(sample_dict, key, list_of_values):
    if key not in sample_dict:
        sample_dict[key] = list()
    sample_dict[key].extend(list_of_values)
    return sample_dict


#########################################################################
start = time.monotonic()

slonie_1 = []
slonie_2 = []
masa_sloni = []

file = open("slo10b.in")  # w "" wpisujemy nazwę pliku z rozszerzeniem. Plik z danymi w tym samym folderze co kod źródłowy

for x, line in enumerate(file):
    if x > 0:
        if x == 1:
            masa_sloni = line.strip().split(' ')
        elif x == 2:
            slonie_1 = line.strip().split(' ')
        elif x == 3:
            slonie_2 = line.strip().split(' ')

file.close()

masa_sloni = [int(i) for i in masa_sloni]  # zamiana na int wartości w liscie


# dlugosc tablicy
ilosc_elementow = (len(slonie_1))

# stworzenie tablicy true/false czy słoń ma dobrą pozycję
pozycja_sloni = []

# dodawanie true/false pozycji słonia
for x in range(0, ilosc_elementow):
    if slonie_1[x] == slonie_2[x]:
        pozycja_sloni.append(True)
    else:
        pozycja_sloni.append(False)

# print(pozycja_sloni)
slonie_id = [i for i in range(0, len(slonie_1))]  # lista do id
slonie_1_id = dict(zip(slonie_1, slonie_id))  # połączenie listy slonie_1 i slonie_id w słownik
# print(slonie_1_id)

# Rozklad p na cykle
c = 0
# Utworzenie pustego słownika Cykli
Cykle = {}
for i in range(0, ilosc_elementow):
    if not pozycja_sloni[i]:
        c = c + 1
        x = i
        while not pozycja_sloni[x]:
            pozycja_sloni[x] = True
            Cykle = add_values_in_dict(Cykle, "Cykl_" + str(c), [slonie_1[x]])
            # x = slonie_1.index(slonie_2[x])
            # print(x)
            x = int(slonie_1_id.get(str(slonie_2[x])))  # przekazenie do x pozycji slonie_1 przy pomocy wartości słonie_2


# print(Cykle)

# Wyznaczenie parametrów cykli
minimum = math.inf

# Utworzenie dwóch słowników, dla sumy cykli i min cykli
cykle_sum = {}
cykle_min = {}

for i in range(1, c + 1):
    cykle_sum = add_values_in_dict(cykle_sum, "Suma_Cykl_" + str(i), [0])
    cykle_min = add_values_in_dict(cykle_min, "Min_Cykl_" + str(i), [math.inf])
    for x in Cykle.get("Cykl_" + str(i)):
        cykle_sum.get("Suma_Cykl_" + str(i))[0] += masa_sloni[int(x) - 1]
        if cykle_min.get("Min_Cykl_" + str(i))[0] > masa_sloni[int(x) - 1]:
            cykle_min.get("Min_Cykl_" + str(i))[0] = masa_sloni[int(x) - 1]

# print(cykle_sum)
# print(cykle_min)
minimum = min(cykle_min.values())[0]  # zwrócenie elementu [0] listy aby zapisać do int

# Obliczanie wyniku
w = 0
metoda_1 = 0
metoda_1_1 = 0
metoda_2 = 0
metoda_2_1 = 0

for i in range(1, c + 1):
    metoda_1_1 = cykle_sum.get("Suma_Cykl_" + str(i))[0] + (len(Cykle.get("Cykl_" + str(i))) - 2) * \
                 cykle_min.get("Min_Cykl_" + str(i))[0]
    metoda_1 += metoda_1_1
    metoda_2_1 = cykle_sum.get("Suma_Cykl_" + str(i))[0] + cykle_min.get("Min_Cykl_" + str(i))[0] + (
            len(Cykle.get("Cykl_" + str(i))) + 1) * minimum
    metoda_2 += metoda_2_1
    w += min(metoda_1_1, metoda_2_1)

# print("Metoda_1", metoda_1)
# print("Metoda_2", metoda_2)
# print("W", w)
print(w)
end = time.monotonic()
print(end - start)
