from re import X
import sys
import logging
from unittest.case import doModuleCleanups
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
    logging.info("Twoja wybor to {choice}".format(choice=choice))
    if choice in ('1','2','3','4'):
        num1 = float(input("Wpisz pierwsza liczbe: "))
        num2 = float(input("Wpisz druga liczbe: "))
        logging.info("Twoja pierwsza liczba to {num1}".format(num1=num1))
        logging.info("Twoja druga liczba to {num2}".format(num2=num2))
        if choice == '1':
            print(num1, "+", num2, "=", dodawanie(num1, num2))
            logging.info('%s wynik dodawania', num1+num2)
        elif choice == '2':
            print(num1, "-", num2, "=", odejmowanie(num1, num2))
            logging.info('%s wynik odejmowania', num1-num2)
        elif choice == '3':
            print(num1, "*", num2, "=", mnozenie(num1, num2))
            logging.info('%s wynik mnozenia', num1*num2)
        elif choice == '4':
            if num2 > 0:
                print(num1, "/", num2, "=", dzielenie(num1, num2))
                logging.info('%s wynik mnozenia', num1/num2)
            else:
                print("nie dziel przez zero")
                logging.info("nie dziel przez zero")

           # print(num1, "/", num2, "=", dzielenie(num1, num2))
           # logging.info('%s wynik dzielenia', num1/num2)
            

        obliczenia = input("czy chcesz kontynuowac? (Tak/Nie)")
        if obliczenia == "Nie":
            break
    else:
        print ("Nieprawidlowa wartosc")