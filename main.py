from telegram.ext import *
from updateChecker import checkForUpdates
import reportBuilder
import credentials
import fileHandlerModule

token = credentials.telegram_bot_token
updater = Updater(token, use_context=True)
job_queue = updater.job_queue
dp = updater.dispatcher

def results_command(update, context):
    update.message.reply_text("Verific rezultatele...")
    checkContact(update)
    report = fileHandlerModule.getReport()
    update.message.reply_text(report)

def start_command(update, context):
    update.message.reply_text("Salut, foloseste comanda /rezultate pentru a vedea ultima extragere de la Loteria Romana")
    update.message.reply_text("Ca sa folosesti comanda, doar scrie-mi /rezultate sau apasa pe butonul [/] din dreapta campului de scris")
    update.message.reply_text("Pentru diverse erori/comentarii : dumitru.vlad1996@gmail.com")
    checkContact(update)

def checkContact(update):
    contact = str(update.message.chat_id)
    contactList = fileHandlerModule.getContactsList()
    if contact not in contactList:
        fileHandlerModule.addContact(contact)

def cron_job(context):
    if checkForUpdates():
        reportBuilder.buildReport()
        report = fileHandlerModule.getReport()
        contactsList = fileHandlerModule.getContactsList()
        for contact in contactsList:
            context.bot.send_message(contact, report)

def main():
    fileHandlerModule.initializeFiles()
    dp.add_handler(CommandHandler("rezultate", results_command))
    dp.add_handler(CommandHandler("start", start_command))
    job_queue.run_repeating(cron_job, interval=300, first=1.0)
    updater.start_polling()
    updater.idle()


main()
