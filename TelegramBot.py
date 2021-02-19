#!python3
#-*- coding: utf-8 -*-

import telegram
from telegram.ext import Updater, CommandHandler, Filters, MessageHandler

class TelegramBot:
    def __init__(self, name):
        '''
        self.user_id : input your chat id
        self.token : input your token
        chat id check : https://api.telegram.org/bot'your token'/getUpdates
        '''
        self.name = name
        self.user_id = ''
        self.token = ''
        self.bot = telegram.Bot(token=self.token)
        self.updater = Updater(self.token)
        self.filters = Filters
        self.commandHandler = CommandHandler
        self.messageHandler = MessageHandler

    def stop(self):
        self.updater.start_polling()
        self.updater.dispatcher.stop()
        self.updater.job_queue.stop()
        self.updater.stop()

    def send_message(self, text):
        self.bot.sendMessage(chat_id =self.user_id, text=text)
