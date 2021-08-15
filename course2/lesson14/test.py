import requests
from bs4 import BeautifulSoup
import time


url = 'https://quotes.toscrape.com/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')

print(soup)
time.sleep(10)