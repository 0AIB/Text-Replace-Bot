import os
from pyrogram import Client
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from plugins import *
from translation import Translation
if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config
else:
    from config import Config

# call_backs 

@Client.on_callback_query()
async def button(bot, cmd: CallbackQuery):
    cb_data = cmd.data
    if "about_data" in cb_data:
        await cmd.message.edit(
             text = Translation.ABOUT_TEXT,
             parse_mode="markdown", 
             disable_web_page_preview=True, 
             reply_markup=InlineKeyboardMarkup(
                 [
                     [
                      InlineKeyboardButton("⬇️ BACK", callback_data="back_data"),
                      InlineKeyboardButton("🔐 CLOSE", callback_data="close_data")
                     ]
 
                 ] 
             ) 
        )
    elif "help_data" in cb_data:
          await cmd.message.edit(
               text=Translation.HELP_TEXT,
               parse_mode="html", 
               disable_web_page_preview=True, 
               reply_markup=InlineKeyboardMarkup(
                   [
                       [
                        InlineKeyboardButton("SOURCE", callback_data = "source_data")
                       ],[
                        InlineKeyboardButton("Media Replace", callback_data = "media_replace_data")
                       ],[                       
                        InlineKeyboardButton("Current Caption", callback_data = "current_caption_data")
                       ],[                       
                        InlineKeyboardButton("⬇️ BACK", callback_data="back_data"),                                              
                        InlineKeyboardButton("🔐 CLOSE", callback_data="close_data")
                       ]
 
                   ] 
               ) 
          )
    elif "back_data" in cb_data:
          await cmd.message.edit(
               text=Translation.START_TEXT.format(cmd.from_user.first_name),
               parse_mode="markdown", 
               disable_web_page_preview=True, 
               reply_markup=InlineKeyboardMarkup(
                   [
                      
                       [
                        InlineKeyboardButton("Owner", url="https://t.me/subhan011"),
                        InlineKeyboardButton("About Me", callback_data="about_data")
                       ],
                       [
                        InlineKeyboardButton("💡 Help", callback_data="help_data"),
                        InlineKeyboardButton("🔐 Close", callback_data="close_data")
                       ]
                   ]
               )
          )
    elif "close_data" in cb_data:
          await cmd.message.delete()
          await cmd.message.reply_to_message.delete()

    elif "source_data" in cb_data:
          await cmd.message.edit(
               text=Translation.SOURCE_TEXT,
               parse_mode="html", 
               disable_web_page_preview=True, 
               reply_markup=InlineKeyboardMarkup(
                   [
                       [
                        InlineKeyboardButton("⬇️ BACK", callback_data="help_data"),
                        InlineKeyboardButton("🔐 CLOSE", callback_data="close_data")
                       ]
 
                   ] 
               ) 
          )
    elif "media_replace_data" in cb_data:
          await cmd.message.edit(
               text=Translation.MEDIA_REPLACE_TEXT,
               parse_mode="html", 
               disable_web_page_preview=True, 
               reply_markup=InlineKeyboardMarkup(
                   [
                       [
                        InlineKeyboardButton("⬇️ BACK", callback_data="help_data"),
                        InlineKeyboardButton("🔐 CLOSE", callback_data="close_data")
                       ]
 
                   ] 
               ) 
          )
    elif "current_caption_data" in cb_data:
          await cmd.message.edit(
               text=Translation.CURRENT_CAPTION.format(Config.CAPTION_TEXT, Config.CAPTION_POSITION),
               parse_mode="html", 
               disable_web_page_preview=True, 
               reply_markup=InlineKeyboardMarkup(
                   [
                       [
                        InlineKeyboardButton("⬇️ BACK", callback_data="help_data"),
                        InlineKeyboardButton("🔐 CLOSE", callback_data="close_data")
                       ]
 
                   ] 
               ) 
          )

