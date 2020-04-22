import csv
import pandas as pd

#nowy = pd.DataFrame({'imie' :['Andrzej'],'pass' :[111111]})

#nowy.to_csv('lista.csv', index=True, columns=['imie','pass'], mode='a',header=False)




#lista = lista.append({"id": 2, 'imie' :'Janusz','pass':222222},ignore_index=True)

#nowy = pd.DataFrame({'imie' :'Janusz','pass':222222})

#lista = lista.append(nowy)

#lista = pd.concat([nowy,lista])

lista  = pd.read_csv('lista.csv')
def reading():
    #lista = pd.read_csv('lista.csv')
    read_name = lista.imie[lista.id.idxmax]
    read_id = lista.id[lista.id.idxmax]
    read_password = lista.password[lista.id.idxmax]
    return print('Dodano osobe {} z ID {} i hasłem "{}"'.format(read_name, read_id,read_password))

reading()