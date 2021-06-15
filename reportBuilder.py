import pandas as pd
import requests
import re
import os
from bs4 import BeautifulSoup
from updateChecker import checkForUpdates

urls = ["https://www.loto.ro/jocuri/649_si_noroc/rezultate_extragere.html",
        "https://www.loto.ro/jocuri/540_si_super_noroc/rezultate_extrageri.html",
        "https://www.loto.ro/jocuri/joker_si_noroc_plus/rezultate_extrageri.html"]

jocuri = ["6 DIN 49", "NOROC", "5 DIN 40", "SUPER NOROC", "JOKER", "PLUS NOROC"]

files = {"report": "logLoto.txt", "dateTrack": "dateTrack.txt"}

def buildReport():
    resetReport()
    countJocuri = 0
    for url in urls:
       noroc = False
       data = requests.get(url).text
       bs = BeautifulSoup(data, "lxml")
       for i in range(2):
            if (noroc):
                numerele = bs.find('div', {"class": "numere-extrase-noroc"})
            else:
                numerele = bs.find('div', {"class": "numere-extrase"})
                noroc = True

            numerele = re.findall(r'\d+', str(numerele))
            dataExtragerii = bs.find('div', {"class": "button-open-details"})
            for row in dataExtragerii:
                ziua = re.findall(r'(?<=<span>)(.*)(?=</span>)', str(dataExtragerii))
            r = requests.get(url)
            tables = pd.read_html(r.text)
            listNumber = tables[i]
            tableResults = listNumber.values.tolist()
            tableResults = removeLastLineDuplicates(tableResults)
            info = "REZULTATE " + str(jocuri[countJocuri]) + str(ziua) + "\n" + "NUMERELE EXTRASE: "  + str(numerele) + "\n"
            for result in tableResults:
                info += str(result)
                info += "\n"
            saveToFile(info, files["report"])
            countJocuri = countJocuri + 1

    overWriteFile(str(ziua), files["dateTrack"])

def removeLastLineDuplicates(table):
    cols = len(table)
    table[cols - 1] = list(dict.fromkeys(table[cols - 1]))
    return table

def saveToFile(info, document):
    savingFile = open(document, "a")
    savingFile.write("\n")
    savingFile.write(info)
    savingFile.close()

def overWriteFile(info, document):
    owFile = open(document, "w")
    owFile.write(info)
    owFile.close()

def getReport():
    if checkIfFileIsEmpty("logLoto.txt"):
        return "A aparut o eroare. Te rog sa mai incerci o data."
    with open('logLoto.txt', 'r') as file:
        data = file.read()
    file.close()
    return data

def resetReport():
    resetFile = open("logLoto.txt", "w")
    resetFile.close()
    resetChecker = open("dateTrack.txt", "w")
    resetChecker.close()

def checkIfFileIsEmpty(file):
    return os.stat(file).st_size == 0


if __name__ == "__main__":
    buildReport()

