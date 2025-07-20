import random

print("Witaj w grze w której musisz zgadnąć liczbę z wybranego przez ciebie przedziału!")

niska = int(input("Podaj pierwszą liczbę z przedziału: "))
wysoka = int(input("Podaj ostatnią liczbę z przedziału: "))

num = random.randint(niska, wysoka + 1)

szanse = int(input("Podaj liczbę szans które chcesz mieć: "))
licznik_szans = 0

while licznik_szans < szanse:
    licznik_szans += 1
    zgadniecie = int(input(f"Liczba prób: {licznik_szans} .Podaj liczbę: "))
    if zgadniecie == num:
        print(f"Gratulacje zgadłeś prawidłową licbę czyli {num} w {licznik_szans} próbach")
        break
    elif licznik_szans >= szanse and zgadniecie != num:
        print("Przekroczyłeś liczbę prób spróbuj ponownie!")
    elif licznik_szans == szanse - 1 and zgadniecie > num:
        print("Ostatnia próba podaj mniejszą liczbę: ")
    elif licznik_szans == szanse - 1 and zgadniecie < num:
        print("Ostatnia próba podaj większą liczbę: ")
    elif zgadniecie > num:
        print("Podaj mniejszą liczbę")
    elif zgadniecie < num:
        print("Podaj większą liczbę")
