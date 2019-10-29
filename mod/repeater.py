# -*- coding:utf-8 -*-

# Sparkle Meow Bot
# repeater 复读机模块
# v1.0


whiteList = []
blackList = []
hotWord = [' ', '我', '你', '草', '艹', 'cao', '晚安', '安安', '还行',
           '[cq:face,id=176]',  # 小纠结
           '[cq:face,id=178]',  # 滑稽
           '[cq:face,id=179]'   # 狗头
           ]
naturalWord = ['我渴望', '吾乃', '之王者', '辣鸡', '没想到你是这样的']


async def repeater(bot, context):
    if context:
        if context['message_type'] == 'private':
            # 私聊
            await bot.send(context, context['message'])
            print('私聊复读', context['sender']['nickname'], context['message'])
        elif context['message_type'] == 'group':
            # 群聊
            # 黑白名单
            if (not blackList or context['group_id'] not in blackList) and (not whiteList or context['group_id'] in whiteList):
                flag = False
                msg = context['message'].lower()
                if msg in hotWord:
                    flag = True
                else:
                    for w in naturalWord:
                        if w in msg:
                            flag = True
                            break

                if flag:
                    await bot.send(context, context['message'])
                    print(
                        '群聊复读', context['group_id'], context['sender']['nickname'], context['message'])
