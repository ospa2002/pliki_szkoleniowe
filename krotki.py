#krotki

krotka = ("Ala" , "3", "koty")
#krotka[0] = "Zosia"
print(krotka[0])

jeden_element = ("Tylko ja",) #zeby zrobic krotke to musisz dac "," na koncu

x, y, z = krotka
print(x,z,y)

print(krotka.count("3"))
print(krotka.index("koty"))
print(len(krotka))

print("Ala" in krotka)

lista = list(krotka)
lista[0] = "nowy"
krotka2 = tuple(lista)
print(krotka2)