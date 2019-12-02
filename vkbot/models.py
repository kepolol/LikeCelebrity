#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class LogTable(Base):
    __tablename__ = "logs"
    
    id_ = Column(Integer, primary_key=True)
    request_date = Column(String)
    user_id = Column(Integer)
    message_info = Column(String)
    response = Column(String)
    duration = Column(Float)


class Feedback(Base):
    __tablename__ = "feedback"

    id_ = Column(Integer, primary_key=True)
    positive = Column(Integer)
    negative = Column(Integer)
