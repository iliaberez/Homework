
""" 
== OpenWeatherMap ==

OpenWeatherMap — онлайн-сервис, который предоставляет бесплатный API
 для доступа к данным о текущей погоде, прогнозам, для web-сервисов
 и мобильных приложений. Архивные данные доступны только на коммерческой основе.
 В качестве источника данных используются официальные метеорологические службы
 данные из метеостанций аэропортов, и данные с частных метеостанций.

Необходимо решить следующие задачи:

== Получение APPID ==
    Чтобы получать данные о погоде необходимо получить бесплатный APPID.
    
    Предлагается 2 варианта (по желанию):
    - получить APPID вручную
    - автоматизировать процесс получения APPID, 
    используя дополнительную библиотеку GRAB (pip install grab)

        Необходимо зарегистрироваться на сайте openweathermap.org:
        https://home.openweathermap.org/users/sign_up

        Войти на сайт по ссылке:
        https://home.openweathermap.org/users/sign_in

        Свой ключ "вытащить" со страницы отсюда:
        https://home.openweathermap.org/api_keys
        
        Ключ имеет смысл сохранить в локальный файл, например, "app.id"

        
== Получение списка городов ==
    Список городов может быть получен по ссылке:
    http://bulk.openweathermap.org/sample/city.list.json.gz
    
    Далее снова есть несколько вариантов (по желанию):
    - скачать и распаковать список вручную
    - автоматизировать скачивание (ulrlib) и распаковку списка 
     (воспользоваться модулем gzip 
      или распаковать внешним архиватором, воспользовавшись модулем subprocess)
    
    Список достаточно большой. Представляет собой JSON-строки:
{"_id":707860,"name":"Hurzuf","country":"UA","coord":{"lon":34.283333,"lat":44.549999}}
{"_id":519188,"name":"Novinki","country":"RU","coord":{"lon":37.666668,"lat":55.683334}}
    
    
== Получение погоды ==
    На основе списка городов можно делать запрос к сервису по id города. И тут как раз понадобится APPID.
        By city ID
        Examples of API calls:
        http://api.openweathermap.org/data/2.5/weather?id=2172797&appid=b1b15e88fa797225412429c1c50c122a

    Для получения температуры по Цельсию:
    http://api.openweathermap.org/data/2.5/weather?id=520068&units=metric&appid=b1b15e88fa797225412429c1c50c122a

    Для запроса по нескольким городам сразу:
    http://api.openweathermap.org/data/2.5/group?id=524901,703448,2643743&units=metric&appid=b1b15e88fa797225412429c1c50c122a


    Данные о погоде выдаются в JSON-формате
    {"coord":{"lon":38.44,"lat":55.87},
    "weather":[{"id":803,"main":"Clouds","description":"broken clouds","icon":"04n"}],
    "base":"cmc stations","main":{"temp":280.03,"pressure":1006,"humidity":83,
    "temp_min":273.15,"temp_max":284.55},"wind":{"speed":3.08,"deg":265,"gust":7.2},
    "rain":{"3h":0.015},"clouds":{"all":76},"dt":1465156452,
    "sys":{"type":3,"id":57233,"message":0.0024,"country":"RU","sunrise":1465087473,
    "sunset":1465149961},"id":520068,"name":"Noginsk","cod":200}    


== Сохранение данных в локальную БД ==    
Программа должна позволять:
1. Создавать файл базы данных SQLite со следующей структурой данных
   (если файла базы данных не существует):

    Погода
        id_города           INTEGER PRIMARY KEY
        Город               VARCHAR(255)
        Дата                DATE
        Температура         INTEGER
        id_погоды           INTEGER                 # weather.id из JSON-данных

2. Выводить список стран из файла и предлагать пользователю выбрать страну 
(ввиду того, что список городов и стран весьма велик
 имеет смысл запрашивать у пользователя имя города или страны
 и искать данные в списке доступных городов/стран (регуляркой))

3. Скачивать JSON (XML) файлы погоды в городах выбранной страны
4. Парсить последовательно каждый из файлов и добавлять данные о погоде в базу
   данных. Если данные для данного города и данного дня есть в базе - обновить
   температуру в существующей записи.


При повторном запуске скрипта:
- используется уже скачанный файл с городами;
- используется созданная база данных, новые данные добавляются и обновляются.


При работе с XML-файлами:

Доступ к данным в XML-файлах происходит через пространство имен:
<forecast ... xmlns="http://weather.yandex.ru/forecast ...>

Чтобы работать с пространствами имен удобно пользоваться такими функциями:

    # Получим пространство имен из первого тега:
    def gen_ns(tag):
        if tag.startswith('{'):
            ns, tag = tag.split('}')
            return ns[1:]
        else:
            return ''

    tree = ET.parse(f)
    root = tree.getroot()

    # Определим словарь с namespace
    namespaces = {'ns': gen_ns(root.tag)}

    # Ищем по дереву тегов
    for day in root.iterfind('ns:day', namespaces=namespaces):
        ...

"""
import json
import requests
from datetime import datetime
import sqlite3

api_key = "538e35eeb83472f75de0acb17c507855"
    
class ApiPost:
    post_get_weather = 'https://api.openweathermap.org/data/2.5/weather'
    post_get_weather_for_group = 'http://api.openweathermap.org/data/2.5/group'

    def get_weather_city_by_id(self, id):
        if isinstance(id, str):
            response = requests.get(f'{self.post_get_weather}?id={id}&appid={api_key}')
            return response
        
        if isinstance(id, list):
            str_id = ''
            for i in id:
                str_id += i + ','
            response = requests.get(f'{self.post_get_weather_for_group}?id={str_id}&units=metric&appid={api_key}')
            return response
        
    def get_data_city(self, name=None, country=None):
        with open('city.list.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
            for item in data:
                if name == item['name']:
                    id = item['id']
                    response = self.get_weather_city_by_id(str(id))
                    print(response)
                if country == item['country']:
                    id = item['id']
                    name = item['name']
                    country = item['country']

class CityWeather:
    def __init__(self, id, name, temperature, country):
        self.id = id
        self.name = name
        self.date = datetime.now()
        self.temperature = temperature
        self.country = country

def data_from_json(json):
    id = json['id']
    name = json['name']
    country = json['country']
    return CityWeather(id, name, None, country)

class Database:
    connection = sqlite3.connect('my_database.db')
    cursor = connection.cursor()
    
    def create_database(self):
        self.cursor.execute('CREATE TABLE IF NOT EXISTS CITY(id INTEGER PRIMARY KEY, name TEXT, date TEXT, temperature FLOAT, country TEXT)')
        self.connection.commit()

    def insert_city(self, city: CityWeather):
        self.cursor.execute('INSERT INTO CITY (id, name, date, temperature, country) VALUES (?, ?, ?, ?, ?, ?)', 
                            (city.id, city.name, str(city.date), city.temperature, city.country))
        self.connection.commit()

    def update_data(self, id, temperature):
        self.cursor.execute('UPDATE CITY SET temperature = ? date = ? WHERE id = ?', (temperature, str(datetime.now(), id)))

    def get_data(self, name=None, country=None, id=None):
        if name:
            self.cursor.execute('SELECT id, name , date, temperature, country FROM CITY WHERE name = ?', (name))
        if country:
            self.cursor.execute('SELECT id, name , date, temperature, country FROM CITY WHERE country = ?', (country))
        if id:
            self.cursor.execute('SELECT id, name , date, temperature, country FROM CITY WHERE id = ?', (id))
        return self.cursor.fetchall()
    
    def close_db(self):
        self.connection.close()

api = ApiPost()
db = Database()
data_input = input('Введите страну или название города на английсокм, например Kemerovo:\n')
api.get_data_city(data_input)
db.create_database()
db.close_db()
