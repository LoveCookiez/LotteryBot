import time
import requests
import re
from bs4 import BeautifulSoup

url = "https://www.loto.ro/jocuri/649_si_noroc/rezultate_extragere.html"

def checkForUpdates():
    data = requests.get(url).text
    bs = BeautifulSoup(data, "lxml")
    extractionDate = bs.find('div', {"class": "button-open-details"})
    day = str(re.findall(r'(?<=<span>)(.*)(?=</span>)',
str(extractionDate)))
    if updateRequired(day):
        testFile = open("testFile.txt", "w")
        testFile.write('aleluia')
        return True
    return False


def updateRequired(dateFound):
    savedFile = open("dateTrack.txt", "r")
    lastDate = str(savedFile.read())
    savedFile.close()
    formatedDate = formatDate(lastDate)
    return (formatDate(dateFound) > formatedDate)

def formatDate(date):
    date = date.replace(".", "/")
    return date

checkForUpdates()

