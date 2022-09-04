import os
import telegram

from telegram.ext import MessageHandler, Filters
from telegram.ext import Dispatcher
from telegram.ext import InlineQueryHandler
from telegram.ext import Updater
from telegram import Update
from telegram.ext import CallbackContext
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
from telegram import InlineQueryResultArticle, InputTextMessageContent
from random import choice
from uwu import *
import re
from random import randint

kaomojiJoy = [" (* ^ ω ^)", " (o^▽^o)", " (≧◡≦)",
                 " ☆⌒ヽ(*\"､^*)chu", " ( ˘⌣˘)♡(˘⌣˘ )", " xD"]
kaomojiEmbarassed = [" (⁄ ⁄>⁄ ▽ ⁄<⁄ ⁄)..", " (*^.^*)..,",
                        "..,", ",,,", "... ", ".. ", " mmm..", "O.o"]
kaomojiConfuse = [" (o_O)?", " (°ロ°) !?", " (ーー;)?", " owo?"]
kaomojiSparkles = [" *:･ﾟ✧*:･ﾟ✧ ", " ☆*:・ﾟ ", "〜☆ ", " uguu.., ", "-.-"]

bot = telegram.Bot(token=os.environ["TELEGRAM_TOKEN"])
dispatcher = Dispatcher(bot=bot, update_queue=None, use_context=True)


def start(update: Update, context: CallbackContext):
    print(
        f"\\start request from user: {update.effective_user} in chat: {update.effective_chat}")
    context.bot.send_message(
        chat_id=update.effective_chat.id, text="Add me to groups and type /mock or /uwu followed by a message. For DMs, type @M0cking_Bot followed by your text and select either 'mock' or 'uwu'. Contact @incomple for feedback and suggestions.")


def helpCommand(update: Update, context: CallbackContext):
    print(
        f"\\help request from user: {update.effective_user} in chat: {update.effective_chat}")
    context.bot.send_message(
        chat_id=update.effective_chat.id, text="Add me to groups and type /mock or /uwu followed by a message. For DMs, type @M0cking_Bot followed by your text and select either 'mock' or 'uwu'. Contact @incomple for feedback and suggestions.")

def mockText(inputText):
    return ''.join(choice((str.upper, str.lower))(c) for c in inputText)

def mock(update: Update, context: CallbackContext):
    print(
        f"\\mock request from user: {update.effective_user} in chat: {update.effective_chat}")
    incoming_text=' '.join(context.args)
    if not (incoming_text.strip()):
        incoming_text="You gotta type something after the /mock command for me to mock!"
    mock_reply=mockText(incoming_text)
    context.bot.send_message(chat_id=update.effective_chat.id, text=mock_reply)


def uwu(update: Update, context: CallbackContext):
    print(
        f"\\uwu request from user: {update.effective_user} in chat: {update.effective_chat}")
    incoming_text=' '.join(context.args)
    if not (incoming_text.strip()):
        incoming_text="Hey silly willy, you have to type something after the /uwu command!"
    uwu_reply=uwuinate(incoming_text)
    context.bot.send_message(chat_id=update.effective_chat.id, text=uwu_reply)


def inline_mock(update: Update, context: CallbackContext):
    query=update.inline_query.query
    if not query:
        return
    results=[]
    results.append(
        InlineQueryResultArticle(
            id=1,
            title='mock',
            input_message_content=InputTextMessageContent(mockText(query))
        )
    )
    results.append(
        InlineQueryResultArticle(
            id=2,
            title="UwU",
            input_message_content=InputTextMessageContent(uwuinate(query))
        )
    )
    context.bot.answer_inline_query(update.inline_query.id, results)


def unknown(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id,
                            text="Sorry, I didn't understand that command.")


def webhook(request):
    if request.method == "POST":
        update=telegram.Update.de_json(request.get_json(force=True), bot)

        start_handler=CommandHandler('start', start)
        dispatcher.add_handler(start_handler)

        help_handler=CommandHandler('help', helpCommand)
        dispatcher.add_handler(help_handler)

        mock_handler=CommandHandler('mock', mock)
        dispatcher.add_handler(mock_handler)

        uwu_handler=CommandHandler('uwu', uwu)
        dispatcher.add_handler(uwu_handler)

        inline_mock_handler=InlineQueryHandler(inline_mock)
        dispatcher.add_handler(inline_mock_handler)

        # unknown_handler = MessageHandler(Filters.command, unknown)
        # dispatcher.add_handler(unknown_handler)

        dispatcher.process_update(update)
    return "ok"
