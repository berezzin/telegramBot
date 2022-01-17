from bs4 import BeautifulSoup
import requests


def main():
    find_items = input('Что ищете?\n')
    url = f'https://www.21vek.by/search/?sa=&term={find_items}&searchId=BY_CLIENT_1642441348023092/'
    params = {'page': 1}
    n = 1

    while True:
        res = requests.get(url, params=params)
        soup = BeautifulSoup(res.text, 'lxml')

        items = soup.find_all('li', class_='cr-result__simple')
        for n, item in enumerate(items, start=n):
            if item.find('span', class_='result__name') is None:
                break
            itemName = item.find('span', class_='result__name').text
            itemLink = item.find('a', class_='result__link')['href']
            if item.find('span', class_='j-item-data') is not None:
                itemPrice = item.find('span', class_='j-item-data').text
            else:
                itemPrice = 'нет на складе'

            print(f'Товар № {n}')
            print(f"Название: {itemName}")
            print(f'Ссылка на товар: {itemLink}')
            print(f"Цена: {itemPrice}")
            print('')

        try:
            pageList = soup.find_all('a', class_='j-load_page cr-paging_link')
            nextPage = pageList[-1]
            if nextPage.text != '>':
                break
            else:
                params['page'] += 1
        except Exception as e:
            print(e)
            break


if __name__ == "__main__":
    main()
