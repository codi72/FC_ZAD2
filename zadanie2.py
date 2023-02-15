print("Ładowarka paczek")
maks_ilosc_elementow = int(input("Wprowadź ilość elementów, którą przyjmie aplikacja: "))
if maks_ilosc_elementow > 0:
    print(f"Aplikacja przyjmie {maks_ilosc_elementow} elementów.")
else:
    print(f"Podałeś błędną wartość {maks_ilosc_elementow} -uruchom program jeszcze raz i wprowadź liczbę całkowitą większą od zera")
    print("Podsumowanie:")
    print("Liczba paczek wysłanych: 0")
    print("Liczba kilogramow wysłanych: 0")
    print("Suma pustych kilogramow: 0")
    print(f"Paczka, która miała najwięcej pustych kilogramów: Najmniej kilogramów miała paczka "
    f"0 : 0")
    exit("Zrestaruj program")
biezacy_element = 0
waga_paczki = 0
lista_paczek = []
for biezacy_element in range(maks_ilosc_elementow):
    waga_elementu = int(input("Podaj element (waga z przedziału 1 a 10 kg): "))
    if 1 <= waga_elementu <= 10:
        biezacy_element += 1
        print(f"Dodajemy do paczki - obecna ilość elementów: {biezacy_element}")
        if waga_paczki + waga_elementu > 20:
            lista_paczek.append(waga_paczki)
            waga_paczki = 0
        waga_paczki += waga_elementu
    else:
        print("Przekroczono limit - kończę działanie.")
        break
lista_paczek.append(waga_paczki)
length_of_packages = len(lista_paczek)
sum_of_packages = sum(lista_paczek)
minimal_package = min(lista_paczek)

print("Podsumowanie:")
print(f"Liczba paczek wysłanych: {length_of_packages}")
print(f"Liczba kilogramow wysłanych: {sum_of_packages}")
print(f"Suma pustych kilogramow: {length_of_packages * 20 - sum_of_packages}")
print(f"Paczka, która miała najwięcej pustych kilogramow: Najmniej kilogramow miała paczka "
      f"{lista_paczek.index(minimal_package) + 1} : {20 - minimal_package}")