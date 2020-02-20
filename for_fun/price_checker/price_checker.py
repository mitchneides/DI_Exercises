import urllib3
from bs4 import BeautifulSoup
import smtplib
import time


http = urllib3.PoolManager()
r = http.request('GET', 'http://httpbin.org/robots.txt')


def get_price(URL):

    headers = {
        "User-Agent": 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'}


    http = urllib3.PoolManager()
    r = http.request('GET', URL, headers=headers)

    soup = BeautifulSoup(r.data, features="html.parser")
    print(soup)
    # name = soup.find(id="productTitle").get_text()

    price = soup.find(id="priceblock_ourprice").get_text()

    price = float(price[1::])
    return price


def send_mail(link):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('pyprojectim20@gmail.com', 'rpsndxwsroqhdvws')

    subject = "Price fell down!"
    body = f"Check the amazon link: {link}"

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail('pyprojectim20@gmail.com', 'pyprojectim20@gmail.com', msg)
    print("Email has been sent")

    server.quit()


if __name__ == "__main__":

    URL = 'https://www.amazon.com/YABER-Projector-Support-Compatible-Smartphone/dp/B07WS7XFLG/ref=sr_1_6?keywords=projector&qid=1582184955&sr=8-6'

    while True:

        price = get_price(URL)

        if price < 265.00:
            send_mail(URL)

        time.sleep(28800)

