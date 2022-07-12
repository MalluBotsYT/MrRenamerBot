from pyrogram import Client, filters 
from helper.database import find, addcaption, delcaption 

@Client.on_message(filters.private & filters.command('set_caption'))
async def add_caption(client, message):
    if len(message.command) == 1:
       return await message.reply_text("**ɢɪᴠᴇ ᴍᴇ ᴀ ᴄᴀᴘᴛɪᴏɴ ᴛᴏ sᴇᴛ.\n\nᴇxᴀᴍᴘʟᴇ:- `/set_caption 📕 ғɪʟᴇɴᴀᴍᴇ: {filename}\n\n💾 sɪᴢᴇ: {filesize}\n\n⏰ ᴅᴜʀᴀᴛɪᴏɴ: {duration}`**")
    caption = message.text.split(" ", 1)[1]
    addcaption(int(message.chat.id), caption)
    await message.reply_text("**ʏᴏᴜʀ ᴄᴀᴘᴛɪᴏɴ sᴜᴄᴄᴇssғᴜʟʟʏ ᴀᴅᴅᴇᴅ ✅**")

@Client.on_message(filters.private & filters.command('del_caption'))
async def delete_caption(client, message): 
    #caption = fint(int(message.chat.id))[1]
    #if not caption:
       #return await message.reply_text("**You dont have any custom caption**")
    delcaption(int(message.chat.id))
    await message.reply_text("**ʏᴏᴜʀ ᴄᴀᴘᴛɪᴏɴ sᴜᴄᴄᴇssғᴜʟʟʏ ᴅᴇʟᴇᴛᴇᴅ ✅**")
                                       
@Client.on_message(filters.private & filters.command('see_caption'))
async def see_caption(client, message): 
    caption = find(int(message.chat.id))[1]
    if caption:
       await message.reply_text(f"<b><u>ʏᴏᴜʀ ᴄᴀᴘᴛɪᴏɴ:</b></u>\n\n`{caption}`")
    else:
       await message.reply_text("**ʏᴏᴜ ᴅᴏɴᴛ ʜᴀᴠᴇ ᴀɴʏ ᴄᴜsᴛᴏᴍ ᴄᴀᴘᴛɪᴏɴ**")
