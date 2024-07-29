import pandas as pd
from sqlalchemy import create_engine
import os

# Подключение к БД 
DB_USER = os.getenv('DB_USER', 'myuser')
DB_PASSWORD = os.getenv('DB_PASSWORD', 'mypassword')
DB_HOST = os.getenv('DB_HOST', 'db')  
DB_PORT = os.getenv('DB_PORT', '5433')  
DB_NAME = os.getenv('DB_NAME', 'mydatabase')

# Создание подключения к БД
engine = create_engine(f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}')

# Считывание данных из CSV
data = pd.read_csv('data.csv', sep=';')

# Загрузка данных в таблицу
data.to_sql('stock_data', engine, if_exists='replace', index=False)

print("Данные успешно загружены в БД.")
