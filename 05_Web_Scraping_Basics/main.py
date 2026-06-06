import requests
from bs4 import BeautifulSoup
url = "https://www.amazon.eg/Casio-Collection-Unisex-Adults-Bracelet/dp/B000LAKYW8?crid=2XX82O53ZBBCN&dib=eyJ2IjoiMSJ9.nGMtJAEVNiZpRHSxtivvqg60lMWGEIA8Jr1iKV2VFtnGrNmvkUvt0yHqeSHyoiRQywHSIC9d9iow99BXK8-wGuvICwNL85PerGN9UOWsF_-D-dzTcLH_tB0keRmcHLObLtk4zAsJQZBQW-szST0USU7v7RJ9SExL9FQ_zlXhjjEVAhI0mEIW5EmRZq1GY5vVASDUb82Qq4S8xXgS3Bm3fIXYIOgg6lMaxCYZlY5zNslMSwbLLcul0Q7hCAIqa05HdvW9Nfc77LRFKMdIEZIJwVfUNOoEgVgb9nMv-1a3Qig.us5MoSpWZazOh4cgphloMgmtwAVjoOUsK8LvPURIXEg&dib_tag=se&keywords=ساعة+يد&qid=1734594961&sprefix=س%2Caps%2C392&sr=8-5"
headers = {'User_Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36'}
response = requests.get(url, headers=headers , params={'k':'ساعة+يد'})
soup = BeautifulSoup(response.content, 'html.parser')
title = soup.find('span' , id='productTitle')
price = soup.find('span' , class_='a-price')
whole_price = soup.find('span' , class_='a-price-whole')
img = soup.find('img' , class_=['a-dynamic-image' ,'a-stretch-vertical'])
ul = soup.find('ul' , class_=['a-unordered-list', 'a-nostyle a-vertical', 'a-spacing-none' ,'detail-bullet-list'])
rows = ul.find_all('li')
print(title.text)
print(price.text)
print(whole_price.text)
print(title.string.strip())
print(price.get_text())
print(img['src'])
print(rows)
