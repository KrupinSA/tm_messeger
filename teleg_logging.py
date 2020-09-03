import logging


MES_FORMAT = "%(asctime)s:[%(name)s]%(filename)s.%(funcName)s:%(levelname)s:%(message)s"
MES_BOT_FORMAT = "%(message)s"
LEVEL = logging.INFO

class TelegHandler(logging.Handler):
    def __init__(self, bot, chat_id):
        super().__init__()
        self.bot = bot
        self.chat_id = chat_id
        
    def emit(self, record):
        log = self.format(record)
        self.bot.send_message(self.chat_id, log)

def get_stream_handler():
    handler = logging.StreamHandler()
    formatter = logging.Formatter(MES_FORMAT)
    handler.setFormatter(formatter)
    handler.setLevel(LEVEL)
    return handler

def get_teleg_handler(bot, chat_id):
    handler = TelegHandler(bot, chat_id)
    formatter = logging.Formatter(MES_BOT_FORMAT)
    handler.setFormatter(formatter)
    handler.setLevel(LEVEL)
    return handler

def get_logger(name, bot=None, chat_id=None):
    logger = logging.getLogger(name)
    logger.addHandler(get_stream_handler())
    if bot and chat_id:
        logger.addHandler(get_teleg_handler(bot, chat_id))
    return logger