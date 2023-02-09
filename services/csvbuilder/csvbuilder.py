import csv
import os


class CsvFileBuilder():
        
    def get_csv(self, data, filename):
        with open(os.path.join(os.getcwd(), 'downloads', f'{filename}.csv'), 'wt', newline='', encoding="utf-8") as frecord:
             record = csv.DictWriter(frecord, list(data[0].keys()))
             record.writeheader()
             record.writerows(data)