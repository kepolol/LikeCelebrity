import sys
sys.path.append("vkbot/")
from vk_bot import bot_response


def test_response():
    message = ""
    resp = bot_response(message, None)
    assert resp == u"Я могу обработать только одну фотографию."
