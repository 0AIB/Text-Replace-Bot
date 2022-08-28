# @lx575
import requests
from asyncio import sleep
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from plugins import OMDB_KEY
               
user = {"User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Mobile Safari/537.36 Edg/87.0.664.57"}

def get_movie_info(query):    
    try:
       url = f'http://www.omdbapi.com/?apikey={OMDB_KEY}&t={query}'
       resp = requests.get(url, headers=user).json()
       poster=resp['Poster']
       id=resp['imdbID']
       text=f"""📀 𝖳𝗂𝗍𝗅𝖾 : <b><u>{resp['Title']}</u></b>
                            
⏱️ 𝖱𝗎𝗇𝗍𝗂𝗆𝖾 : <b>{resp['Runtime']}</b>
🌟 𝖱𝖺𝗍𝗂𝗇𝗀 : <b>{resp['imdbRating']}/10</b>
🗳️ 𝖵𝗈𝗍𝖾𝗌 : <b>{resp['imdbVotes']}</b>
📆 𝖱𝖾𝗅𝖾𝖺𝗌𝖾 : <b>{resp['Released']}</b>
🎭 𝖦𝖾𝗇𝗋𝖾 : <b>{resp['Genre']}</b>
🎙 𝖫𝖺𝗇𝗀𝗎𝖺𝗀𝖾 : <b>{resp['Language']}</b>
🌐 𝖢𝗈𝗎𝗇𝗍𝗋𝗒 : <b>{resp['Country']}</b>
🎥 𝖣𝗂𝗋𝖾𝖼𝗍𝗈𝗋𝗌 : <b>{resp['Director']}</b>
📝 𝖶𝗋𝗂𝗍𝖾𝗋𝗌 : <b>{resp['Writer']}</b>
🔆 𝖲𝗍𝖺𝗋𝗌 : <b>{resp['Actors']}</b>
🗒 𝖯𝗅𝗈𝗍 : <code>{resp['Plot']}</code>"""

    except Exception as error:
        print(error)
    return poster, id, text

@Client.on_message(filters.command(["imdb", 'search']))
async def imdb_search(client, message):
    if ' ' in message.text:
        title = message.text.split(None, 1)        
        try:
            poster, id, text = get_movie_info(title)
            buttons=[[InlineKeyboardButton('🎟 𝖨𝖬𝖣𝖻', url=f"https://www.imdb.com/title/{id}"), InlineKeyboardButton('𝖥𝗈𝗅𝗅𝗈𝗐 𝖮𝗇 𝖦𝗂𝗍𝗁𝗎𝖻', url=f"https://GitHub.com/lx575")]]    
            m=await message.reply_text("𝖥𝗂𝗇𝖽𝗂𝗇𝗀 𝖣𝖾𝗍𝖺𝗂𝗅𝗌..")
            await message.reply_photo(photo=poster.replace("SX300",""), caption=text, reply_markup=InlineKeyboardMarkup(buttons))
            await sleep(2)
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
