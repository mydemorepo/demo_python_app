import csv
import os


# Об'єкт класу CsvFileBuilder використовується для 
# запису вхідних данних у CSV файл.
class CsvFileBuilder():
    
# Функція список словників якиї містить дані з таблиці та назву таблиці
# та записує їх у CSV файл.   
    def get_csv(self, data, filename):
        with open(os.path.join(os.getcwd(), 'downloads', f'{filename}.csv'), 'wt', newline='', encoding="utf-8") as frecord:
             record = csv.DictWriter(frecord, list(data[0].keys()))
             record.writeheader()
             record.writerows(data)
