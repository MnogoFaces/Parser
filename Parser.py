from bs4 import BeautifulSoup
import requests
import json

URL = input('Введите URL адрес сайта для парсинга: ')

headers = {
    'Accept': '*/*',
    'User-Agent': 'Mozilla/5.0 (compatible; ABrowse 0.4; Syllable)'
}

req = requests.get(URL, headers=headers) #Это мы отправили запрос на получение данных и притворились браузером, а не ботом.

src = req.text

print(src)

soup = BeautifulSoup(src, 'lxml')

all_ssilki = {}
for item in soup.find_all('a'):
    item_text = item.text
    item_href = item.get('href')
    print(f'{item_text}: {item_href}')
    
    all_ssilki[item_text] = item_href

with open ('all_ssilki.json','w') as file:
    json.dump(all_ssilki, file, indent=4, ensure_ascii=False)

with open ('all_ssilki.json') as file:
    all_spisok = json.load(file)

print(all_spisok)

