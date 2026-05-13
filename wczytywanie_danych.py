file = open("plik.txt" , "rt" , encoding= "utf8")

# zawartosc = file.read()
#print(zawartosc)

#zawartosc = file.read(10)
#print(zawartosc)

#for wiersz in file:
#    print(wiersz.strip())
'''
wiersz = file.readline()
while wiersz:
    print(wiersz.strip())
    wiersz = file.readline()

file.close()
'''
file = open("plik2.txt","w")
file.write("Zosia ma kotka.")
file.close()

file = open("plik2.txt","a", encoding= "utf8")
file.write("\nKrzys ma Jelcza.")
file.close()

