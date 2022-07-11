import requests
import re
from bs4 import BeautifulSoup
from datetime import datetime

url = "https://www.loto.ro/loto-new/newLotoSiteNexioFinalVersion/web/app2.php/jocuri/649_si_noroc/rezultate_extragere.html"

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
    if len(lastDate) == 0:
        return true
    lastDate = formatDate(lastDate)
    return datetime.strptime(formatDate(dateFound), "['%d/%m/%Y']") > datetime.strptime(formatDate(lastDate), "['%d/%m/%Y']")
    #return (formatDate(dateFound) > lastDate)

def formatDate(date):
    date = date.replace(".", "/")
    return date

checkForUpdates()

