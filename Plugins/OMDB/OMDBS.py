# @lx575
from bot import autoforward
from asyncio import sleep
from Plugins.OMDB import get_movie_info
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
               
@autoforward.on_message(filters.command(["imdb", 'search']))
async def imdb_search(client, message):
    if ' ' in message.text:
        r, title = message.text.split(None, 1)        
        try:
            poster, id, text = get_movie_info(title)
            buttons=[[InlineKeyboardButton('🎟 𝖨𝖬𝖣𝖻', url=f"https://www.imdb.com/title/{id}"), InlineKeyboardButton('𝖥𝗈𝗅𝗅𝗈𝗐 𝖮𝗇 𝖦𝗂𝗍𝗁𝗎𝖻', url=f"https://GitHub.com/lx575")]]    
            m=await message.reply_text("𝖥𝗂𝗇𝖽𝗂𝗇𝗀 𝖣𝖾𝗍𝖺𝗂𝗅𝗌..")
            await message.reply_photo(photo=poster.replace("SX300",""), caption=text, reply_markup=InlineKeyboardMarkup(buttons))
            await sleep(1)
            await m.delete()                                                          
        except ValueError:
            m=await message.reply_text("𝖲𝗈𝗋𝗋𝗒,\n𝖨 𝖢𝖺𝗇'𝗍 𝖥𝗂𝗇𝖽 𝖯𝗈𝗌𝗍𝖾𝗋𝗌.\n𝖲𝖾𝗇𝖽𝗂𝗇𝗀 𝖠𝗏𝖺𝗂𝗅𝖺𝖻𝗅𝖾 𝖣𝖾𝗍𝖺𝗂𝗅𝗌..")
            await message.reply_text(text=text, reply_markup=InlineKeyboardMarkup(buttons))
            await sleep(4)
            await m.delete()
        except Exception as e:
            buttons=[[InlineKeyboardButton('🔍 𝖲𝖾𝖺𝗋𝖼𝗁 𝖮𝗇 𝖦𝗈𝗈𝗀𝗅𝖾.', url=f'https://google.com/search?q={title.replace(" ","+")}')]]
            await message.reply_text(text="𝖢𝗈𝗎𝗅𝖽𝗇'𝗍 𝖥𝖾𝗍𝖼𝗁 𝖣𝖾𝗍𝖺𝗂𝗅𝗌\n𝖳𝗋𝗒 𝖳𝗈 𝖢𝗁𝖾𝖼𝗄 yo𝗎𝗋 𝖲𝗉𝖾𝗅𝗅𝗂𝗇𝗀.", reply_markup=InlineKeyboardMarkup(buttons))  
            await m.delete()   
            print(e)
