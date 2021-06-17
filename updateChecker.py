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
    return updateRequired(day)

def updateRequired(dateFound):
    savedFile = open("dateTrack.txt", "r")
    lastDate = str(savedFile.read())
    savedFile.close()
    lastDate = formatDate(lastDate)
    return (formatDate(dateFound) > lastDate)

def formatDate(date):
    date = date.replace(".", "/")
    return date

checkForUpdates()

