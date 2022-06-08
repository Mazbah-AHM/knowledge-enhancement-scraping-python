from bs4 import BeautifulSoup

with open("home.html", 'r') as htmlFIle:
    content = htmlFIle.read()
    soup = BeautifulSoup(content, 'lxml')
    h5tags = soup.find_all('h5')
    for name in h5tags:
        print(name.text)