import json
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
    report = fileHandlerModule.getReport()
    update.message.reply_text(report)

#TODO finish check contact if in list and add it if not
def checkContact(update):
    update_info = str(update)
    update_info = json.dumps(update_info)
    update_info = json.loads(update_info)
    contact = update_info["message"]["chat"]["id"]

def cron_job(context):
        if checkForUpdates():
            reportBuilder.buildReport()
            report = fileHandlerModule.getReport()
            context.bot.send_message(148886443, report)
            context.bot.send_message(1352882699, report)

def main():
    dp.add_handler(CommandHandler("rezultate", results_command))
    job_queue.run_repeating(cron_job,interval=300,first=1.0)
    updater.start_polling()
    updater.idle()

main()
