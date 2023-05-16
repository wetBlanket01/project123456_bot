from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from src import config as cfg

# создание кнопки для перехода на канал
btnUrlChannel = InlineKeyboardButton(text="Go to Channel", url=cfg.CHANNEL_URL)
channelMenu = InlineKeyboardMarkup(row_width=1)

channelMenu.insert(btnUrlChannel)
