import pandas as pd
import csv

lista = pd.DataFrame({'imie' :['Bartek'],'pass':[654321]})



lista.to_csv('lista.csv', columns=['imie','pass'])