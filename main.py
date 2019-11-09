# coding=utf-8

# Sparkle Meow Bot 喵~
# v1.0

from aiocqhttp import CQHttp
from quart import request, jsonify

from config import myId, whiteList, blackList

from mod.repeater import repeater
from mod.handleAdd import handleAdd

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
@app.route('/msg')
async def msg():
    msg = request.args.get("msg")
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
    # 黑白名单
    if blackWhiteListFlag(context):
        return await repeater(bot, context)


# 收到加群加好友申请
@bot.on_request()
async def handle_group(context):
    await handleAdd(bot, context)

bot.run(host='0.0.0.0', port=5757)
