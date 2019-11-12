# coding=utf-8

# Sparkle Meow Bot
# chat 聊天模块(自动回复)
# v2.0

import jieba
import random

from config import chat_rule as rule,botName

# 让名字绝对不会被分出来
jieba.suggest_freq(botName, True)

async def chat(context):
    send = await findRule(context['message'])
    if send:
        print('聊天', context['sender']['nickname'], context['message'], '\n回复', send)
        return {'reply': send, 'at_sender': False}


# 寻找规则
async def findRule(msg):
    msg = msg.strip()
    if msg:
        cut = jieba.lcut(msg)
        if cut:
            print(' '.join(cut))
            for i in rule:
                for key in i[0]:
                    if type(key) == str:
                        # 单词素
                        if key in cut:
                            return await chooseMsg(i[1])
                    else:
                        # 多词素
                        flag = True
                        for k in key:
                            if k not in cut:
                                flag = False
                                break
                        if flag:
                            return await chooseMsg(i[1])


# 抽取消息
async def chooseMsg(msgs):
    if msgs:
        if len(msgs) == 1:
            return msgs[0]
        else:
            return random.choice(msgs)
