import requests
url = "https://www.iplt20.com/stats/2019"

page = requests.get(url)

from bs4 import BeautifulSoup

soup = BeautifulSoup(page.text, 'html.parser')

soup.find('table', class_ = 'standings-table__header')
