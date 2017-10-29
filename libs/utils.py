# encoding: utf-8
"""
@author: xsren 
@contact: bestrenxs@gmail.com
@site: xsren.me

@version: 1.0
@license: Apache Licence
@file: utils.py
@time: 29/10/2017 5:24 PM

"""
import logging


class ColoredFormatter(logging.Formatter):
    def __init__(self, fmt=None):
        logging.Formatter.__init__(self, fmt=fmt)

    def format(self, record):
        COLORS = {
            'Black': '0;30',
            'Red': '0;31',
            'Green': '0;32',
            'Brown': '0;33',
            'Blue': '0;34',
            'Purple': '0;35',
            'Cyan': '0;36',
            'Light_Gray': '0;37',

            'Dark_Gray': '1;30',
            'Light_Red': '1;31',
            'Light_Green': '1;32',
            'Yellow': '1;33',
            'Light_Blue': '1;34',
            'Light_Purple': '1;35',
            'Light_Cyan': '1;36',
            'White': '1;37',
        }
        COLOR_SEQ = "\033[%sm"
        RESET_SEQ = "\033[0m"

        message = logging.Formatter.format(self, record)

        if record.levelno == logging.DEBUG:
            message = COLOR_SEQ % COLORS['White'] + message + RESET_SEQ
        elif record.levelno == logging.INFO:
            message = COLOR_SEQ % COLORS['Green'] + message + RESET_SEQ
            pass
        elif record.levelno == logging.WARNING:
            message = COLOR_SEQ % COLORS['Brown'] + message + RESET_SEQ
        elif record.levelno == logging.ERROR:
            message = COLOR_SEQ % COLORS['Red'] + message + RESET_SEQ
        elif record.levelno == logging.CRITICAL:
            message = COLOR_SEQ % COLORS['Purple'] + message + RESET_SEQ
        return message


import logging.handlers


def init_logger():
    logger = logging.getLogger("run_parse_url_server")
    logger.setLevel(logging.DEBUG)

    # file
    log_file_name = "run_parse_url_server.log"
    fh = logging.handlers.RotatingFileHandler(log_file_name, maxBytes=1024 * 1024 * 600, backupCount=3)
    color_formatter = ColoredFormatter(fmt='%(asctime)s %(funcName)s[line:%(lineno)d] [%(levelname)s]: %(message)s')
    fh.setFormatter(color_formatter)
    fh.setLevel(logging.DEBUG)
    logger.addHandler(fh)

    # stdout
    sh = logging.StreamHandler()
    color_formatter = ColoredFormatter(fmt='%(asctime)s %(funcName)s[line:%(lineno)d] [%(levelname)s]: %(message)s')
    sh.setFormatter(color_formatter)
    sh.setLevel(logging.DEBUG)
    logger.addHandler(sh)

    return logger


def run():
    pass


if __name__ == '__main__':
    run()
