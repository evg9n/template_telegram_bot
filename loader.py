from telebot.async_telebot import AsyncTeleBot
from telebot.storage import StateMemoryStorage

# Логгер
from loguru import logger

from os.path import abspath, join
# Константы
from constants import Constants


constants = Constants()
logger.add(
    abspath(join('logs', '{time:YYYY-MM-DD  HH.mm.ss}.log')),  # Путь к файлу логов с динамическим именем
    rotation=constants.ROTATION_LOGGER,  # Ротация логов каждый день
    compression="zip",  # Использование zip-архива
    level=constants.LEVEL_FILE_LOGGER,  # Уровень логирования
    format=constants.FORMAT_LOGGER,  # Формат вывода
    serialize=constants.SERIALIZE_LOGGER,  # Сериализация в JSON
)

# # Вывод лога в консоль
# logger.add(
#     sink=print,
#     level=constants.LEVEL_CONSOLE_LOGGER,
#     format=constants.FORMAT_LOGGER,
# )

logger.debug('Загрузка токен бота')
storage = StateMemoryStorage()
bot = AsyncTeleBot(token=constants.BOT_TOKEN, state_storage=storage)
logger.debug('Токен бота загружен')
