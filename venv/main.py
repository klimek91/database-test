import pandas as pd
from random import randint
import csv
#lista  = pd.read_csv('lista.csv')

def listappend():
    password = randint(100000,999999)
    lista  = pd.read_csv('lista.csv')
    lista = lista.append({'imie':name,'password':password}, ignore_index=True)
    lista.to_csv('lista.csv', index_label='id', index=True, columns = ['imie','password'])

def reading():
    lista = pd.read_csv('lista.csv')
    read_name = lista.imie[lista.id.idxmax]
    read_id = lista.id[lista.id.idxmax]
    read_password = lista.password[lista.id.idxmax]
    return print('Dodano osobe {} z ID {} i hasłem "{}"'.format(read_name, read_id,read_password))


pytanie = True
pytanie2 = True

while pytanie:
    wyswietlenie = input("Czy chcesz wyswietlic liste? (Y/N):" )
    if wyswietlenie.lower() == 'y':
        df = pd.read_csv('lista.csv', usecols=['id','imie', 'password'])
        print(df.to_dict(orient='records'))
        pytanie = False
        while pytanie2:
            wyswietlenie2 = input("Czy chcesz dodac osobe? (Y/N):")
            if wyswietlenie2.lower() == 'y':
                name = input("Podaj imie: ")
                listappend()
                reading()
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


