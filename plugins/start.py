from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ForceReply, CallbackQuery
import humanize
from helper.txt import mr
from helper.database import  insert 
from helper.utils import not_subscribed 

@Client.on_message(filters.private & filters.create(not_subscribed))
async def is_not_subscribed(client, message):
    buttons = [[ InlineKeyboardButton(text="♻️ ᴊᴏɪɴ ᴍʏ ᴄʜᴀɴɴᴇʟ ♻️", url=client.invitelink) ]]
    text = "**ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴊᴏɪɴᴇᴅ ᴍʏ ᴄʜᴀɴɴᴇʟ 😔 ᴊᴏɪɴ ᴍʏ ᴄʜᴀɴɴᴇʟ ᴛᴏ ᴜsᴇ ᴍᴇ **"
    await message.reply_text(text=text, reply_markup=InlineKeyboardMarkup(buttons))
           
@Client.on_message(filters.private & filters.command(["start"]))
async def start(client, message):
    insert(int(message.chat.id))
    await message.reply_photo(
       photo="https://telegra.ph/file/4d4e5b31834d5f1398331.jpg",
       caption=f"""👋 ʜᴇʟʟᴏ {message.from_user.mention} \nɪ'ᴍ ᴀ sɪᴍᴘʟᴇ ʀᴇɴᴀᴍᴇʀ ʙᴏᴛ ᴡɪᴛʜ ᴘᴇʀᴍᴀɴᴇɴᴛ ᴛʜᴜᴍʙɴᴀɪʟ & ᴄᴜsᴛᴏᴍ ᴄᴀᴘᴛɪᴏɴ sᴜᴘᴘᴏʀᴛ! """,
       reply_markup=InlineKeyboardMarkup( [[
           InlineKeyboardButton("👼 ᴅᴇᴠᴇʟᴏᴘᴇʀ 👼", callback_data='dev')
           ],[
           InlineKeyboardButton('📢 ᴜᴘᴅᴀᴛᴇs 📢', url='https://t.me/MalluBotsYT'),
           InlineKeyboardButton('♻️ ᴄʜᴀɴɴᴇʟ ♻️', url='https://t.me/MalluHubYT')
           ],[
           InlineKeyboardButton('💫 ᴀʙᴏᴜᴛ 💫', callback_data='about'),
           InlineKeyboardButton('ℹ️ ʜᴇʟᴘ ℹ️', callback_data='help')
           ]]
          )
       )
    return

@Client.on_message(filters.private &( filters.document | filters.audio | filters.video ))
async def send_doc(client, message):
    file = getattr(message, message.media.value)
    filename = file.file_name
    filesize = humanize.naturalsize(file.file_size)
    fileid = file.file_id
    await message.reply_text(
        f"__ᴡʜᴀᴛ ᴅᴏ ʏᴏᴜ ᴡᴀɴᴛ ᴍᴇ ᴛᴏ ᴅᴏ ᴡɪᴛʜ ᴛʜɪs ғɪʟᴇ?__\n**ғɪʟᴇ ɴᴀᴍᴇ** :- `{filename}`\n**ғɪʟᴇ sɪᴢᴇ** :- `{filesize}`",
        reply_to_message_id = message.id,
        reply_markup = InlineKeyboardMarkup([[ InlineKeyboardButton("🖋️ ʀᴇɴᴀᴍᴇ 🖋️",callback_data = "rename")],
        [InlineKeyboardButton("✖️ ᴄᴀɴᴄᴇʟ ✖️",callback_data = "cancel")  ]]))


@Client.on_callback_query()
async def cb_handler(client, query: CallbackQuery):
    data = query.data 
    if data == "start":
        await query.message.edit_text(
            text=f"""👋 ʜᴇʟʟᴏ {query.from_user.mention} \nɪ'ᴍ ᴀ sɪᴍᴘʟᴇ ʀᴇɴᴀᴍᴇʀ ʙᴏᴛ ᴡɪᴛʜ ᴘᴇʀᴍᴀɴᴇɴᴛ ᴛʜᴜᴍʙɴᴀɪʟ & ᴄᴜsᴛᴏᴍ ᴄᴀᴘᴛɪᴏɴ sᴜᴘᴘᴏʀᴛ! """,
            reply_markup=InlineKeyboardMarkup( [[
                InlineKeyboardButton("👼 ᴅᴇᴠᴇʟᴏᴘᴇʀ 👼", callback_data='dev')                
                ],[
                InlineKeyboardButton('📢 ᴜᴘᴅᴀᴛᴇs 📢', url='https://t.me/MalluBotsYT'),
                InlineKeyboardButton('♻️ ᴄʜᴀɴɴᴇʟ ♻️', url='https://t.me/MalluHubYT')
                ],[
                InlineKeyboardButton('💫 ᴀʙᴏᴜᴛ 💫', callback_data='about'),
                InlineKeyboardButton('ℹ️ ʜᴇʟᴘ ℹ️', callback_data='help')
                ]]
                )
            )
        return
    elif data == "help":
        await query.message.edit_text(
            text=mr.HELP_TXT,
            reply_markup=InlineKeyboardMarkup( [[
               #⚠️ don't change source code & source link ⚠️ #
               InlineKeyboardButton("♻️ ɢʀᴏᴜᴘ ♻️", url="https://t.me/MalluHubGP")
               ],[
               InlineKeyboardButton("◀️ ʙᴀᴄᴋ ◀️", callback_data = "start"),
               InlineKeyboardButton("🔒 ᴄʟᴏsᴇ 🔒", callback_data = "close")
               ]]
            )
        )
    elif data == "about":
        await query.message.edit_text(
            text=mr.ABOUT_TXT.format(client.mention),
            disable_web_page_preview = True,
            reply_markup=InlineKeyboardMarkup( [[
               #⚠️ don't change source code & source link ⚠️ #
               InlineKeyboardButton("♻️ ɢʀᴏᴜᴘ ♻️", url="https://t.me/MalluHubGP")
               ],[
               InlineKeyboardButton("◀️ ʙᴀᴄᴋ ◀️", callback_data = "start"),
               InlineKeyboardButton("🔒 ᴄʟᴏsᴇ 🔒", callback_data = "close")
               ]]
            )
        )
    elif data == "dev":
        await query.message.edit_text(
            text=mr.DEV_TXT,
            reply_markup=InlineKeyboardMarkup( [[
               #⚠️ don't change source code & source link ⚠️ #
               InlineKeyboardButton("♻️ ɢʀᴏᴜᴘ ♻️", url="https://t.me/MalluHubGP")
               ],[
               InlineKeyboardButton("◀️ ʙᴀᴄᴋ ◀️", callback_data = "start"),
               InlineKeyboardButton("🔒 ᴄʟᴏsᴇ 🔒", callback_data = "close")
               ]]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass





