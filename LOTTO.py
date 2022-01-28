import random
import time

print("Podaj sześć liczb od 1 do 49:")
a = int(input("1 - "))
b = int(input("2 - "))
c = int(input("3 - "))
d = int(input("4 - "))
e = int(input("5 - "))
f = int(input("6 - "))

print("")
print("Trwa losowanie wygrywających liczb...")

wyg1 = random.randrange(1, 49)
wyg2 = random.randrange(1, 49)
wyg3 = random.randrange(1, 49)
wyg4 = random.randrange(1, 49)
wyg5 = random.randrange(1, 49)
wyg6 = random.randrange(1, 49)

time.sleep(3)

print("Wygrywające liczby to:", wyg1, wyg2, wyg3, wyg4, wyg5, wyg6)

wynik = 0

wylosowane = [wyg1, wyg2, wyg3, wyg4, wyg5, wyg6]

liczby = [a, b, c, d, e, f]

for liczba in liczby:
    if liczba in wylosowane:
        wynik = wynik + 1
    
print("Udało Ci się trafić",wynik,"liczb")
