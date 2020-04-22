import pandas as pd
import csv

lista = pd.DataFrame({'imie' :['Bartek'],'password':[654321]})



lista.to_csv('lista.csv', columns=['imie','password'], index_label='id')