#!/usr/bin/python3
# -*- coding: utf-8 -*-

# 2018/4/11 9:37
__Author__ = 'zb'

import orm
from models import User,Blog,Comment
import asyncio

async def test(loop):
    await orm.create_pool(loop=loop,user='root',password='zhangbo123',db='awesome')
    u = User(name='Test',email='itzhangnima@163.com',password='123456',image='about:blank')
    await u.save()
    await orm.close_pool()


# 获取EventLoop:
loop = asyncio.get_event_loop()

#把协程丢到EventLoop中执行
loop.run_until_complete(test(loop))

#关闭EventLoop
loop.close()
