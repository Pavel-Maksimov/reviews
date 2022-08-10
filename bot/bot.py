import json

import telegram
# from telegram.ext import Updater, Filters, ChatMemberHandler, CommandHandler, MessageHandler

from review_tracker.settings import BOT_TOKEN
from review_tracker.traker import read_reviews

bot = telegram.Bot(token=BOT_TOKEN)

with open('permitted_users.txt', 'r') as f:
    permitted_users = f.readlines()

for user in permitted_users:
    bot.send_message(user.strip(), 'Запуск бота')

while True:
    reviews = read_reviews()
    data_json = json.dumps(
        reviews,
        indent=4,
        ensure_ascii=False
    )

    for user in permitted_users:
        bot.send_message(user.strip(), data_json)


# updater = Updater(token=BOT_TOKEN)


# def say_echo(update, context):
#     pass


# def add(update, context):
#     print(update.message)
#     new_user = update.message.text.split()[-1]
#     permitted_users.append(new_user)
#     with open('permitted_users.txt', 'a') as f:
#         f.write('\n' + new_user)


# def hello(update, context):
#     print(update)


# updater.dispatcher.add_handler(CommandHandler('add', add))
# # updater.dispatcher.add_handler(MessageHandler(Filters.all, say_echo))
# updater.start_polling()
# updater.idle()
