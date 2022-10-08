from re import X
import sys
import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s', filename="logfile.log")

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

print ("Jakie działanie chciałbyś wykonać:?")
print ("1.Dodawanie")
print ("2. Odejmowanie")
print ("3. Mnożenie")
print ("4. Dzielenie")

while True:
    #wybierz co chcesz zrobić
    choice = input("Wybierz 1,2,3,4:")
    if choice in ('1','2','3','4'):
        num1 = float(input("Wpisz pierwsza liczbe: "))
        num2 = float(input("Wpisz druga liczbe: "))
        logging.info (num1)
        logging.info (num2)
        if choice == '1':
            print(num1, "+", num2, "=", dodawanie(num1, num2))
            logging.info ("wynik dodawania", {num1}, "i", {num2}, "to ", dodawanie(num1,num2))
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