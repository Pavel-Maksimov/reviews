import json
from time import sleep

import telegram

from review_tracker.settings import BOT_TOKEN
from review_tracker.traker import read_reviews

bot = telegram.Bot(token=BOT_TOKEN)

with open('permitted_users.txt', 'r') as f:
    permitted_users = f.readlines()

for user in permitted_users:
    bot.send_message(user.strip(), 'Запуск бота')

sleep(5)
while True:
    data = read_reviews()
    reviews = 'Новых отзывов не найдено.'
    if len(data) > 0:
        reviews = json.dumps(
            data,
            indent=4,
            ensure_ascii=False
        )

    for user in permitted_users:
        bot.send_message(user.strip(), reviews)
    sleep(60*60*24)
