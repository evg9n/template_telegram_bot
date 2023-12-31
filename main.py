import handlers
from loader import bot
from telebot.custom_filters import StateFilter
from telebot.types import BotCommand

from os import listdir, path, mkdir
from asyncio import run, gather

from loader import logger


DEFAULT_COMMANDS = (
    # ('start', "Запустить бота"),
    # Команды которые будут отображаться приклике на меню
)


async def set_commands():
    await bot.set_my_commands(
        [BotCommand(*i) for i in DEFAULT_COMMANDS]
        )


async def main():
    await bot.set_my_commands(
        [BotCommand(*i) for i in DEFAULT_COMMANDS]
    )
    bot.add_custom_filter(StateFilter(bot))
    await gather(bot.infinity_polling())


if __name__ == '__main__':
    logger.debug('Старт БОТ')
    if 'logs' not in listdir(path.abspath('.')):
        mkdir('logs')
        logger.debug('Создан каталог "logs"')

    run(main())
