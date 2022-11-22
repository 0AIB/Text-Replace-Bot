import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import pyrogram
from pyrogram import filters, Client
from translation import Translation
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from pyromod import listen
from pyrogram.errors import UserNotParticipant
from pyrogram.types import InputMediaPhoto,InputMediaDocument,InputMediaVideo,InputMediaAnimation,InputMediaAudio
from asyncio import TimeoutError
import os
PACK = filters.animation | filters.document| filters.video|filters.audio |filters.photo
if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config
else:
    from config import Config


#start buttons 

start_button=InlineKeyboardMarkup(
        [
              [
                  InlineKeyboardButton("Owner", url="https://t.me/Subhan011"),
                  InlineKeyboardButton("🛡 About", callback_data = "about_data")
              ], 
              [
                  InlineKeyboardButton("🤩 Help", callback_data = "help_data"),
                  InlineKeyboardButton("🔐 Close", callback_data = "close_data")
              ] 
        ]
)

# help buttons

help_button=InlineKeyboardMarkup(
        [
              [
                InlineKeyboardButton("Source", callback_data = "source_data")
              ], 
              [
                  InlineKeyboardButton("⏪ BACK", callback_data = "back_data"), 
                  InlineKeyboardButton("🔐 CLOSE", callback_data = "close_data")
              ]
        ]
) 

# about button

about_button=InlineKeyboardMarkup(
        [
              [
                  InlineKeyboardButton("⬇️ BACK", callback_data = "back_data"), 
                  InlineKeyboardButton("🔐 CLOSE", callback_data = "close_data")
              ], 
              [
                  InlineKeyboardButton("🤩 Help", callback_data = "help_data")
              ]
        ]
) 

# Source Button

source_button=InlineKeyboardMarkup(
        [
              [
                  InlineKeyboardButton("⏪ Back", callback_data = "back_data"), 
                  InlineKeyboardButton("🔐 Close", callback_data = "close_data")
              ]
        ]
) 



@Client.on_message(filters.command("start") & filters.private)
async def start(bot, cmd):
      await bot.send_message(
          chat_id = cmd.chat.id,
          text = Translation.START_TEXT.format(cmd.from_user.first_name), 
          reply_to_message_id = cmd.message_id,
          parse_mode = "markdown",
          disable_web_page_preview = True, 
          reply_markup = start_button
      )


@Client.on_message(filters.command("help") & filters.private)
async def help(bot, cmd):
      await bot.send_message(
          chat_id = cmd.chat.id,
          text = Translation.HELP_TEXT, 
          reply_to_message_id = cmd.message_id,
          parse_mode = "html",
          disable_web_page_preview = True,
          reply_markup = help_button           
      )


@Client.on_message(filters.command("about") & filters.private)
async def about(bot, cmd):
      await bot.send_message(
          chat_id = cmd.chat.id,
          text = Translation.ABOUT_TEXT, 
          reply_to_message_id = cmd.message_id,
          parse_mode = "markdown",
          disable_web_page_preview = True, 
          reply_markup = about_button
      )


@Client.on_message(filters.command("source") & filters.private)
async def about(bot, cmd):
      await bot.send_message(
          chat_id = cmd.chat.id,
          text = Translation.SOURCE_TEXT, 
          reply_to_message_id = cmd.message_id,
          parse_mode = "html",
          disable_web_page_preview = True, 
          reply_markup = source_button
      )      

@Client.on_message(filters.command('media_replace') & filters.private)
async def media_replace(client, message):
    await message.reply_text(
        text="Follow the steps...\n\n🌀First Send Me A Media That You Need To Edit/Replace The Other One " \
             "\n\n🌀Send The Link Of The Media That Will Be Replaced/Edited\nNB: Note both you & the bot " \
             "must be an admin in the targert channel",
        disable_web_page_preview=True,
        reply_to_message_id=message.message_id
    )    

# media replace
@Client.on_message(PACK  & filters.private)
async def media(client, message):
     if message.chat.id not in Config.AUTH_USERS:
        return
     if message.photo:
        file_id = message.photo.file_id
        mid = InputMediaPhoto(file_id, caption=message.caption and message.caption.html)

     elif message.document:
        file_id = message.document.file_id
        mid = InputMediaDocument(file_id, caption=message.caption and message.caption.html)

     elif message.video:
        file_id = message.video.file_id
        mid = InputMediaVideo(file_id, caption=message.caption and message.caption.html)

     elif message.animation:
        file_id = message.animation.file_id
        mid = InputMediaAnimation(file_id, caption=message.caption and message.caption.html)

     elif message.audio:
          file_id  = message.audio.file_id
          mid = InputMediaAudio(file_id, caption=message.caption and message.caption.html)
     else:
         print('no way')

     try:
         a = await client.ask(message.chat.id,'Now send me the link of the message of the channnel that you need to edit',
                    filters=filters.text, timeout=30)

     except TimeoutError:
           await message.reply_text(
             "```Session Timed Out. Resend the file to Start again```",
             parse_mode="md",
             quote=True
           )
           return
     link = a.text
     a = "-100"
     try:
         id = link.split('/')[4]
         msg_id = link.split('/')[5]
         cd = a + str(id)
         chid = int(cd)

     except:
          chid = link.split('/')[3]
          msg_id = link.split('/')[4]    
     try:
         is_admin=await client.get_chat_member(chat_id=chid, user_id=message.from_user.id)
     except UserNotParticipant:
          await message.reply("It seems you are not a member of this channel and hence you can't do this action.")
          return
     if not is_admin.can_edit_messages:
        await message.reply("You are not permited to do this, since you do not have the right to edit posts in this channel.")
        return
            
     try:
        await client.edit_message_media(
               chat_id = chid,
               message_id = int(msg_id),
               media = mid
              )
     except Exception as e:
           await message.reply_text(e)
           return
     await message.reply_text("**successfully Edited the media**",
             parse_mode="md",
             quote=True
           )
