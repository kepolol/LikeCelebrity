import sys
import os
sys.path.append("vkbot/")
from vk_bot import bot_response
from create_db import init_db, add_log
sys.path.append("cel_base/")
from add import inserter
from time import time


def test_many_attach():
    message = ""
    resp = bot_response(message, None)
    assert resp == u"Я могу обработать только одну фотографию."


def test_other_message1():
    message = "хай"
    resp = bot_response(message, None)
    assert resp == u"Не понимаю тебя.\nПопробуй отправить мне свою фотографию!"


def test_other_message2():
    message = "asdgsa"
    resp = bot_response(message, None)
    assert resp == u"Не понимаю тебя.\nПопробуй отправить мне свою фотографию!"


def test_inserter():
    os.remove('data/celebrities.db')
    os.system('python cel_base/script_create.py')
    inserter()
    assert time() - os.stat('data/celebrities.db')[8] < 30


def test_init_db():
    os.remove('data/database.db')
    init_db()
    assert time() - os.stat('data/database.db')[8] < 5


def test_add_log():
    add_log('request_date', 2, 'msg', 'resp', 2.3)
    assert time() - os.stat('data/database.db')[8] < 5
