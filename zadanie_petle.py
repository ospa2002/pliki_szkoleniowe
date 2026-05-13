from tkinter import messagebox
from tkinter import simpledialog

firmy = {}
firmy["Nazwa firmy"] = ["Firma 1","Firma 2","Firma 3","Firma 4","Firma 5","Firma 6","Firma 7","xyz"]
firmy["Kurs akcji wczoraj"] = [16.48, 25.24,57.23,37.92,99.59,94.39,91.56,90]  
firmy["Kurs akcji dziś"] = [ 16.71,25.64 ,57.11, 38.16, 99.14, 94.52, 91.11 , 89 ]
firmy["Wzrost/Spadek"]=[None,None,None,None,None,None,None,None]
firmy["Wartość"]=[None,None,None,None,None,None,None,None]


ile = len(firmy["Nazwa firmy"])
print(ile)

komunikat_do_mb = ""

for indeks in range(ile):
    firma = firmy["Nazwa firmy"][indeks]
    kurs_wczorajszy = firmy["Kurs akcji wczoraj"][indeks]
    kurs_dzisiejszy = firmy["Kurs akcji dziś"][indeks]
    wzrost_spadek = firmy["Wzrost/Spadek"][indeks] = (kurs_dzisiejszy - kurs_wczorajszy) / kurs_dzisiejszy
    wartosc = firmy["Wartość"][indeks] = kurs_dzisiejszy - kurs_wczorajszy
    info = "spadl o"
    if wartosc > 0:
        info = "wzroslo o"
    komunikat = f"Firma: {firma}, kurs akcji {info}: {wartosc:.02f}"
    print(komunikat)
    komunikat_do_mb += komunikat + '\n'

messagebox.showinfo("Dane", komunikat_do_mb)
   
#praca domowa - wyswietlicz tabliczke mnozenia