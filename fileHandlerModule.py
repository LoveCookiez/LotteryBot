import os

def saveToFile(info, document):
    savingFile = open(document, "a")
    savingFile.write("\n")
    savingFile.write(info)
    savingFile.close()

def overWriteFile(info, document):
    owFile = open(document, "w")
    owFile.write(info)
    owFile.close()

def resetReport():
    resetFile = open("logLoto.txt", "w")
    resetFile.close()
    resetChecker = open("dateTrack.txt", "w")
    resetChecker.close()

def checkIfFileIsEmpty(file):
    return os.stat(file).st_size == 0

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