import sys
sys.path.append("vkbot/")
from vk_bot import bot_response


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
