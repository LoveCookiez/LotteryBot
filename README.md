# LotteryBot

This is a Telegram Bot created to get the results from the romanian lottery extractions, which occurs on every thursday and sunday. This project has been created just as a fun and learning opportunity, and it also helps my mother who needs to fetch these results after every extraction.


1. In order to use the bot, first create a bot by following steps from here https://core.telegram.org/bots . You need to get the bot's token, which needs to be pasted inside credentials.py file
2. After the bot is created, search for it using the search icon inside Telegram App and write the bot name.
3. Navigate to the repository and run: python3 main.py . This depends on your default environment.
4. After you /start the bot, you can use the defined /rezultate command to get the latest lottery extractions from the main romanian lottery website.
5. I am currently hosting my bot on a RaspberryPI (https://www.raspberrypi.org/), as a daemon service that restarts itself whenever RaspberryPI reboots.
