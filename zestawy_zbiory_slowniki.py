#zestawy, zbiory

naprezenia = [1, 8, 3, 2, 8, 1, 2]
print(naprezenia)

unikalne = list(set(naprezenia))
unikalne = unikalne.sort()
print(unikalne)

#slownik (klucz: wartosc)

dict = { "brand": "Ford", "model": "Mondeo", "year": 2018 }
print(dict)

x = dict.get("model")
print(x)
y = dict.get("model_auta", "brak danych")
print(y)

dict["year"] = 2023
dict["kolor"] = "czarny"
print(dict)

mapa = {(52.1, 21.0): "Warszawa"}
miejsce = mapa[ (52.1, 21.0)]
print(miejsce)

klucze = dict.keys()
print(klucze)

wartosci = dict.values()
print(wartosci)