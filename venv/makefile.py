import csv

listaOsob = [{'id': 0, 'imie':'Bartek', 'pass':123456},{'id': 1, 'imie':'Damian', 'pass':654321}]

plik = open('lista.csv','w')

for osoba in listaOsob:
    for key in osoba.keys():
        plik.write("%s,%s\n"%(key,osoba[key]))