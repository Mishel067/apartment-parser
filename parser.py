import requests
import json
from typing import Any
import sqlite3
from types import TracebackType
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)

class Parser:
    def __init__(self, url: str) -> None:
        self.url = url
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 YaBrowser/26.8.0.0 Safari/537.36',
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'ru,en;q=0.9,pt;q=0.8',
            'Accept-Encoding': 'gzip, deflate, br, zstd',
            'Referer': 'https://www.nestpick.com/ru/dallas/',
            'Authority': 'www.nestpick.com',
            'Sec-Ch-Ua': '"Not;A=Brand";v="8", "Chromium";v="150", "YaBrowser";v="26.8", "Yowser";v="2.5"',
            'Sec-Ch-Ua-Mobile': '?0',
            'Sec-Ch-Ua-Platform': '"Windows"',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'Cache-Control': 'no-cache',
            'Pragma': 'no-cache',
            'Priority': 'u=1, i'
        }
    def parse(self, pages: int = 5) -> list[dict[str, Any]]:
        try:
            all_apartments = []
            for j in range(1, pages + 1):
                responce = requests.get(f'{self.url}&page={j}',
                                        headers=self.headers,
                                        timeout=5)
                responce = responce.json()['items']
                data = []
                for i in responce:
                    apartment = {'number_of_bedrooms': i.get('number_of_bedrooms', 'N/A'),
                                 'category': i.get('category', 'apartment'),
                                 'apartment_size': int(i.get('apartment_size', 0)),
                                 'price': i.get('price', {}).get('price', 0),
                                 'name': i.get('name', 'N/A'),
                                 'description': i.get('translations', {}).get('en', {}).get('description', 'Нет описания')[:200],
                                 'url': f"https://www.nestpick.com{i.get('property_details_url', '/')}",
                                 'photos': i.get('photos', [{}])[0].get('thumbnail', 'Нет фото')}
                    data.append(apartment)
                all_apartments.extend(data)
            logger.info('Data parsed.')
            return all_apartments
        except Exception as err:
            logger.error(err, exc_info=True)
            return []

class ToJson:
    def __init__(self, data: list[dict[str, Any]], filename: str) -> None :
        self.data = data
        self.filename = filename

    def __enter__(self):
        self.file = open(self.filename, 'w', encoding='utf-8')
        logger.info('File opened.')
        return self

    def to_json(self) -> None:
        json.dump(self.data, self.file, indent=2, ensure_ascii=False)
        logger.info('File created.')

    def __exit__(self, exc_type: type[BaseException] | None, exc_value: BaseException | None, exc_traceback: TracebackType | None) -> bool:
        if self.file:
            self.file.close()
        logger.info('File closed.')
        return False

class ToDataBase:
    def __init__(self, db_file: str, db_name: str | None = None) -> None:
        self.db_name = db_name
        self.db_file = db_file

    def __enter__(self):
        self.con = sqlite3.connect(self.db_file)
        self.con.row_factory = sqlite3.Row
        self.cur = self.con.cursor()
        if self.db_name:
            self.cur.execute(f'''CREATE TABLE IF NOT EXISTS {self.db_name} (id INTEGER PRIMARY KEY AUTOINCREMENT,
                                                            number_of_bedrooms INTEGER,
                                                            category TEXT,
                                                            apartment_size INTEGER,
                                                            price INTEGER,
                                                            name TEXT,
                                                            description TEXT,
                                                            url TEXT UNIQUE,
                                                            photos TEXT)''')
        self.con.commit()
        logger.info('Database connection established and schema verified.')
        return self

    def __exit__(self, exc_type: type[BaseException] | None, exc_value: BaseException, exc_traceback: TracebackType | None) -> bool:
         if exc_type:
            logger.error(f"Database error occurred: {exc_value}", exc_info=True)
         if hasattr(self, 'cur'):
             self.cur.close()
         if  hasattr(self, 'con'):
            self.con.close()
         logger.info('Database connection closed.')
         return False

    def to_db(self, data: list) -> None:
        for row in data:
            self.cur.execute(f'''INSERT OR IGNORE INTO {self.db_name} (number_of_bedrooms, category, apartment_size, price, name, description, url, photos) VALUES (?, ?, ?, ?, ?, ?, ?, ?)''',
                    (row['number_of_bedrooms'], row['category'], row['apartment_size'], row['price'], row['name'], row['description'], row['url'], row['photos']))
        self.con.commit()
        logger.info('Data successfully inserted into database.')

    def get_all(self, db_name: str) -> list[dict[str, Any]]:
        self.cur.execute(f'''SELECT * FROM {db_name}''')
        logger.info('All data returned.')
        return self.cur.fetchall()

if __name__ == '__main__':
    logger.info('Start...')
    parse = Parser('https://www.nestpick.com/search/api/?city=dallas&order=relevance&currency=USD&location=101724385').parse(5)
    with ToJson(parse, 'apartment_test.json') as js:
        js.to_json()
    with ToDataBase('apartment.db', 'apartment') as db:
        db.to_db(parse)
    logger.info('Success...')

