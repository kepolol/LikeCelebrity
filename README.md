# LikeCelebrity [![Build Status](https://travis-ci.org/kepolol/LikeCelebrity.svg?branch=master)](https://travis-ci.org/kepolol/LikeCelebrity) [![Coverage Status](https://coveralls.io/repos/github/kepolol/LikeCelebrity/badge.svg)](https://coveralls.io/github/kepolol/LikeCelebrity)

Бот для социальной сети vk.com позволяет находить по пользовательской фотографии наиболее похожую "звезду".

# Участники проекта
## Создатели:
* [Быков Антон](https://github.com/Bykov25) - WEB сервис
* [Леонов Иван](https://github.com/kepolol) - ML сервис
* [Терёхин Артём](https://github.com/VudiRB) - ML сервис
* [Уткин Илья](https://github.com/BLOOMFLARK) - ML сервис
## Менторы:
* Баранов Михаил - компания Mail.ru Group
* Ефимов Владислав - компания Mail.ru Group

# Данные
* [Celebrity Face Recognition Dataset](https://github.com/prateekmehta59/Celebrity-Face-Recognition-Dataset)
* [Предобученная keras модель](https://drive.google.com/drive/folders/1pwQ3H4aJ8a6yyJHZkTwtjcL4wYWQb7bn)
* Для бота использовалась лишь  [часть](https://drive.google.com/open?id=1lpM_nzwkMJc7QrRig3VVh7_fNtTaTPwH) датасета CFRD (10 случайных фото для каждой звезды)
* [Эмбеддинги](https://yadi.sk/d/SDKBoWQJ9YRgGw) этих фото, переведенные в пространство [Annoy](https://github.com/spotify/annoy)

# Инструкция по установке:
* Скачать весь репозиторий
* Получить токен в сообществе ВК и добавить его в файл get_token.py
* Скачать [файл](https://yadi.sk/d/SDKBoWQJ9YRgGw)
* Заменить в папке data/ файл stars_embeddings.ann на скачанный файл (имя оставить stars_embeddings.ann)
* Выйти из папки LikeCelebrity/ и запустить команду: docker build -t vkbot:v1 LikeCelebrity/
* vkbot:v1 - имя образа:версия (можно указать произвольные)
* Запустить приложение командой docker run vkbot:v1
