import logging

def dodawanie (x, y):
    return x + y

# funkcja odejmowania
def odejmowanie(x, y):
    return x - y

# funkcja mnozenia
def mnozenie (x, y):
    return x * y

def dzielenie (x, y):
    return x / y

logging.info ("Jakie działanie chciałbyś wykonać:?")
logging.info ("1.Dodawanie")
logging.info ("2. Odejmowanie")
logging.info ("3. Mnożenie")
logging.info ("4. Dzielenie")

while True:
    #wybierz co chcesz zrobić
    choice = input("Wybierz 1,2,3,4:")
    if choice in ('1','2','3','4'):
        num1 = float(input("Wpisz pierwsza liczbe: "))
        num2 = float(input("Wpisz druga liczbe: "))
        if choice == '1':
            print(num1, "+", num2, "=", dodawanie(num1, num2))
        elif choice == '2':
            print(num1, "-", num2, "=", odejmowanie(num1, num2))
        elif choice == '3':
            print(num1, "*", num2, "=", mnozenie(num1, num2))
        elif choice == '4':
            print(num1, "/", num2, "=", dzielenie(num1, num2))
        obliczenia = input("czy chcesz kontynuowac? (Tak/Nie)")
        if obliczenia == "Nie":
            break
    else:
        print ("Nieprawidlowa wartosc")