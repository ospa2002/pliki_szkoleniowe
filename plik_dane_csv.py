plik = open("dane.csv" , 'rt' , encoding= "utf8")

#tu sa parametry do zmiany
separator_csv = ","
#*********************************************************


next(plik)
wyniki = {} #tu bede unikatowe marki pojazdow i obliczenia
for wiersz in plik:
    wiersz = wiersz.strip().split(";")

    marka = wiersz[1]
    cena = float(wiersz[2])
    przebieg = float(wiersz[8])

    #uzupelnienie slownika pomocniczego
    if marka not in wyniki:
        wyniki[marka] =  [cena , przebieg , 1]
    else:
        wyniki[marka][0] += cena
        wyniki[marka][1] += przebieg
        wyniki[marka][2] += 1

plik.close()

for marka in wyniki:
    ile = wyniki[marka][2]
    przebieg = wyniki[marka][1]
    srednia = round(przebieg / ile, 2)

    wyniki[marka].append(srednia)

#print(wyniki)

#zapis obliczonych danych do csv

naglowki_lista = ['LP' , 'Marka' , 'Cena' , 'Sredni przebieg' , "Ilosc pojazdow"]
naglowki_tekst = separator_csv.join(naglowki_lista)

zapis = []
zapis.append(naglowki_tekst)

lp = 1

for marka, dane in wyniki.items():
    ceny = str(dane[0])
    przebieg = str(dane[3])
    ile = str(dane[2])
    lp_tekst = str(lp)

    pomocnicza_lista = [lp_tekst, marka, ceny, przebieg, ile]
    pomocniczy_tekst = separator_csv.join(pomocnicza_lista)

    zapis.append(pomocniczy_tekst)
    lp += 1

do_zapisu = "\n".join(zapis)

print(do_zapisu)

plik = open("Obliczenia_pojazdow.csv", "w", encoding="utf8")
plik.write(do_zapisu)
plik.close()

#praca domowa - kazdy plik oddzielnie z nazwa lokalizacji 