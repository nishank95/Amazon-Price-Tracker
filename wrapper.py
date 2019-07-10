import requests
from bs4 import BeautifulSoup
import smtplib


URL = "https://www.amazon.in/Kotion-Each-Wireless-Bluetooth-Headphone/dp/B01KX9O1H0/ref=sr_1_4_sspa?crid=1UMLAXRF7JXRQ&keywords=kotion+each+headphones&qid=1562738565&s=gateway&sprefix=kotion+%2Caps%2C296&sr=8-4-spons&psc=1"
URL = "https://www.amazon.in/Kotion-Each-Gaming-Headset-Channel/dp/B01J49LST4/ref=sr_1_38?crid=1UMLAXRF7JXRQ&keywords=kotion+each+headphones&qid=1562738565&s=gateway&sprefix=kotion+%2Caps%2C296&sr=8-38"

headers= {"User-Agent" : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}

page = requests.get(URL, headers=headers )

soup = BeautifulSoup(page.content,'html.parser')
def sendEmail(priority):
    if priority == 1:
        subject = "Check out fast item at cheap price"
    elif priority == 2:
        subject = "Price fell down"

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('nishanksamant95@gmail.com', '**YOUR_PASSWORD_HERE**')

    body = 'Check the Amazon link fpr the product here : https://www.amazon.in/Kotion-Each-Wireless-Bluetooth-Headphone/dp/B01KX9O1H0/ref=sr_1_4_sspa?crid=1UMLAXRF7JXRQ&keywords=kotion+each+headphones&qid=1562738565&s=gateway&sprefix=kotion+%2Caps%2C296&sr=8-4-spons&psc=1'

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'nishanksamant95@gmail.com',
        'nishanksamant95@gmail.com',
        msg
    )   
    print("EMAIL HAS BEEN SENT!!")
    server.quit() 


def checkPrice():
    page = requests.get(URL, headers=headers )

    soup = BeautifulSoup(page.content,'html.parser')

    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_ourprice").get_text() 

    converted_price = float(price.replace("," , '')[3:]) 

    if converted_price <= 700:
        sendEmail(1)
    elif converted_price < 900:
        sendEmail(2)


title = soup.find(id="productTitle").get_text()

print(title.strip()) 
checkPrice()