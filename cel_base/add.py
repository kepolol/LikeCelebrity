#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
from .script_create import ImageTable, Session
import json


def inserter():
    k_proc = 0
    with open("../data/file.txt", "r") as file:
        data = json.load(file)
    for name_of_star in data:
        print('load %d/%d' % (k_proc, len(data)))
        i = 0
        for _ in data[name_of_star]:
            key = k_proc * 10 + i
            session = Session()
            cel = ImageTable(key=key,
                             name=name_of_star)
            session.add(cel)
            session.commit()
            session.close()
            i += 1
        k_proc += 1


if __name__ == "__main__":
    inserter()
