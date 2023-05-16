
import logging
from aiogram import Bot, Dispatcher, executor, types
import config as cfg
import markups as nav
from db import Database

logging.basicConfig(level=logging.INFO)

bot = Bot(token=cfg.TOKEN)
dp = Dispatcher(bot)
db = Database('')


def check_sub_channel(chat_member):
    return chat_member['status'] != "left"


@dp.message_handler(commands=["mute"], commands_prefix="/")
async def mute(message: types.Message):
    if str(message.from_user.id) == cfg.ADMIN_ID:
        if not message.reply_to_message:
            await message.reply("This command should be answer on message!!")
            return

        mute_sec = int(message.text[6:])
        db.add_mute(message.reply_to_message.from_user.id, mute_sec)
        await message.bot.delete_message(cfg.CHAT_ID, message.message_id)
        await message.reply_to_message.reply(f"User was mute on {mute_sec} second")


@dp.message_handler(content_types=["new_chat_members"])
async def user_joined(message: types.Message):
    await message.answer("Welcome !!\nTo send messages subscribe to channel", reply_markup=nav.channelMenu)


@dp.message_handler()
async def mess_handler(message: types.Message):
    if not db.user_exists(message.from_user.id):
          db.add_user(message.from_user.id)

    if not db.mute(message.from_user.id):

        if check_sub_channel(await bot.get_chat_member(chat_id=cfg.CHANNEL_ID, user_id=message.from_user.id)):
            text = message.text.lower()
            for word in cfg.WORDS:
                if word in text:
                    await message.delete()

        else:
            await message.answer("Sorry, You`re not subscribed on the channel😢", reply_markup=nav.channelMenu)
            await message.delete()
    else:
        await message.delete()


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
# @dp.message_handler(commands=["test"], commands_prefix="/")
# async def test(message: types.Message):
#     await bot.send_message(message.from_user.id, f"ID: {message.from_user.id}")
