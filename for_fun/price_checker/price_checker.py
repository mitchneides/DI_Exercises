import requests
from bs4 import BeautifulSoup
import smtplib
import time


def get_price(URL):

    headers = {
        "User-Agent": 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'}

    html = requests.get(URL)
    soup = BeautifulSoup(html.text, features="html.parser")

    name = soup.find(id="productTitle").get_text()

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

    URL = 'https://www.amazon.com/Western-Digital-Elements-Portable-External/dp/B06W55K9N6/ref=lp_16225007011_1_1?s=computers-intl-ship&ie=UTF8&qid=1582117721&sr=1-1'

    while True:

        price = get_price(URL)

        if price < 65.00:
            send_mail(URL)

        time.sleep(28800)

