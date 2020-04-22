import pandas as pd
from random import randint
import csv

def listappend():
    lista  = pd.read_csv('lista.csv')

    lista = lista.append({'imie':"adam",'pass':111111}, ignore_index=True)

    lista.to_csv('lista.csv', index_label='id', index=True, columns = ['imie','pass'])

pytanie = True
pytanie2 = True

while pytanie:
    wyswietlenie = input("Czy chcesz wyswietlic liste? (Y/N):" )
    if wyswietlenie.lower() == 'y':
        df = pd.read_csv('lista.csv', usecols=['id','imie', 'pass'])
        print(df.to_dict(orient='records'))
        pytanie = False

        while pytanie2:
            wyswietlenie2 = input("Czy chcesz dodac osobe? (Y/N):")
            if wyswietlenie2.lower() == 'y':
                name = input("Podaj imie: ")
                listappend()
                print('dodac imie z kolejnym indexem i random pass')
                pytanie2 = False
            elif wyswietlenie2.lower() == 'n':
                print('ok and bye')
                break
            else:
                print('please input Y or N')
    elif wyswietlenie.lower() == "n":
        print('ok, closing app, bye')
        break
    else:
        print('please input Y or N')


