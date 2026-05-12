#listy

przemieszczenia = ["w_dol", "w_gore", "w_prawo"]
naprezenia = [1, 8, 3, 2, 14, 17]   #duplikaty sa dozwolone
mieszana = ["Maniek", 38, False]    #rozne typy danych

print(przemieszczenia)
print(naprezenia)
print(mieszana)

print(przemieszczenia[0])   #pierwszy
print(przemieszczenia[1])
print(przemieszczenia[-1])  #ostatni

print(type(naprezenia[0]))

przemieszczenia[1] = "w_lewo"
print(przemieszczenia)
przemieszczenia.append("w_gore")
print(przemieszczenia)
przemieszczenia.insert(2,"w_przód")
print(przemieszczenia)
przemieszczenia.remove("w_przód")
print(przemieszczenia)
ostatni = przemieszczenia.pop(1)
print(ostatni)
print(przemieszczenia)

przemieszczenia.extend(naprezenia)
print(przemieszczenia)

przemieszczenia.append([1,2]) #lista w liscie
print(przemieszczenia)
#przemieszczenia.remove()
print(przemieszczenia)
przemieszczenia.extend([1,2]) #lista dodaje pojedynczo elementy
print(przemieszczenia)

#listy wielowymiarowe

macierz = [ [1, 2, 3] , [4, 5, 6] , [7, 8, 9] ]
print(macierz)
print(macierz[1][2])
print(macierz[2][1])

macierz[2][1] = 100
print(macierz[2])

print(len(macierz[0]))

x = 5
y = x

x = 10
print(y)

x = "abc"
y = x

x = "xyz"
print(y)

x = [ "a" , "b" , "c" ]
y = x.copy() #tworzenie kopii obiektu, nie doda sie przypadkowo przez append nic do y

x.append("v") #normalnie y nie bedzie sie update'owal, ale jak dodajemy cos do listy to sie update'uje
x = [ "x" , "y" , "z" ]
print(y)
