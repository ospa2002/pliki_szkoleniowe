#zad. teksty

from datetime import datetime, date, timedelta

tekst = "03/12/2025 jan KOWalski wyplata PLN: 10999.76"

#Wytnij i wyswietl: rok, mc, dzien
print("dzien:\t\t",tekst[0:2])
print("miesiac:\t",tekst[3:5])
print("rok:\t\t",tekst[6:10])

#Wytnij i popraw jakos tekstuL imie i nazwisko
iin = tekst[11:23].title()
print(f"imie i nazwisko: {iin}")

#Wyplata
dwukropek = tekst.find( ":" )
wyplata_pln = tekst[dwukropek + 2: ]
wyplata_pln = float(wyplata_pln)
wyplata_eu = wyplata_pln / 4.33
wyplata_pln = int(round(wyplata_pln, 0 ))
#wyplata_eu = round(wyplata_eu, 0 )
print("wyplata PLN:\t", wyplata_pln)
print(f"wyplata EU:\t {wyplata_eu:.0f}")

#Wyciaganie daty
data_z_tekstu = tekst[0:10]
data_obiekt = datetime.strptime(data_z_tekstu, '%m/%d/%Y') #parsowanie daty
#zmiana tekstu na prawidowa date
wynikowa_data = data_obiekt.strftime('%Y-%m-%d') #zmiana formatu daty na inny - string (tekst)
print(wynikowa_data)

lista = tekst.split()
print(lista)

#lista = lista.title()

lista[1] = lista[1].title()
lista[2] = lista[2].title()
print(lista[1], lista[2])

znowu_tekst = ' '.join(lista) #przed kropka separator ktory polaczy elementy listy
print(znowu_tekst)

znowu_tekst = znowu_tekst.replace("Jan", "Piotr").split()
print(znowu_tekst)

#znowu_lista = znowu_tekst.split()
#print(znowu_lista)

