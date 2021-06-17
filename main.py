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
    dp.add_handler(CommandHandler("rezultate", results_command))
    job_queue.run_repeating(cron_job, interval=300, first=1.0)
    updater.start_polling()
    updater.idle()


main()
