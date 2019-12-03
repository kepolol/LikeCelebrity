#!/bin/bash


rm data/stars_embeddings.ann
rm data/database.db
python vkbot/create_db.py
python vkbot/vk_bot.py
