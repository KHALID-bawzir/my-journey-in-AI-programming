import requests
from bs4 import BeautifulSoup
import re
from tabulate import tabulate
import json

def get_books_data():
    url = 'https://books.toscrape.com/catalogue/page-1.html'
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)

    if response.ok:
        soup = BeautifulSoup(response.content, 'html.parser')
        books = soup.find('ol', class_='row')

        re_name_book = r'title="([^"]+)"'
        names = re.findall(re_name_book, str(books))

        re_price_book = r'(£\d+\.\d+)'
        prices = re.findall(re_price_book, str(books))

        re_star_book = r'class="star-rating (\w+)"'
        stars = re.findall(re_star_book, str(books))

        star_number = {"One": '1/5', "Two": '2/5', "Three": '3/5', "Four": '4/5', "Five": '5/5'}
        stars = [star_number[s] for s in stars]

        data =zip(names, prices, stars)
        return data
    return False

def get_books_text():
    data = get_books_data()

    if data:
        with open('books_text.txt', 'w', encoding='utf-8') as f:
            f.write('all Book:' + '\n')
            f.write('_-_'*30 + '\n')
            table = tabulate(data,headers=['names','prices','stars'] ,tablefmt='heavy_outline')
            f.write(table)

def get_books_json():
    data = get_books_data()
    if data:
        books_json = [{'name':names , 'price': prices , 'star' : stars} for names, prices, stars in data]
        data_books_json = {'title' : 'all books:' , 'books' : books_json}
        with open('books_json.json', 'w', encoding='utf-8') as f:
            json.dump(data_books_json, f , ensure_ascii=False)

if __name__ == '__main__':
    get_books_text()
    get_books_json()
