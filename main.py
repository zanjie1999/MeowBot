# coding=utf-8

# Sparkle Meow Bot 喵~
# v1.0

from aiocqhttp import CQHttp
from quart import request, jsonify
import random
import asyncio

from config import myId, whiteList, blackList, lastMsg

from mod.repeater import repeater
from mod.handleAdd import handleAdd
from mod.chat import chat
from mod.admin import admin
from mod.fuck import fuck

bot = CQHttp(enable_http_post=False)
app = bot.server_app

# 黑白名单
async def blackWhiteListFlag(context):
    id = 0
    if context['message_type'] == 'private':
        id = context['user_id']
    elif context['message_type'] == 'group':
        id = context['group_id']
    else:
        print('未知类型:', context)
        return False
    return (not blackList or id not in blackList) and (not whiteList or id in whiteList)


# 给我自己发送物联网设备的消息
@app.route('/push', methods=['GET', 'POST'])
async def msg():
    # 为什么这里不能直接  await request.form['msg']
    form = await request.form
    # object str can't be used in 'await' 不写异步 await request.args.get() 为何依然可用
    msg = form['msg'] if request.method == 'POST' else request.args.get('msg')
    if msg:
        ret = await bot.send_private_msg(user_id=myId, message=msg)
        print('Send me msg: ', msg)
        ret.update({'success': True})
        return jsonify(ret)
    else:
        return jsonify({'success': False})


# 收到消息
@bot.on_message()
async def handle_msg(context):
    global lastMsg
    if context:
        # id经常用到就写到外面吧
        id = context['group_id'] if context['message_type'] == 'group' else context['user_id'] if context['message_type'] == 'private' else None
        if id:
            # 骂人 管理 模块高优先级
            # msg = await fuck(context) or await admin(bot, context)
            msg = await admin(bot, context)
            if not msg:
                # 黑白名单
                if await blackWhiteListFlag(context):
                    msg = await chat(context, id) or await repeater(context, id)
                    if msg:
                        # 为了不被识破 随机延时
                        await asyncio.sleep(random.random() * 10 + 1)

            # 最后保存
            await _recordLastMsg(context, id)
            return msg


# 收到加群加好友申请
@bot.on_request()
async def handle_group(context):
    return await handleAdd(bot, context)


# 记录最后的消息
async def _recordLastMsg(context, id):
    global lastMsg
    if id in lastMsg and lastMsg[id]['my']:
        if context['user_id'] == myId:
            lastMsg[id]['my'][1] = lastMsg[id]['my'][0]
            lastMsg[id]['my'][0] = context['message']
        else:
            lastMsg[id]['other'][1] = lastMsg[id]['other'][0]
            lastMsg[id]['other'][0] = context['message']
    else:
        # 初次记录 如果没有这个key需要先给他赋值一下 否则Key Error
        if id not in lastMsg:
            lastMsg[id] = {}
        if context['user_id'] == myId:
            lastMsg[id]['my'] = [context['message'], None]
            lastMsg[id]['other'] = [None, None]
        else:
            lastMsg[id]['other'] = [context['message'], None]
            lastMsg[id]['my'] = [None, None]
    # debug
    print(lastMsg)


bot.run(host='0.0.0.0', port=5757)
