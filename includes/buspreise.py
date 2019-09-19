import requests, datetime
from bs4 import BeautifulSoup

class Buspreise():
    def getLowestPrice(self, start, destination, day):
        connection = {}
        connection['price'] = 500
        url = "http://www.fernbusse.de/busverbindungen/?from="+start+"&to="+destination+"&date="+day.strftime("%d.%m.%Y")+"&tab=&fromReturn=&toReturn=&dateReturn=18.09.2019"

        resp = requests.get(url)
        soup = BeautifulSoup(resp.text, 'lxml')

        elements = soup.findAll("tr", {"class":"line"})

        for element in elements:
            try:
                price = float(element.find("strong", {"class": "preis"}).contents[0].replace("€", "").replace(",", "."))
                duration = element.find("span", {"class": "dauer"}).contents[0]
                departure = element.find("span", {"class": "abfahrt"}).contents[0]
                provider = element.find("a", {"class":"fernbus_anbieter_link"}).contents[0]
                if connection['price'] > price:
                    connection['price'] = price
                    connection['duration'] = duration
                    connection['departure'] = departure
                    connection['provider'] = provider
            except:
                pass

        return connection

    def getHighestPrice(self, start, destination, day):
        connection = {}
        connection['price'] = 0
        connection['departure'] = False
        connection['provider'] = False
        connection['duration'] = False
        url = "http://www.fernbusse.de/busverbindungen/?from="+start+"&to="+destination+"&date="+day.strftime("%d.%m.%Y")+"&tab=&fromReturn=&toReturn=&dateReturn=18.09.2019"

        resp = requests.get(url)
        soup = BeautifulSoup(resp.text, 'lxml')

        elements = soup.findAll("tr", {"class":"line"})

        for element in elements:
            try:
                price = float(element.find("strong", {"class": "preis"}).contents[0].replace("€", "").replace(",", "."))
                duration = element.find("span", {"class": "dauer"}).contents[0]
                departure = element.find("span", {"class": "abfahrt"}).contents[0]
                provider = element.find("a", {"class":"fernbus_anbieter_link"}).contents[0]
                if connection['price'] < price and provider != 'Deutsche Bahn':
                    connection['price'] = price
                    connection['duration'] = duration
                    connection['departure'] = departure
                    connection['provider'] = provider
            except:
                pass

        return connection

    import requests, datetime
from bs4 import BeautifulSoup

class Buspreise():
    def getLowestPrice(self, start, destination, day):
        connection = {}
        connection['price'] = 500
        connection['departure'] = False
        connection['provider'] = False
        connection['duration'] = False
        url = "http://www.fernbusse.de/busverbindungen/?from="+start+"&to="+destination+"&date="+day.strftime("%d.%m.%Y")+"&tab=&fromReturn=&toReturn=&dateReturn=18.09.2019"

        resp = requests.get(url)
        soup = BeautifulSoup(resp.text, 'lxml')

        elements = soup.findAll("tr", {"class":"line"})

        for element in elements:
            try:
                price = float(element.find("strong", {"class": "preis"}).contents[0].replace("€", "").replace(",", "."))
                duration = element.find("span", {"class": "dauer"}).contents[0]
                departure = element.find("span", {"class": "abfahrt"}).contents[0]
                provider = element.find("a", {"class":"fernbus_anbieter_link"}).contents[0]
                if connection['price'] > price:
                    connection['price'] = price
                    connection['duration'] = duration
                    connection['departure'] = departure
                    connection['provider'] = provider
            except:
                pass

        return connection

    def getNextPrice(self, start, destination, day):
        connection = {}
        connection['price'] = 0
        connection['departure'] = '24:00'
        connection['provider'] = False
        connection['duration'] = False
        url = "http://www.fernbusse.de/busverbindungen/?from="+start+"&to="+destination+"&date="+day.strftime("%d.%m.%Y")+"&tab=&fromReturn=&toReturn=&dateReturn=18.09.2019"

        resp = requests.get(url)
        soup = BeautifulSoup(resp.text, 'lxml')

        elements = soup.findAll("tr", {"class":"line"})

        for element in elements:
            try:
                price = float(element.find("strong", {"class": "preis"}).contents[0].replace("€", "").replace(",", "."))
                duration = element.find("span", {"class": "dauer"}).contents[0]
                departure = element.find("span", {"class": "abfahrt"}).contents[0]
                provider = element.find("a", {"class":"fernbus_anbieter_link"}).contents[0]
                print(day.strftime("%H"))
                print(int(connection['departure'].split(':')[0]))
                print(int(departure.split(':')[0]))
                if int(day.strftime("%H")) < int(departure.split(':')[0]) and int(connection['departure'].split(':')[0]) > int(departure.split(':')[0]) and provider != 'Deutsche Bahn':
                    if int(connection['departure'].split(':')[0]) == int(departure.split(':')[0]):
                        if int(connection['departure'].split(':')[1]) > int(departure.split(':')[1]):
                            connection['price'] = price
                            connection['duration'] = duration
                            connection['departure'] = departure
                            connection['provider'] = provider
                    else:
                        connection['price'] = price
                        connection['duration'] = duration
                        connection['departure'] = departure
                        connection['provider'] = provider
            except:
                pass

        return connection
