#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from models import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import LogTable, Feedback


eng = create_engine('sqlite:///database.db')
Ses = sessionmaker(bind=eng)


def init_db():
    Base.metadata.create_all(bind=eng)
    defualt_value = 0
    ses = Ses()
    fb = Feedback(positive=defualt_value,
                  negative=defualt_value)
    ses.add(fb)
    ses.commit()
    ses.close()

def add_log(request_date, user_id, msg, resp, dur_time):
    ses = Ses()
    log = LogTable(request_date=request_date,
                   user_id=user_id,
                   message_info=msg,
                   response=resp,
                   duration=dur_time)
    ses.add(log)
    ses.commit()
    ses.close()
    
if __name__ == "__main__":
    init_db()