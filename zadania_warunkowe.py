from tkinter import messagebox

odpowiedz = messagebox.askyesno("Question","Czy chcesz rozpoczac wycene rabatu?")

if odpowiedz == False:
    messagebox.showerror("Error", "Do widzenia ;)")
else:
    marka = input("Podaj nazwe pojazdu: ")
    print("Pojazd: " + marka)

    Cena = 100000

    if marka == "":
        print("Nie wpisano pojazdu")
    else:
        if marka == "Opel":
            Cena = Cena*0.85
        elif marka == "Skoda":
            Cena = Cena*0.82
        elif marka == "Audi":
            Cena = Cena*0.80
        else:
            Cena = Cena*0.95
        messagebox.showinfo("Info",f"Pojazd po rabacie kosztuje: {Cena:.2f} PLN")

'''
Praca domowa
1. Obliczona cena pojawia sie na ekranie - ma sie pojawic w ladnym okienku
2. Zapytaj, czy obliczac? Jesli tak, obliczamy. Jesli nie, exit()
3. 
'''

