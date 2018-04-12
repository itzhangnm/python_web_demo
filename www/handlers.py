#!/usr/bin/python3
# -*- coding: utf-8 -*-

# 2018/4/11 17:29
__Author__ = 'zb'

from coreweb import get, post
from models import User, Comment, Blog, next_id

@get('/')
async def index(request):
    users = await User.findAll()
    return {
        '__template__':'test.html',
        'users':users
    }