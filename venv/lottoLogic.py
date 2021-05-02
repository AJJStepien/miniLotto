import requests as rq
from bs4 import BeautifulSoup
import csv
import logging

class Logic():

    def getLastMiniLottoScoreFromNet(self, url):
        page = rq.get(url).content
        soup = BeautifulSoup(page, 'html.parser')
        last = soup.find('div',attrs={'id':'ostatnie_ex'})
        result = last.text
        date = result[14:24]
        num1 = result[24:26]
        num2 = result[26:28]
        num3 = result[28:30]
        num4 = result[30:32]
        num5 = result[32:]
        print(date)
        print(num1,num2,num3,num4,num5)


    def getMiniLottiAllDb(self):
        db = rq.get(url="https://www.multipasko.pl/wyniki-csv.php?f=minilotto-sortowane").text
        try:
            file = open('db.txt','x')
            file.write(db)
            file.close()
        except:
            logging.info("plik istnieje")

        file = open('db.txt', 'r')
        with open('db.txt', mode='r') as csv_file:

            reader = csv.reader(csv_file, delimiter=";") #('db.txt', delimiter=';',dialect='excel')
            lineCounter = 0
            for row in reader:
                if lineCounter == 0:
                    lineCounter += 1
                else:
                    print("Losowanie z dnia " + str(row[1]) + "." + str(row[2])+ "." + str(row[3]) + ": " + str(row[4:]), end="\n")
                    lineCounter += 1

        file.close()
var = Logic()
var.getLastMiniLottoScoreFromNet("https://www.multipasko.pl/wyniki-lotto/express-lotek/")
var.getMiniLottiAllDb()