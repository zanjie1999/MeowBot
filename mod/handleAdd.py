# coding=utf-8

# Sparkle Meow Bot
# handleAdd 加群加好友申请处理模块
# v2.0

from config import myId, handleAdd_rule as rule


async def handleAdd(bot, context):
    if context['request_type'] == 'group':
        if context['group_id'] in rule.keys():
            comment = context['comment'].lower()
            for i in rule.get(context['group_id']):
                if i in comment:
                    # 同意申请
                    print('同意了申请', context['user_id'], '加入', context['group_id'])
                    return {'approve': True}
    elif context['request_type'] == 'friend':
        # 通知小主人处理
        await bot.send_private_msg(user_id=myId, message='收到来自 {} 的好友请求:\n{}'.format(context['user_id'], context['comment']))
