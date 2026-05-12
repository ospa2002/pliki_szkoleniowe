'''
import cowsay
print("Hello, World!")

cowsay.pig("Czesc!!!")

print(cowsay.char_names) #nazwy zwierzakow
'''

"""
wielo
linij
kowy
"""
'''
print("ala","ma","kota")
print("ala"+"ma"+"kota")

print("*********************************")
print("="*40)

# zmienne
x = 5
y = None
z = "tekst"
a = 'tekst'
r = a
p,q,s = 2, "Ala", 6


print(x,y,z,a,r)
print(r)

print("*"*40)

import keyword
print(keyword.kwlist)

x = "100.143"
# x = float(x)
print(x)

y = 10
y = y * 5
print(y)

print("*"*40)

miasto = "Warszawa"
rzeka = "Wisla"
print(f"Jestem w {miasto}","ladna pogoda", sep=", ",end=". ") #aby odczytac - uzyj f przed KAZDYM ""
print(f"{miasto} lezy nad {rzeka}.")

#\n - od nowej linii
#\t - wciecia, tabulatory

print(f"Jestem w \n\t{miasto}","ladna pogoda\n", sep=", ") #aby odczytac - uzyj f przed KAZDYM ""

print("*"*40)

liczba = 128901234567890.123123123
print(f"Wynik:{liczba:,}")
print(f"Zysk:{liczba:,.2f} PLN")

print("*"*40)

polska_liczba = f"{liczba:_.2f}".replace("," , "").replace("." , ",")
print(f"Zysk netto:{polska_liczba} PLN")

x = 123


wynik = str(x).rjust(6," ")

print(wynik)

'''

#********************Dzien 2***************************

x = 16.48
y = 16.71
print(x-y)

wynik = round(x-y, 2)
print(wynik)

b = "Hello, World!"
print(b[2:5])

przecinek = b.find(",")
print(b[przecinek + 2:])
