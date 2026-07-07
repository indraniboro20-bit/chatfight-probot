from pyrogram import Client, filters
from pyrogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton
)
from config import START_IMAGE, UPDATES_CHANNEL, SUPPORT_GROUP


@Client.on_message(filters.command("start") & filters.private)
async def start_cmd(client, message):

    text = f"""
👋 **Welcome {message.from_user.mention}**

🏆 Welcome to **ChatFight Clone Bot**

✨ Features:
• Global Ranking
• Group Ranking
• Daily / Weekly / Monthly Leaderboard
• Message Counter
• User Profile
• Statistics

➕ Add me to your group and start chatting!
"""

    buttons = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    "➕ Add Me",
                    url="https://t.me/YourBotUsername?startgroup=true"
                )
            ],
            [
                InlineKeyboardButton(
                    "📢 Updates",
                    url=UPDATES_CHANNEL
                ),
                InlineKeyboardButton(
                    "💬 Support",
                    url=SUPPORT_GROUP
                )
            ],
            [
                InlineKeyboardButton(
                    "⚙️ Settings",
                    callback_data="settings"
                )
            ]
        ]
    )

    await message.reply_photo(
        photo=START_IMAGE,
        caption=text,
        reply_markup=buttons
    )
