#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
from script_create import ImageTable, Session
import sqlite3
import pickle
import cv2
import json


def inserter(file_dir, n):
    list_fold = os.listdir(file_dir)
    list_fold.sort()
    k_proc = 0
    for name_of_star in list_fold:
        print('load %d/%d' % (k_proc, len(list_fold)))
        fold_name = '%s/%s' % (file_dir, name_of_star)
        i = 0
        with open("file.txt", "r") as file:
            data = json.load(file)
        for name in data[name_of_star]:
            path_to_img = '%s/%s' % (fold_name, name)
            try:
                pil_im = cv2.imread(path_to_img)
            except:
                print('error')
            key = k_proc * 10 + i
            blob = pickle.dumps(pil_im, -1)
            session = Session()
            cel = ImageTable(key=key,
                             name=name_of_star,
                             image=sqlite3.Binary(blob))
            session.add(cel)
            session.commit()
            session.close()
            i += 1
        k_proc += 1

if __name__ == "__main__":
    inserter("Celebrities", 10)
