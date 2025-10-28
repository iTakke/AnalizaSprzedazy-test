import pandas as pd
from sqlalchemy import create_engine

CSV_FILE = '/home/oskar/PycharmProjects/AnalizaSprzedazy/Data/Superstore Dataset.csv'
DATABASE_NAME = 'superstore.db'
TABLE_NAME = 'sales_data'

# 1. Ładowanie i czyszczenie
df = pd.read_csv(CSV_FILE, encoding='latin1')
df.columns = df.columns.str.replace(r'[^A-Za-z0-9_]+', '', regex=True).str.strip().str.replace(' ', '_')
# Konwersja numeryczna aby SQL działał poprawnie
df['Sales'] = df['Sales'].astype(str).str.replace('$', '', regex=False).str.replace(',', '', regex=False).astype(float)
df['Profit'] = df['Profit'].astype(str).str.replace('$', '', regex=False).str.replace(',', '', regex=False).astype(float)

# 2. Tworzenie bazy (plik) i ładowanie danych
# 'sqlite:///superstore.db' informuje SQLAlchemy, że ma użyć SQLite i utworzyć plik.
engine = create_engine(f'sqlite:///{DATABASE_NAME}')
df.to_sql(TABLE_NAME, engine, if_exists='replace', index=False)

print(f"Gotowe. Plik bazy danych '{DATABASE_NAME}' został utworzony!")