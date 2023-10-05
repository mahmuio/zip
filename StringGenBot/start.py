from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

from config import OWNER_ID


def filter(cmd: str):
    return filters.private & filters.incoming & filters.command(cmd)

@Client.on_message(filter("start"))
async def start(bot: Client, msg: Message):
    me2 = (await bot.get_me()).mention
    await bot.send_message(
        chat_id=msg.chat.id,
        text=f"""⎚¦ اهلا بك عيزيزي بي بوت تربون ❤️‍🔥
⎚¦ يمكنك استخراج التلي❤️‍🔥

⎚¦ترمكس تلثيون الحسبات❤️‍🔥

⎚¦ ترمكس تلثون البوتات❤️‍🔥

⎚¦ بايروجرا ميوزك البوتات❤️‍🔥

⎚¦ بايروجرا ميوزك البوتات❤️‍🔥

⎚¦ تم انشاء البوت بواسطة❤️‍🔥 [ㅤ𓏺 ˛ َِ 𝐓𝐀𝐑𝐁𝐎𝐔𝞝𝐍.. 🧑‍💻 ˼ ](https://t.me/W_X_E1)""",

        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text="[{اضـعـط لـبـدا اسـتـخـراج الـكـود}]  ", callback_data="generate")
                ],
                [
                    InlineKeyboardButton("♥️️ قنات الـــمــطــور❤️‍🔥😈 ️", url="https://t.me/ADXG25"),
                    InlineKeyboardButton("مــطـور الـبـوت ❤️‍🔥ُْٖ", user_id=OWNER_ID)
                ]
            ]
        ),
        disable_web_page_preview=True,
    )
