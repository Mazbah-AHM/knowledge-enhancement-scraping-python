from unicodedata import name
from bs4 import BeautifulSoup

with open("home.html", 'r') as htmlFIle:
    content = htmlFIle.read()
    soup = BeautifulSoup(content, 'lxml')
    cards = soup.find_all('div', class_='card')
    for i in cards:
        name = i.h5.text
        btn = i.a.text
        print(f'{name} for {btn}')