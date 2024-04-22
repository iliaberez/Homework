
""" OpenWeatherMap (экспорт)

Сделать скрипт, экспортирующий данные из базы данных погоды, 
созданной скриптом openweather.py. Экспорт происходит в формате CSV или JSON.

Скрипт запускается из командной строки и получает на входе:
    export_openweather.py --csv filename [<город>]
    export_openweather.py --json filename [<город>]
    export_openweather.py --html filename [<город>]
    
При выгрузке в html можно по коду погоды (weather.id) подтянуть 
соответствующие картинки отсюда:  http://openweathermap.org/weather-conditions

Экспорт происходит в файл filename.

Опционально можно задать в командной строке город. В этом случае 
экспортируются только данные по указанному городу. Если города нет в базе -
выводится соответствующее сообщение.

"""

import csv
import io
import json
import sqlite3
import pandas as pd

class CityWeather:
    def __init__(self, id, name, date, temperature, country):
        self.id = id
        self.name = name
        self.date = date
        self.temperature = temperature
        self.country = country

    def data_from_db(str_db):
        return CityWeather(
            id = str_db[0], 
            name = str_db[1],
            date = str_db[2], 
            temperature = str_db[3], 
            country = str_db[4]
        )
    
    def data_to_json(self):
        return {
            "id" : self.id,
            "name" : self.name,
            "date" : self.date,
            "temperature" : self.temperature,
            "country" : self.country,
        }
    
    def data_to_dataframe(self):
        return {
            "id" : [self.id],
            "name" : [self.name],
            "date" : [self.date],
            "temperature" : [self.temperature],
            "country" : [self.country],
        }


class Database:
    connection = sqlite3.connect('my_database.db')
    cursor = connection.cursor()

    def get_data(self, name):
        if name:
            self.cursor.execute('SELECT * FROM CITY WHERE name = ?', (name,))
        result = self.cursor.fetchall()
        if result == []:
            print(f'Данные по городу {name} не обнаружены в базе данных')
            return None
        else:
            return result[0]
    
    def close_db(self):
        self.connection.close()

db = Database()

temp_str = input('Введите название города ')

temp = db.get_data(name=temp_str)
data = None

if  temp:
    data = CityWeather.data_from_db(temp)
    temp_str = input('В какой формат экспортировать данные? ')

if str.lower(temp_str) == 'json':
    file_name = 'data_' + data.name + '.json'
    with io.open(file_name, 'w', encoding='utf-8') as file:
        file.write(json.dumps(data.data_to_json(), ensure_ascii=False))
        print(f'Данные по городу {data.name} успешно экспортированы в {file_name}')
        file.close

if str.lower(temp_str) == 'csv':
    file_name = 'data_' + data.name + '.csv'
    with open(file_name, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['id', data.id])
        writer.writerow(['name', data.name])
        writer.writerow(['data.', data.date])
        writer.writerow(['temperature', data.temperature])
        writer.writerow(['country', data.country])
        print(f'Данные по городу {data.name} успешно экспортированы в {file_name}')
    file.close()

if str.lower(temp_str) == 'html':
    file_name = 'data_' + data.name + '.html'
    df = pd.DataFrame(data.data_to_dataframe())
    f = open(file_name,'w')
    result = df.to_html()
    f.write(result)
    print(f'Данные по городу {data.name} успешно экспортированы в {file_name}')
    f.close()
