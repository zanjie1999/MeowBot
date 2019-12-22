# coding=utf-8

# Sparkle Meow Bot
# repeater 复读机模块
# v2.0

import random

from config import myId, repeater_hotWord as hotWord, repeater_naturalWord as naturalWord, repeater_probability as probability, lastMsg

async def repeater(context, id):
    global lastMsg
    if context:
        if context['message_type'] == 'private':
            # 私聊 无脑复读
            if await randomFlag():
                print('私聊复读', context['sender']['nickname'], context['message'])
                return {'reply': context['message'], 'at_sender': False}
        elif context['message_type'] == 'group':
            # 群聊
            if context['user_id'] == myId and id in lastMsg and lastMsg[id]['my']:
                # 我说的而且我在复读
                if context['message'] == lastMsg[id]['my'][0] == lastMsg[id]['my'][1] or context['message'] == lastMsg[id]['my'][0] == lastMsg[id]['other'][0] or context['message'] == lastMsg[id]['other'][0] == lastMsg[id]['other'][1]:
                    print('学我复读', context['message'])
                    return {'reply': context['message'], 'at_sender': False}
            
            # 匹配规则复读
            if await listFlag(context) and await randomFlag():
                print('群聊复读', context['group_id'], context['sender']['nickname'], context['message'])
                return {'reply': context['message'], 'at_sender': False}


async def listFlag(context):
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
