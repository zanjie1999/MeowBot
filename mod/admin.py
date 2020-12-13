# coding=utf-8

# Sparkle Meow Bot
# admin 管理模块
# v1.0

from config import myId, send_next_msg_to_group_plus_time
import time

# 被at的数据
at = {}

# 下一条消息发到指定群
send_next_msg_to_group = {
    'flag': False,
    'time': 0,
    'id': 0,
    'type': ''
}


async def admin(bot, context):
    if context:
        if context['message_type'] == 'private':
            # 私聊
            if context['user_id'] == myId:
                return await admin2at(bot, context)
        elif context['message_type'] == 'group':
            # 群聊
            return await at2admin(bot, context)


# 按\r或\n分割
async def splitrn(msg):
    out = msg.split('\r\n', 1)
    if len(out) == 1:
        out = msg.split('\r', 1)
    if len(out) == 1:
        out = msg.split('\n', 1)
    return out


async def adminSend(bot, sendType, sendId, message):
    # 内含消息内容
    if 'g' == sendType:
        # 发群消息(指定群号)  @g群号\r\n消息内容
        await bot.send_group_msg(group_id=sendId, message=message, auto_escape=False)
        return {'reply': '群消息已发送\n@g' + sendId, 'at_sender': False}
    elif 'q' == sendType:
        # 发私聊(指定qq号)  @qQQ号\r\n消息内容
        await bot.send_private_msg(user_id=sendId, message=message, auto_escape=False)
        return {'reply': '私聊已发送\n@q' + sendId, 'at_sender': False}
    else:
        # 回复at  @xxx\r\n消息内容
        if sendId in at:
            await bot.send(at[sendId], message, at_sender=True, auto_escape=False)
            # 回复完就删掉啦
            at.pop(sendId)
            return {'reply': '回复成功\n@' + sendId, 'at_sender': False}
        else:
            return {'reply': '找不到需要回复的\n@' + sendId, 'at_sender': False}


# 我发消息  方便就写在一起了
async def admin2at(bot, context):
    global at
    global send_next_msg_to_group
    if context['message'] and  '@' == context['message'][0]:
        if len(context['message']) < 2:
            if send_next_msg_to_group['flag']:
                send_next_msg_to_group['flag'] = False
                return {'reply': '发送消息操作已取消', 'at_sender': False}
        else:
            if  '\r' in context['message'] or '\n' in context['message']:
                # 内含消息内容 割出来发出去
                if 'g' == context['message'][1] or 'q' == context['message'][1]:
                    msg = await splitrn(context['message'][2:])
                    return await adminSend(bot, context['message'][1], msg[0], msg[1])
                else:
                    msg = await splitrn(context['message'][1:])
                    return await adminSend(bot, None, msg[0], msg[1])
            else:
                # 记录当前指定的发送消息对象 下一条是消息内容
                sendType = ''
                sendId = ''
                if 'g' == context['message'][1] or 'q' == context['message'][1]:
                    sendType = context['message'][1]
                    sendId = context['message'][2:]
                else:
                    sendId = context['message'][1:]
                send_next_msg_to_group = {
                    'flag': True,
                    'time': time.time() + send_next_msg_to_group_plus_time,
                    'id': sendId,
                    'type': sendType
                }
                return {'reply': str(send_next_msg_to_group_plus_time) + ' 秒内回复一条消息发送给\n@' + sendType + sendId + '\n回复@取消', 'at_sender': False}
    elif send_next_msg_to_group['flag']:
        # 收到了下一条消息 发出去
        if send_next_msg_to_group['time'] < time.time():
           send_next_msg_to_group['flag'] = False 
        else:
            send_next_msg_to_group['flag'] = False 
            return await adminSend(bot, send_next_msg_to_group['type'], send_next_msg_to_group['id'], context['message'])
            
            


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
        tip = '@g{}\n群中被@\n@{}\n{}({}):\n{}'.format(
            context['group_id'], tip, context['sender']['nickname'], context['user_id'], context['message'])
        print(tip)
        await bot.send_private_msg(user_id=myId, message=tip, auto_escape=False)
        # 返回一个没有意义的东西避免继续执行其他模块
        return True
