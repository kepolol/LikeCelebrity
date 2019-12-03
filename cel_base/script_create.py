#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, Binary, String
from sqlalchemy.ext.declarative import declarative_base



Base = declarative_base()


class ImageTable(Base):
    __tablename__ = "Images"
    
    id_ = Column(Integer, primary_key=True)
    key = Column(Integer)
    name = Column(String)


engine = create_engine('sqlite:///../data/celebrities.db')
Session = sessionmaker(bind=engine)
Base.metadata.create_all(bind=engine)
