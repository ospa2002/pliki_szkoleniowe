#petle for i while

cars = ['audi' , 'bmw' , 'skoda' , 'kia']



for car in cars:
    print('Pojazd: ', car)

ile_razy = 6

for x in range(ile_razy):
    y = x*2
    print('Petla uruchomila sie:', x)
    print('y =', y)



ile = len(cars)

for car in range(ile):
    print("Pojazd nr =", car + 1 , end=" ")
    samochod = cars[car]
    print("to: " , samochod)

 
    
garaz = { 'Toyota': 'Corolla' , 'Mazda': 'CX-5' , 'BMW': 'M3' , 'Tesla' : 'Model S'}

print('\n******Moja Kolekcja******')
for marka, model in garaz.items():
    print(f'Marka: {marka} | Model: {model}')

print('\n******Posiadane Marki******')
for marka in garaz.keys():
    print(f'Mam w garazu samochod marki: {marka}', end=' ')
    pojazd = garaz[marka]
    print(f'{pojazd}')

print('\n******Posiadane Modele******')
for model in garaz.values():
    print(f'Mam w garazu pojazd: {model}')



auta_szczegoly = {
    "WA12345": {"marka": "Toyota", "rok": 2020, "przebieg": 50000}, 
    "KR67890": {"marka": "BMW", "rok": 20218, "przebieg": 120000}
    }

for rejestracja, dane in auta_szczegoly.items():
    print(f"Auto o numerze {rejestracja}")
    marka = dane["marka"]
    rok = dane["rok"]
    przebieg = dane["przebieg"]
    print(f"    -> {marka} z roku {rok} ma przebieg: {przebieg}")

licznik = 0
while licznik <5:
    print(f"Licznik wynosi: {licznik}")
    licznik += 0.5 #licznik = licznik + 1

szukane = "kia"

for auto in cars:
    if auto == szukane:
        print(f"Znaleziono: {auto}!")
        break
else:
    print(f"Niestety, {szukane} nie ma na liscie")