import json
import os
#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Created by Selva<peratchiselvan@tuta.io>

from uuid import uuid4

from telegram.utils.helpers import escape_markdown

from telegram import InlineQueryResultArticle, ParseMode, \
    InputTextMessageContent
from telegram.ext import Updater, InlineQueryHandler, CommandHandler
import logging

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments bot and
# update. Error handlers also receive the raised TelegramError object in error.
def start(bot, update):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi, this bot is created for @dartlang_group by @selvasoft_ceo')


def help(bot, update):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Hi, this bot is created for @dartlang_group by @selvasoft_ceo')


def inlinequery(bot, update):
    """Handle the inline query."""
    query = update.inline_query.query.lower()
    results=[ ]
    #print(js.keys())
    if query in js.keys():
        l = js[query]
        print('{}\n{}\n{}'.format(query,l['desc'],l['url']))
        results.append(InlineQueryResultArticle(
            id=uuid4(),
            title=query,
            input_message_content=InputTextMessageContent('{}\n{}\n{}'.format(query,l['desc'],l['url']))))
    """for k,l in js.items():
        if str(k).startswith(query):
            results.append(InlineQueryResultArticle(
            id=uuid4(),
            title=k,
            input_message_content=InputTextMessageContent('{}\n{}\n'.format(k,l['desc',l['url']]))))
    """

    update.inline_query.answer(results)


def error(bot, update, error):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, error)


# Create the Updater and pass it your bot's token.
token = os.environ['TELEGRAM_TOKEN']
updater = Updater(token)
file1 = open('op.json')
js = json.load(file1)
#js = {"Container" : {"desc": "A convenience widget that combines common painting, positioning, and sizing widgets.","url": "https://docs.flutter.io/flutter/widgets/Container-class.html"},"Row" : {"desc": "Layout a list of child widgets in the horizontal direction.","url": "https://docs.flutter.io/flutter/widgets/Row-class.html"},"Column" : {"desc": "Layout a list of child widgets in the vertical direction.","url": "https://docs.flutter.io/flutter/widgets/Column-class.html"}}
# Get the dispatcher to register handlers
dp = updater.dispatcher

# on different commands - answer in Telegram
dp.add_handler(CommandHandler("start", start))
dp.add_handler(CommandHandler("help", help))

# on noncommand i.e message - echo the message on Telegram
dp.add_handler(InlineQueryHandler(inlinequery))

# log all errors
dp.add_error_handler(error)

# Start the Bot
updater.start_polling()

# Block until the user presses Ctrl-C or the process receives SIGINT,
# SIGTERM or SIGABRT. This should be used most of the time, since
# start_polling() is non-blocking and will stop the bot gracefully.
updater.idle()


