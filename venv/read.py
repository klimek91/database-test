import csv
import pandas as pd

#nowy = pd.DataFrame({'imie' :['Andrzej'],'pass' :[111111]})

#nowy.to_csv('lista.csv', index=True, columns=['imie','pass'], mode='a',header=False)




#lista = lista.append({"id": 2, 'imie' :'Janusz','pass':222222},ignore_index=True)

#nowy = pd.DataFrame({'imie' :'Janusz','pass':222222})

#lista = lista.append(nowy)

#lista = pd.concat([nowy,lista])
def listappend():
    lista  = pd.read_csv('lista.csv')

    lista = lista.append({'imie':name,'pass':111111}, ignore_index=True)

    lista.to_csv('lista.csv', index_label='id', index=True, columns = ['imie','pass'])

def addname():
