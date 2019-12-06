# coding=utf-8

# Sparkle Meow Bot 喵~
# 骂人的模块
# v1.0

import random
import asyncio

msgs = [ '你是大变态', '滚', '大坏蛋', '大坏蛋大坏蛋']

fucku = [1208467214]

async def fuck(context):
    if context['sender']['user_id'] in fucku :
        await asyncio.sleep(random.random() * 3)
        return {'reply': random.choice(msgs), 'at_sender': False}


