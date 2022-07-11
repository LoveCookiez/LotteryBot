import pandas as pd
import requests
import re
import fileHandlerModule
from bs4 import BeautifulSoup

urls = ["https://www.loto.ro/loto-new/newLotoSiteNexioFinalVersion/web/app2.php/jocuri/649_si_noroc/rezultate_extragere.html",
        "https://www.loto.ro/loto-new/newLotoSiteNexioFinalVersion/web/app2.php/jocuri/joker_si_noroc_plus/rezultate_extrageri.html",
        "https://www.loto.ro/loto-new/newLotoSiteNexioFinalVersion/web/app2.php/jocuri/540_si_super_noroc/rezultate_extrageri.html"]

lotteryGames = ["6 DIN 49", "NOROC", "5 DIN 40", "SUPER NOROC", "JOKER", "PLUS NOROC"]


def buildReport():
    fileHandlerModule.resetReport()
    currentLotteryGameIndex = 0
    for url in urls:
       noroc = False
       data = requests.get(url).text
       bs = BeautifulSoup(data, "lxml")
       for i in range(2):
            if (noroc):
                extractedLotteryNumbers = bs.find('div', {"class": "numere-extrase-noroc"})
            else:
                extractedLotteryNumbers = bs.find('div', {"class": "numere-extrase"})
                noroc = True

            extractedLotteryNumbers = re.findall(r'\d+', str(extractedLotteryNumbers))
            extractionDate = bs.find('div', {"class": "button-open-details"})
            extractionDate = re.findall(r'(?<=<span>)(.*)(?=</span>)', str(extractionDate))
            response = requests.get(url)
            tables = pd.read_html(response.text)
            listNumber = tables[i]
            tableResults = listNumber.values.tolist()
            tableResults = removeLastLineDuplicates(tableResults)
            info = "REZULTATE " + str(lotteryGames[currentLotteryGameIndex]) + str(extractionDate) + "\n" + "NUMERELE EXTRASE: "  + str(extractedLotteryNumbers) + "\n"
            for result in tableResults:
                info += str(result)
                info += "\n"
            info += "\n"
            fileHandlerModule.saveToFile(info, fileHandlerModule.files["report"])
            currentLotteryGameIndex = currentLotteryGameIndex + 1

    fileHandlerModule.overWriteFile(str(extractionDate), fileHandlerModule.files["dateTrack"])

def removeLastLineDuplicates(table):
    cols = len(table)
    table[cols - 1] = list(dict.fromkeys(table[cols - 1]))
    return table

if __name__ == "__main__":
    buildReport()
