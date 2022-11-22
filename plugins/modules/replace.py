import os
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import asyncio
from pyrogram import Client, filters
from plugins import RE1TXT, RE2TXT, RE3TXT, RE4TXT, RE5TXT, RE6TXT, REPLACED
if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config
else:
    from config import Config


usercaption_position = Config.CAPTION_POSITION
caption_position = usercaption_position.lower()
caption_text = Config.CAPTION_TEXT


@Client.on_message(filters.channel & (filters.document | filters.video | filters.audio ) & ~filters.edited, group=-1)
async def editing(bot, message):
      try:
         media = message.document or message.video or message.audio
         caption_text = Config.CAPTION_TEXT
      except:
         caption_text = ""
         pass 
      if (message.document or message.video or message.audio): 
          if message.caption:                        
             file_caption = f"**{message.caption}**"                
          else:
             fname = media.file_name
             filename = fname.replace("_", ".")
             file_caption = f"`{filename}`"  
              
      try:
          if caption_position == "bottom":          
             await bot.edit_message_caption(
                 chat_id = message.chat.id, 
                 message_id = message.message_id,
                 caption = file_caption.replace(RE1TXT, REPLACED).replace(RE2TXT, REPLACED).replace(RE3TXT, REPLACED).replace(RE4TXT, REPLACED).replace(RE5TXT, REPLACED).replace(RE6TXT, REPLACED) + "\n\n" + caption_text, 
                 parse_mode = "markdown"
             )
          elif caption_position == "top":
             await bot.edit_message_caption(
                 chat_id = message.chat.id, 
                 message_id = message.message_id,
                 caption = caption_text + file_caption.replace(RE1TXT, REPLACED).replace(RE2TXT, REPLACED).replace(RE3TXT, REPLACED).replace(RE4TXT, REPLACED).replace(RE5TXT, REPLACED).replace(RE6TXT, REPLACED),
                 parse_mode = "markdown"
             )
          elif caption_position == "nil":
             await bot.edit_message_caption(
                 chat_id = message.chat.id,
                 message_id = message.message_id,
                 caption = caption_text, 
                 parse_mode = "markdown"
             ) 
      except:
          pass
