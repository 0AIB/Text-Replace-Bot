import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import pyrogram
from pyrogram import filters
from bot import autoforward
from config import Config
from translation import Translation
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

#start buttons 

start_button=InlineKeyboardMarkup(
        [
              [
                  InlineKeyboardButton("Follow On Github", url="https://github.com/lx575"),
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



@autoforward.on_message(filters.command("start") & filters.private)
async def start(bot, cmd):
      await bot.send_message(
          chat_id = cmd.chat.id,
          text = Translation.START_TEXT.format(cmd.from_user.first_name, Config.ADMIN_USERNAME), 
          reply_to_message_id = cmd.message_id,
          parse_mode = "markdown",
          disable_web_page_preview = True, 
          reply_markup = start_button
      )


@autoforward.on_message(filters.command("help") & filters.private)
async def help(bot, cmd):
      await bot.send_message(
          chat_id = cmd.chat.id,
          text = Translation.HELP_TEXT, 
          reply_to_message_id = cmd.message_id,
          parse_mode = "html",
          disable_web_page_preview = True,
          reply_markup = help_button           
      )


@autoforward.on_message(filters.command("about") & filters.private)
async def about(bot, cmd):
      await bot.send_message(
          chat_id = cmd.chat.id,
          text = Translation.ABOUT_TEXT, 
          reply_to_message_id = cmd.message_id,
          parse_mode = "markdown",
          disable_web_page_preview = True, 
          reply_markup = about_button
      )


@autoforward.on_message(filters.command("source", "repo") & filters.private)
async def about(bot, cmd):
      await bot.send_message(
          chat_id = cmd.chat.id,
          text = Translation.SOURCE_TEXT, 
          reply_to_message_id = cmd.message_id,
          parse_mode = "html",
          disable_web_page_preview = True, 
          reply_markup = source_button
      )      



# call_backs 

@autoforward.on_callback_query()
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
                       ],
                       [
                        InlineKeyboardButton("⬇️ BACK", callback_data="back_data"),
                        InlineKeyboardButton("🔐 CLOSE", callback_data="close_data")
                       ]
 
                   ] 
               ) 
          )
    elif "back_data" in cb_data:
          await cmd.message.edit(
               text=Translation.START_TEXT.format(cmd.from_user.first_name, Config.ADMIN_USERNAME),
               parse_mode="markdown", 
               disable_web_page_preview=True, 
               reply_markup=InlineKeyboardMarkup(
                   [
                      
                       [
                        InlineKeyboardButton("Follow On GitHub", url="https://Instagram.com/proavipatil"),
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
     
