#!/usr/bin/python3

def dodawanie(x, y):
    return x + y

def odejmowanie(x, y):
    return x - y

def mnozenie(x, y):
    return x * y

def dzielenie(x, y):
    if y == 0:
        return "Błąd: Dzielenie przez zero!"
    return x / y

print("Wybierz operację.")
print("1.Dodawanie")
print("2.Odejmowanie")
print("3.Mnożenie")
print("4.Dzielenie")

while True:
    wybor = input("Wpisz numer operacji (1/2/3/4): ")

    if wybor in ('1', '2', '3', '4'):
        num1 = float(input("Wpisz pierwszą liczbę: "))
        num2 = float(input("Wpisz drugą liczbę: "))

        if wybor == '1':
            print(num1, "+", num2, "=", dodawanie(num1, num2))

        elif wybor == '2':
            print(num1, "-", num2, "=", odejmowanie(num1, num2))

        elif wybor == '3':
            print(num1, "*", num2, "=", mnozenie(num1, num2))

        elif wybor == '4':
            wynik = dzielenie(num1, num2)
            print(num1, "/", num2, "=", wynik)

        kolejna_operacja = input("Czy chcesz wykonać kolejną operację? (tak/nie): ")
        if kolejna_operacja.lower() != "tak":
            break
    else:
        print("Nieprawidłowy wybór")

