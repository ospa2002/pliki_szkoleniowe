#zadanie kalkulator
from tkinter import messagebox
from tkinter import simpledialog

ceny_pln = [45000 , 120000 , 32500 , 89900 , 55000]

suma_pln = sum(ceny_pln)
srednia_pln = sum(ceny_pln) / len(ceny_pln)

pytanie = messagebox.askyesno("Komunikat" , "Czy chcesz wyswietlic wyniki w walucie Euro?")

if pytanie == False:
    messagebox.showinfo("Komunikat",f"Suma cen: {suma_pln:.02f} PLN\nWartosc srednia: {srednia_pln:.02f} PLN")
else:
    kurs = simpledialog.askfloat("Kurs" , "Podaj kurs Euro:", minvalue = 0.5 , initialvalue = 4.1)
    if kurs:
        suma_euro = suma_pln / kurs
        srednia_euro = srednia_pln / kurs
        messagebox.showinfo("Komunikat",f"Suma cen: {suma_euro:.02f} EUR\nWartosc srednia: {srednia_euro:.02f} EUR\nKurs: {kurs:.02f} PLN")
    else:
        messagebox.showerror("Blad" , "Nie wybrano zadnej wartosci kursu")
        exit()



