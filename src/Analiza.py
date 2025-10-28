import pandas as pd
import matplotlib.pyplot as plt

#Pobieramy do kodu csv
df = pd.read_csv('/home/oskar/PycharmProjects/AnalizaSprzedazy/Data/Superstore Dataset.csv')

#Drukujemy jego informacje
print(df.head())
print(df.info())
print(df.describe())

#Ustawiamy w csv kolumny z datą żeby odczytywały jako date a nie jako text
df['Order date']=pd.to_datetime(df['Order date'])
