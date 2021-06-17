import os

files = {"report": "logLoto.txt", "dateTrack": "dateTrack.txt", "contacts": "contacts.txt"}
 
def saveToFile(info, document):
    savingFile = open(document, "a")
    if document == "contacts.txt":
        if not isFileEmpty(document):
            savingFile.write(",")
    savingFile.write(info)
    savingFile.close()

def overWriteFile(info, document):
    owFile = open(document, "w")
    owFile.write(info)
    owFile.close()

def getContactsList():
    contactsFile = open("contacts.txt", "r")
    contactsList = contactsFile.read().split(',')
    contactsFile.close()
        
    return contactsList

def addContact(contact):
    saveToFile(contact, "contacts.txt")
    
def resetReport():
    resetFile = open("logLoto.txt", "w")
    resetFile.close()
    resetChecker = open("dateTrack.txt", "w")
    resetChecker.close()

def isFileEmpty(file):
    return os.stat(file).st_size == 0

def getReport():
    if isFileEmpty("logLoto.txt"):
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

def initializeFiles():
    for k,v in files.items():
        if not os.path.exists(v):
            open(v, 'a').close()
            