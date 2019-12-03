#!/bin/bash


rm data/database.db
python vkbot/create_db.py
python vkbot/vk_bot.py
