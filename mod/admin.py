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


# 我发消息  方便就写在一起了
async def admin2at(bot, context):
    global at
    if context['message'] and '@' == context['message'][0] and '\r' in context['message']:
        if 'g' == context['message'][1]:
            # 发群消息(指定群号)  @g群号\r\n消息内容
            msg = context['message'][2:].split('\r', 1)
            await bot.send_group_msg(group_id=msg[0], message=msg[1], auto_escape=False)
            return {'reply': '群消息已发送 @g' + msg[0], 'at_sender': False}
        elif 'q' == context['message'][1]:
            # 发私聊(指定qq号)  @qQQ号\r\n消息内容
            msg = context['message'][2:].split('\r', 1)
            await bot.send_private_msg(user_id=msg[0], message=msg[1], auto_escape=False)
            return {'reply': '私聊已发送 @q' + msg[0], 'at_sender': False}
        else:
            # 回复at  @xxx\r\n消息内容
            msg = context['message'][1:].split('\r', 1)
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
        tip = '@g{} 群中被@{}\n{}({}):\n{}'.format(
            context['group_id'], tip, context['sender']['nickname'], context['user_id'], context['message'])
        print(tip)
        await bot.send_private_msg(user_id=myId, message=tip, auto_escape=False)
        # 返回一个没有意义的东西避免继续执行其他模块
        return True
