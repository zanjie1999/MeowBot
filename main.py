# -*- coding:utf-8 -*-

# Sparkle Meow Bot 喵~
# v1.0

from aiocqhttp import CQHttp
from quart import request,jsonify

from mod.repeater import repeater


# config
myId = 625797728

bot = CQHttp(enable_http_post=False)
app = bot.server_app

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

@bot.on_message()
async def handle_msg(context):
    await repeater(bot, context)
    # print(context)
    # await bot.send(context, '你好呀，下面一条是你刚刚发的：')
    # return {'reply': context['message']}

bot.run(host='0.0.0.0', port=5757)
