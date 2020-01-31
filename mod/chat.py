# coding=utf-8

# Sparkle Meow Bot
# chat 聊天模块(自动回复)
# v3.0

import jieba
import random
import time

from config import chat_rule as rule, botName, chat_sleepTime as sleepTime, lastMsg

# 让名字绝对不会被分出来
jieba.suggest_freq(botName, True)

# 加载用户分词词典 可以把输入法的热词转了放进去
jieba.load_userdict("dict.txt")


async def chat(context, id):
    send = await findRule(context, id)
    if send:
        print('聊天', context['sender']['nickname'],
              context['message'], '\n回复', send)
        return {'reply': send, 'at_sender': False}


# 寻找规则
async def findRule(context, id):
    msg = context['message'].strip()
    if msg:
        cut = jieba.lcut(msg)
        if cut:
            # debug
            # print(' '.join(cut))
            for i in rule:
                for key in i[0]:
                    if type(key) == str:
                        # 单词素
                        if key in cut:
                            return await chooseMsg(context, id, key, i[1])
                    else:
                        # 多词素
                        flag = True
                        for k in key:
                            if k not in cut:
                                flag = False
                                break
                        if flag:
                            return await chooseMsg(context, id, key, i[1])


# 抽取消息
async def chooseMsg(context, id, key, msgs):
    global lastMsg
    if context and key and msgs:
        if id in lastMsg and 'chat' in lastMsg[id] and lastMsg[id]['chat']:
            # 发送过消息
            if lastMsg[id]['chat'][0] == key and time.time() < lastMsg[id]['chat'][1]:
                return True
        else:
            if id not in lastMsg:
                lastMsg[id] = {}
            lastMsg[id]['chat'] = [key, time.time() + sleepTime]
        # 随机返回回复
        if len(msgs) == 1:
            return msgs[0]
        else:
            return random.choice(msgs)
