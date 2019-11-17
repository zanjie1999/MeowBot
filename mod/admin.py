# coding=utf-8

# Sparkle Meow Bot
# admin 管理模块
# v1.0

from config import myId

# 被at的数据
at = {}


async def admin(bot, context):
    if context:
        if context['message_type'] == 'private':
            # 私聊
            if context['user_id'] == myId:
                return await admin2at(bot, context)
        elif context['message_type'] == 'group':
            # 群聊
            return await at2admin(bot, context)


# 我回复at  @xxx\r\n消息内容
async def admin2at(bot, context):
    global at
    if '@' == context['message'][0] and '\r\n' in context['message']:
        msg = context['message'][1:].split('\r\n', 1)
        if msg[0] in at:
            await bot.send(at[msg[0]], msg[1], at_sender=True, auto_escape=False)
            # 回复完就删掉啦
            at.pop(msg[0])
            return {'reply': '回复成功 @' + msg[0], 'at_sender': False}
        else:
            return {'reply': '找不到需要回复的 @' + msg[0], 'at_sender': False}


# 被at提醒我
async def at2admin(bot, context):
    global at
    if '[CQ:at,qq=' + str(context['self_id']) + ']' in context['message']:
        tip = ''
        msgId = str(context['message_id'])
        if msgId in at:
            tip = str(context['font'])
        else:
            tip = msgId
        # 放进去
        at[tip] = context
        # 提醒我
        tip = '在群 {} 被 @{}\n{}({}):\n{}'.format(
            context['group_id'], tip, context['sender']['nickname'], context['user_id'], context['message'])
        print(tip)
        await bot.send_private_msg(user_id=myId, message=tip, auto_escape=False)
        # 返回一个没有意义的东西避免继续执行其他模块
        return True
