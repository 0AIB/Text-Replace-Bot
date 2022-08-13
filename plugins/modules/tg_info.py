from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

BUTTONS = InlineKeyboardMarkup([[InlineKeyboardButton(text="UPDATE CHANNEL", url=f"https://t.me/Subhan011")]])

@Client.on_message(filters.private & filters.command("info"))
async def info(bot, update):
    
    text = f"""--<b>Information</b>--
<b>🙋🏻‍♂️ First Name :</b> {update.from_user.first_name}
<b>🧖‍♂️ Your Second Name :</b> {update.from_user.last_name if update.from_user.last_name else 'None'}
<b>🧑🏻‍🎓 Your Username :</b> {update.from_user.username}
<b>🆔 Your Telegram ID :</b> <code>{update.from_user.id}</code>
<b>🔗 Your Profile Link :</b> {update.from_user.mention}"""
    
    await update.reply_text(        
        text=text,
        disable_web_page_preview=True,
        reply_markup=BUTTONS
    )

@Client.on_message(filters.private & filters.sticker)
async def stickers(_, msg):
    await msg.reply(f"<b>This Sticker's ID is</b> \n <code>{msg.sticker.file_id}</code>", quote=True)

@Client.on_message(filters.private & filters.forwarded)
async def forwarded(_, msg):
    if msg.forward_from:
        text = "Forward detected! \n\n"
        if msg.forward_from.is_bot:
            text += "<b>Bot</b>"
        else:
            text += "<b>User</b>"
        text += f'\n{msg.forward_from.first_name} \n'
        if msg.forward_from.username:
            text += f'@{msg.forward_from.username} \nID : `{msg.forward_from.id}`'
        else:
            text += f'ID : <code>{msg.forward_from.id}</code>'
        await msg.reply(text, quote=True)
    else:
        hidden = msg.forward_sender_name
        if hidden:
            await msg.reply(
                f"Forward detected but unfortunately, {hidden} has enabled forwarding privacy, so I can't get their id",
                quote=True,
            )
        else:
            text = f"Forward Detected. \n\n"
            if msg.forward_from_chat.type == "channel":
                text += "<b>Channel</b>"
            if msg.forward_from_chat.type == "supergroup":
                text += "<b>Group</b>"
            text += f'\n{msg.forward_from_chat.title} \n'
            if msg.forward_from_chat.username:
                text += f'@{msg.forward_from_chat.username} \n'
                text += f'ID : <code>{msg.forward_from_chat.id}</code>'
            else:
                text += f'ID : <code>{msg.forward_from_chat.id}</code>'
            await msg.reply(text, quote=True)

