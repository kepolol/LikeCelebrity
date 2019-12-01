#! /usr/bin/env python3
# -*- coding: utf-8 -*-
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from create_db import add_log
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import Feedback
from random import random
import vk_api
import urllib
import numpy
import cv2
import requests
import time
import re


engine = create_engine('sqlite:///database.db')
Session = sessionmaker(bind=engine)


def write_msg(user_id, message):
    vk.method('messages.send', {'user_id': user_id, 'message': message, 'random_id': random()})


def send_photo(user_id):
    a = vk.method("photos.getMessagesUploadServer")
    b = requests.post(a['upload_url'], files={'photo': open('send_test.jpg', 'rb')}).json()
    c = vk.method('photos.saveMessagesPhoto', {'photo': b['photo'], 'server': b['server'], 'hash': b['hash']})[0]
    d = "photo{}_{}".format(c["owner_id"], c["id"])
    vk.method("messages.send", {"peer_id": user_id, "attachment": d, 'random_id': random()})


def upload_photo(msg_id):
    msg = vk.get_api().messages.getById(message_ids=msg_id)
    photo_url = msg['items'][0]['attachments'][0]['photo']['sizes'][5]['url']
    req = urllib.request.urlopen(photo_url)
    arr = numpy.asarray(bytearray(req.read()), dtype=numpy.uint8)
    img = cv2.imdecode(arr, -1)
    cv2.imwrite("test.jpg", img)


def update_feedback(review):
    session = Session()
    if review == "Good":
        session.query(Feedback).update({Feedback.positive: Feedback.positive + 1}, synchronize_session=False)
    if review == "Bad":
        session.query(Feedback).update({Feedback.negative: Feedback.negative + 1}, synchronize_session=False)
    session.commit()
    session.close()


def get_statistics():
    session = Session()
    pos = session.query(Feedback.positive).filter(Feedback.id_ == 1).first()[0]
    neg = session.query(Feedback.negative).filter(Feedback.id_ == 1).first()[0]
    session.close()
    return pos, neg


def bot_response(message, user_id):
    if message == u"Ты ошибся...":
        update_feedback("Bad")
        return u"Попробуй отправить другое фото."
    elif message == u"Да это я! Похож!":
        update_feedback("Good")
        return u"Отлично!"
    elif message == "":
        return u"Я могу обработать только одну фотографию."
    elif re.search(r'\b[Пп]\ривет\b', message):
        name = vk.method('users.get', {'user_ids': user_id})[0]['first_name']
        return u"Привет, " + name + u"!\nОтправь мне свое фото, и я покажу, на кого из знаменитостей ты похож!"
    elif message == u"Покажи статистику отзывов":
        stat = get_statistics()
        good = u"количество положительных отзывов: {}.\n".format(stat[0])
        bad = u"Но в {} случаях пользователи посчитали, что я ошибся.".format(stat[1])
        return u"На данный момент " + good + bad
    else:
        return u"Не понимаю тебя.\nПопробуй отправить мне свою фотографию!"


def resp_work(user_id, message, start):
    resp = bot_response(message, user_id)
    write_msg(user_id, resp)
    dur_time = round(time.time() - start, 4)
    add_log(time.asctime(), event.user_id, event.message, resp, dur_time)


token = "01e71dc0db9523a795691bcdc5f346b834b2138deb7d6591b14af99e78ffe3119001c950623abb1edae46"

vk = vk_api.VkApi(token=token)

longpoll = VkLongPoll(vk)
keyboard = VkKeyboard(one_time=True)

keyboard.add_button(u'Ты ошибся...', color=VkKeyboardColor.NEGATIVE)
keyboard.add_button(u'Да это я! Похож!', color=VkKeyboardColor.POSITIVE)

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
        start = time.time()
        attach_data = event.attachments
        if attach_data:
            if len(attach_data) == 2:
                if attach_data["attach1_type"] == "photo":
                    write_msg(event.user_id, u"Фото принято, обрабатываю...")
                    upload_photo(event.message_id)
                    send_photo(event.user_id)
                    vk.method('messages.send', {'user_id': event.user_id, 'message': "Оцени!",'keyboard': keyboard.get_keyboard(), 'random_id': random()})
                    msg = vk.get_api().messages.getById(message_ids=event.message_id)
                    photo_url = msg['items'][0]['attachments'][0]['photo']['sizes'][5]['url']
                    resp = vk.method("photos.getMessagesUploadServer")['upload_url']
                    dur_time = time.time() - start
                    add_log(time.asctime(), event.user_id, str(photo_url), resp, dur_time)
                else:
                    resp = u"Ты пытаешься мне отправить что то не то...\nОтправь мне свою фотографию."
                    write_msg(event.user_id, resp)
                    dur_time = time.time() - start
                    add_log(time.asctime(), event.user_id, u"Отправленное вложение не является фото", resp, dur_time)
            else:
                resp = bot_response(event.message, event.user_id)
                write_msg(event.user_id, resp)
                dur_time = round(time.time() - start, 4)
                add_log(time.asctime(), event.user_id, u"Было отправлено более одного вложения", resp, dur_time)
        else:
            resp_work(event.user_id, event.message, start)
