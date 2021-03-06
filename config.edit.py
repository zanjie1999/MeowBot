# coding=utf-8

# Sparkle Meow Bot
# 配置文件

# 我的QQ
myId = 13245678

# 人工智能的名字
botName = '智乃'

# 号码白名单
whiteList = ()

# 号码黑名单
blackList = ()


# 审核规则 号码. 包含的内容(任意一个)
handleAdd_rule = {
    13245678: ('包含', '任意内容')
}


# 聊天回复规则
# (['key',['key1','key2']], ['value'])
# (['key'], ['in time'], (0, 23), ['not in time'])
chat_rule = (
    (['智乃'], [None, ' ', '噫', '咦', '噗', '好像有人提到我', '(阿嚏)', '真有邪的']),
    (['机器人'], [None, ' ', '噫', '咦', '噗', '嗯?', '嘛~', '还行', '?', '？', '.', '...', '。', '。。。']),
    ([['翻墙', 'vpn'], 'ss', 'ssr', 'ssrr', ['免费', '代理'], '翻墙', 'fq', ['开', '代理']], ['(前排提示: 敏感词请自觉撤回)']),
    (['早上好', '早安', '早呀', '早啊'], ['早', '早呀', '早上好', '(我通宵了)'], (5, 14), ['你在想🍑', '现在不早了', '现在已经很晚了', '好晚...']),
    (['晚安', ['睡觉', '了']], ['安', '晚安', '祝...算了'], (21, 6), ['你在想🍑', '现在不是睡觉的时候', '别睡了快来玩啊', '睡什么睡', '你已经是一个成熟的吸血鬼了，应该...', '你是吸血鬼吗']),
    ([['我', '渴望']], ['你渴望', '嗯?']),
    ([['嗨', '最晚'], ['守夜', '冠军'], ['打算', '通宵']], ['早点睡!', '快睡觉吧~', '说好的睡觉呢?']),
    (['🐂🍺', '牛逼', ['是', '大佬'], ['是', '大神'], ['是', 'dalao'], '666', ['好', '厉害']], ['🐂🍺', '牛逼', '太强了', '好厉害呀']),
    (['魔鬼', '恶魔'], ['😈', '可怕', '魔鬼', '恶魔', 'emmmm……']),
    (['我太难了', '我好难'], ['你太难了', '你好难啊', '太难了', '真有邪的']),
    (['好酸', '真香', '🍋'], ['真香', '真香警告', '🍋', '我好酸', '太香了'])
)

# 同样的内容回复时间间隔 秒
chat_sleepTime = 600


# 复读机 直接匹配
repeater_hotWord = (
    ' ', '我', '我们', '你', '你们', '草', '艹', 'cao', '晚上好', '安安', '安', '早', '早安', '早上好', '还行', '没毛病', '?', '？', '我好难啊', '我裂开了', '不知道', '看我的', '.', '...', '。', '。。。',
    '[cq:face,id=176]',  # 小纠结
    '[cq:face,id=178]',  # 滑稽
    '[cq:face,id=179]',  # 狗头
    '[cq:face,id=169][cq:face,id=178]',  # 枪指滑稽
    '[cq:face,id=178][cq:face,id=67]',   # 滑稽心碎
    '[cq:face,id=178][cq:face,id=146]',  # 滑稽生气
    '[ CQ : face , id = 182 ]',  # 笑哭
    '😂', '😳'
)

# 复读机 模糊匹配
repeater_naturalWord = ('吾乃', '辣鸡', '没想到你是这样的')

# 复读机 复读几率 0-1
repeater_probability = 0.3

# 下一条消息发到指定群功能超时时间 
send_next_msg_to_group_plus_time = 30


# 全局变量
# 记录最后的消息内容  {id:{'my':[], 'other':[], 'chat':[]}}
lastMsg = {}
