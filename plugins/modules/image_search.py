import os
import requests
from pyrogram import Client, filters
from pyrogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    InlineQueryResultPhoto
)

@Client.on_inline_query()
async def search(bot, update):
    
    results = requests.get(
        "https://apibu.herokuapp.com/api/y-images?query=" + requests.utils.requote_uri(update.query)
    ).json()["result"][:50]
    
    answers = []
    for result in results:
        answers.append(
            InlineQueryResultPhoto(
                title=update.query.capitalize(),
                description=result,
                caption="Made by @subhan011",
                photo_url=result
            )
        )
    
    await update.answer(answers)

