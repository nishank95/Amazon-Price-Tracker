# Library for fetching data from URL
import requests
from bs4 import BeautifulSoup
# Library for sending emails through smtp protocol
import smtplib
import time

# Amazon URL for the designated product for checking the price
URL = "https://www.amazon.in/Kotion-Each-Gaming-Headset-Channel/dp/B01J49LST4/ref=sr_1_38?crid=1UMLAXRF7JXRQ&keywords=kotion+each+headphones&qid=1562738565&s=gateway&sprefix=kotion+%2Caps%2C296&sr=8-38"

# Client side (browser agent) header to send to the server
headers= {"User-Agent" : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}


# Function dealing with sending an email to the receiver based on the current price 
def sendEmail(priority):
    # Tampering the subject based on the product price
    if priority == 1:
        subject = "Check out fast item at cheap price"
    elif priority == 2:
        subject = "Price fell down"

    # Initialise the smtp server for sending an email using this server
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    # For encrypting communication on the protocol
    server.starttls()
    server.ehlo()
    # Signing in the host for sending an email 
    server.login('nishanksamant95@gmail.com', '**YOUR_PASSWORD_HERE**')

    # Mesaage Body
    body = 'Check the Amazon link fpr the product here : https://www.amazon.in/Kotion-Each-Gaming-Headset-Channel/dp/B01J49LST4/ref=sr_1_38?crid=1UMLAXRF7JXRQ&keywords=kotion+each+headphones&qid=1562738565&s=gateway&sprefix=kotion+%2Caps%2C296&sr=8-38'

    # Complete Message
    msg = f"Subject: {subject}\n\n{body}"
        
    # Send an email to the receiver
    server.sendmail(
        'nishanksamant95@gmail.com',
        'nishanksamant95@gmail.com',
        msg
    )   
    # Showw status on the terminal
    print("EMAIL HAS BEEN SENT!!")
    # Disconnect the server
    server.quit() 


def checkPrice():
    # Get the data from the reuested URL
    page = requests.get(URL, headers=headers )

    # Parse the content of the page in html format
    soup = BeautifulSoup(page.content,'html.parser')

    # Find the text within the element which has id as productTitle
    title = soup.find(id="productTitle").get_text()
    # Find the text within the element which has id as productPrice 
    price = soup.find(id="priceblock_ourprice").get_text() 

    # convert the price into float format from string format for parsing further 
    converted_price = float(price.replace("," , '')[3:]) 

    if converted_price <= 700:
        sendEmail(1)
    elif converted_price < 900:
        sendEmail(2)



# Call this function to check the product price
checkPrice()