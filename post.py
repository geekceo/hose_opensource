import requests
from bs4 import BeautifulSoup

def post(url, key_value):
    r = requests.get(url+key_value)
    soup = BeautifulSoup(r.text, 'html.parser')
    print(soup.find_all('div', {'class': 'friends_list_bl'}))