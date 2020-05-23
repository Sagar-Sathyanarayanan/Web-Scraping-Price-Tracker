import requests
from bs4 import BeautifulSoup
import smtplib
  
def send_mail():
    server = smtplib.SMTP('smtp.gmail.com' ,587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('YOUR_EMAIL@gmail.com','YOUR_PASSWORD')
    subject = "Price fell Down"
    body ="Check the link: https://www.amazon.in/Fitbit-FB507BKBK-Smartwatch-Tracking-Included/dp/B07TWFVDWT/ref=sr_1_1?crid=1HLGEN6SXUNUX&dchild=1&keywords=fitbit+versa+2&qid=1589976561&sprefix=fitbit+versa+%2Caps%2C291&sr=8-1"
    msg = f"Subject:{subject}\n\n{body}"
    server.sendmail(
        'sagartennis@gmail.com',
        'sagarthetennis10k@gmail.com',
        msg
    )
    print("Email Sent")
    server.quit

URL = 'https://www.amazon.in/Fitbit-FB507BKBK-Smartwatch-Tracking-Included/dp/B07TWFVDWT/ref=sr_1_1?crid=1HLGEN6SXUNUX&dchild=1&keywords=fitbit+versa+2&qid=1589976561&sprefix=fitbit+versa+%2Caps%2C291&sr=8-1'
headers = {"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"}
page = requests.get(URL,headers=headers)
soup =BeautifulSoup(page.content, 'html.parser')

title = soup.find(id="productTitle").get_text()
price =soup.find(id="priceblock_ourprice").get_text()
price_replace = price.replace(",", "")
coverted_price = price_replace.replace("₹","")
final_price = float(coverted_price[0:-3])
if(final_price < 19600):
    send_mail()
print(title.strip())
print(final_price)






