#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from models import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import LogTable, Feedback


engine = create_engine('sqlite:///data/database.db')
Session = sessionmaker(bind=engine)


def init_db():
    Base.metadata.create_all(bind=engine)
    defualt_value = 0
    session = Session()
    fb = Feedback(positive=defualt_value,
                  negative=defualt_value)
    session.add(fb)
    session.commit()
    session.close()


def add_log(request_date, user_id, msg, resp, dur_time):
    session = Session()
    log = LogTable(request_date=request_date,
                   user_id=user_id,
                   message_info=msg,
                   response=resp,
                   duration=dur_time)
    session.add(log)
    session.commit()
    session.close()


if __name__ == "__main__":
    init_db()
