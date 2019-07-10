import requests
from bs4 import BeautifulSoup


URL = "https://www.amazon.in/Kotion-Each-Wireless-Bluetooth-Headphone/dp/B01KX9O1H0/ref=sr_1_4_sspa?crid=1UMLAXRF7JXRQ&keywords=kotion+each+headphones&qid=1562738565&s=gateway&sprefix=kotion+%2Caps%2C296&sr=8-4-spons&psc=1"

headers= {"User-Agent" : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}

page = requests.get(URL, headers=headers )

soup = BeautifulSoup(page.content,'html.parser')

title = soup.find(id="productTitle").get_text()

print(title.strip())