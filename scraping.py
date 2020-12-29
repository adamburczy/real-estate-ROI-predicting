from bs4 import BeautifulSoup
from requests import get
import csv

URL = 'https://www.otodom.pl/sprzedaz/mieszkanie/gliwice/?search%5Bregion_id%5D=12&search%5Bsubregion_id%5D=447&search%5Bcity_id%5D=175'

def parse_price(price):
    return float(price.replace(' ', '').replace('zł', '').replace(',', '.'))

page = get(URL)
bs = BeautifulSoup(page.content, 'html.parser')

file = open('real-estate-df.csv', 'w')
writer = csv.writer(file)

# write title row
writer.writerow(['Price', 'Rooms'])

for offer in bs.find_all('div', class_='offer-item-details'):
    price = parse_price(offer.find('li', class_='offer-item-price').get_text().strip())
    rooms = offer.find('li', class_='offer-item-rooms hidden-xs').get_text().strip()[0]
    writer.writerow([price, rooms])
    print(price, rooms)