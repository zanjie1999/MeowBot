# -*- coding:utf-8 -*-

# Sparkle Meow Bot
# repeater 复读机模块
# v2.0

import random

# 号码白名单
whiteList = []

#号码黑名单
blackList = []

# 直接匹配
hotWord = [' ', '我', '我们', '你', '你们', '草', '艹', 'cao', '晚安', '安安', '安', '还行', '没毛病', '?', '？', '我好难啊',
           '[cq:face,id=176]',  # 小纠结
           '[cq:face,id=178]',  # 滑稽
           '[cq:face,id=179]',  # 狗头
           '[cq:face,id=169][cq:face,id=178]',  # 枪指滑稽
           '[cq:face,id=178][cq:face,id=67]',   # 滑稽心碎
           '[cq:face,id=178][cq:face,id=146]',  # 滑稽生气
           '😂', '😳'
           ]

# 模糊匹配
naturalWord = ['我渴望', '吾乃', '之王者', '辣鸡', '没想到你是这样的']

# 复读几率 0-1
probability = 0.5

async def repeater(bot, context):
    if context:
        if context['message_type'] == 'private':
            # 私聊 无脑复读
            if await randomFlag():
                await bot.send(context, context['message'])
                print('私聊复读', context['sender']['nickname'], context['message'])
        elif context['message_type'] == 'group':
            # 群聊 匹配规则复读
            if await listFlag(context) and await randomFlag():
                await bot.send(context, context['message'])
                print('群聊复读', context['group_id'], context['sender']['nickname'], context['message'])


async def listFlag(context):
    id = 0
    if context['message_type'] == 'private':
        id = context['user_id']
    elif context['message_type'] == 'group':
        id = context['group_id']
    else:
        return False

    flag = False
    # 黑白名单
    if (not blackList or id not in blackList) and (not whiteList or id in whipyteList):
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
