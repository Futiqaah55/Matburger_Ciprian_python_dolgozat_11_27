#1.
import math
print("Mit szeretnél kiszámítani? Kör vagy Négyzet?")

alakzat = input("Írd be, hogy 'kör' vagy 'négyzet': ")

if alakzat == "Kör":
    sugar = float(input("Add meg a kör sugarát: "))
    terulet = math.pi * sugar ** 2
    print("A kör területe:", round(terulet, 2))
elif alakzat == "Négyzet":
    oldal = float(input("add meg a négyzet oldalhosszát: "))
    terulet = oldal ** 2
    print("oldalhossz:", round(terulet, 2))
    print("A négyzet területe:", round(terulet, 2))
else:
    print("Érvénytelen alakzat. csak Kör vagy Négyzet lehet.")

#2.
nev = input("mi a felhasználó neved?: ")
jelszo = input("Mi a jelszavad?: ")

if nev == "admin" and jelszo == "1234":
    print("Sikeres bejelentkezés!")
elif nev != "admin":
    print("Hibás felhasználónév!")
elif jelszo != "1234":
    print("hibás jelszó!")
else:
    print("Hibás felhasználónév és jelszó!")

#3.
osszeg = float(input("Add meg a vásárlás összegét: "))

if osszeg < 10000:
    kedvezmeny = 0
elif 10000 <= osszeg <= 20000:
    kedvezmeny = 0.05
else:
    kedvezmeny =  0.1
vegosszeg = osszeg 

vegosszeg = osszeg * (1 - kedvezmeny)

print("A végösszeg kedvezménnyel:", vegosszeg)


#4.
import random
kocka1 = random.randint(1, 6)
kocka2 = random.randint(1, 6)

kocka_dobas = kocka1 + kocka2

print("dobott értékek:", kocka1, "és", kocka2)

if kocka_dobas > 9:
    print("Nagy dobás!")
elif 6 <= kocka_dobas <= 9:
    print("Közepes dobás!")
else:
    print("Kicsi dobás!")