#-*- coding: utf-8 -*-

__author__ = '打补丁的狮子'

import time, uuid

from orm import Model, StringField, BooleanField, FloatField, TextField

def next_id():
    return "%015d%s000" % (int(time.time() * 1000), uuid.uuid4().hex)

class User(Model):
    __table__='users'

    id = StringField(primary_key=True, default=next_id(), ddl='VARCHAR(50)')
    email = StringField(ddl='VARCHAR(50)')
    passwd = StringField(ddl='VARCHAR(50)')
    admin = BooleanField()
    name = StringField(ddl='VARCHAR(50)')
    image = StringField(ddl='VARCHAR(500)')
    create_at = FloatField(default=time.time)