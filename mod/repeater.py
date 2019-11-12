# coding=utf-8

# Sparkle Meow Bot
# repeater 复读机模块
# v2.0

import random

from config import repeater_hotWord as hotWord, repeater_naturalWord as naturalWord, repeater_probability as probability


async def repeater(context):
    if context:
        if context['message_type'] == 'private':
            # 私聊 无脑复读
            if await randomFlag():
                print('私聊复读', context['sender']['nickname'], context['message'])
                return {'reply': context['message'], 'at_sender': False}
        elif context['message_type'] == 'group':
            # 群聊 匹配规则复读
            if await listFlag(context) and await randomFlag():
                print(
                    '群聊复读', context['group_id'], context['sender']['nickname'], context['message'])
                return {'reply': context['message'], 'at_sender': False}


async def listFlag(context):
    id = 0
    if context['message_type'] == 'private':
        id = context['user_id']
    elif context['message_type'] == 'group':
        id = context['group_id']
    else:
        return False

    flag = False
    # 匹配规则
    msg = context['message'].lower()
    if msg in hotWord:
        flag = True
    else:
        for w in naturalWord:
            if w in msg:
                flag = True
                break
    return flag


async def randomFlag(flag=True):
    if probability == 1:
        return flag
    if flag:
        return random.random() < probability
    return False
