import ssl

from bs4 import BeautifulSoup
import requests, datetime as dt, smtplib


if dt.datetime.now().hour == 9:
    URL = "https://www.amazon.com/Piano-Exam-Pieces-2021-2022/dp/1786013207/ref=sr_1_1?keywords=grade+3+piano+abrsm&qid=1657271846&sprefix=grade+3+piano+%2Caps%2C829&sr=8-1"
    PARAMS = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
        "Accept-Language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
    }

    with requests.get(URL, headers=PARAMS) as connection:
        if connection.status_code != 200:
            connection.raise_for_status()
        result = connection.content

    soup = BeautifulSoup(result,"html.parser")
    price = soup.find_all(name = "span",class_="a-color-price", id="price")[0]
    # print(price.getText().strip("$"))

    if price < 9.99:
        with smtplib.SMTP_SSL("smtp.gmail.com",port=587,context= ssl.create_default_context()) as email:
            email.login("sender@gmail.com","password")
            email.sendmail("sender@gmail.com","receiver@gmail.com",f"Subject:Sale!\n\nThe Item that you want is on sale for {price} ")
