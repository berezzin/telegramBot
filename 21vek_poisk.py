from bs4 import BeautifulSoup
import requests

find_items = input('Что ищете?')
url = f'https://www.21vek.by/search/?sa=&term={find_items}&searchId=BY_CLIENT_1642441348023092/'
params = {'page': 1}
n = 1

while True:
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'lxml')

    items = soup.find_all('li', class_='result__item')
    for n, item in enumerate(items, start=n):
        itemName = item.find('span', class_='result__name').text
        itemDescription = item.find('a', class_='result__link')['href']
        if item.find('span', class_='j-item-data') is not None:
            itemPrice = item.find('span', class_='j-item-data').text
        else:
            itemPrice = 'нет на складе'

        print(f'Товар № {n}')
        print(f"Название: {itemName}")
        print(f'Ссылка на товар: {itemDescription}')
        print(f"Цена: {itemPrice}")
        print('')

    pageList = soup.find_all('a', class_='j-load_page cr-paging_link')
    nextPage = pageList[-1]
    if nextPage.text != '>':
        break
    else:
        url = nextPage['href']
