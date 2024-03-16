#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>╔════════════⦿\n├⋗ ᴏᴡɴᴇʀ : <a href='tg://user?id={2098973647}'>This Person</a>\n\n </a>\n├⋗ Help : <a href='https://t.me/AryanTeamUniverse/'>Aryan Via Owner </a>\n├⋗ Credits : <a href=https://t.me/Trippy_xt>𝐓𝐑𝐈𝐏𝐏𝐘</a>\n├⋗ Main Channel : <a href=https://t.me/teamUniverseOffical>TeamUniverse</a>\n├⋗ Support Group : <a href=https://t.me/AnimeUniverse_Chatt>Group Chat</a>\n╚═════════════════⦿</b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔒 Close", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
