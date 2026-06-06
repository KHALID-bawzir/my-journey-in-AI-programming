import requests
from bs4 import BeautifulSoup
import re

def get_books_data():
    headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36'}
    name_book = []
    price_book = []
    star_book = []
    for page in range(1, 3):
        url = f'https://books.toscrape.com/catalogue/page-{page}.html'
        response = requests.get(url, headers=headers)
        if response.ok:
            soup = BeautifulSoup(response.content, 'html.parser')
            books = soup.find('ol', class_='row')

            re_name_book = r'title="([^"]+)"'
            name_book.extend(re.findall(re_name_book, str(books)))

            re_price_book = r'(£\d+.\d+)'
            price_book.extend(re.findall(re_price_book, str(books)))

            re_star_book = r'class="star-rating (\w+)"'
            star_book.extend(re.findall(re_star_book, str(books)))

    star_number = {"One": 1,"Two": 2,"Three": 3,"Four": 4,"Five": 5}

    search_name = input("Enter book name: ").strip().lower()

    for i in range(len(name_book)):
        if search_name in name_book[i].lower():
            print("\n Book:", name_book[i])
            print("Price:", price_book[i])
            print("Stars:", star_number[star_book[i]])
            break
    else:
        print("sorry, Book not found")

get_books_data()


