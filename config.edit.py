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


# 复读机 直接匹配
chat_rule = (
    (['智乃'], [' ', '噫', '咦', '好像有人提到我', '(阿嚏)']),
    ([['是', '机器人']], [' ', '噫', '咦', '嗯?', '嘛~', '还行', '?', '？', '.', '...', '。', '。。。']),
    (['vpn', ['免费', '代理'], '翻墙', ['开', '代理']], ['(前排提示: 敏感词请自觉撤回)']),
    (['早上好', '早安', ['早', '呀']], ['早', '早呀', '早上好', '(我通宵了)']),
    (['晚安', ['睡觉', '了']], ['祝好梦~', '晚安', '我帮你关灯 XD']),
    ([['我', '渴望']], ['你渴望', '嗯?']),
    ([['嗨', '最晚'], ['守夜', '冠军'], ['打算', '通宵']], ['早点睡!', '快睡觉吧~', '说好的睡觉呢?']),
    (['🐂🍺', '大佬', '大神', 'dalao', '666', '厉害'], ['🐂🍺', '太强了', '好厉害呀', '好棒', '群除我佬', '大神', '大佬']),
    (['魔鬼', '恶魔'], ['😈', '可怕', '魔鬼', '恶魔', 'emmmm……']),
    (['我太难', '我好难'], ['你太难了', '你好难啊', '太难了', '好难呀']),
    (['好酸', '真香', '🍋'], ['真香', '真香警告', '真香定律', '🍋', '我好酸', '太香了'])
)

# 复读机 直接匹配
repeater_hotWord = (
    ' ', '我', '我们', '你', '你们', '草', '艹', 'cao', '晚上好', '安安', '安', '早', '早安', '早上好', '还行', '没毛病', '?', '？', '我好难啊', '我裂开了', '不知道', '.', '...', '。', '。。。',
    '[cq:face,id=176]',  # 小纠结
    '[cq:face,id=178]',  # 滑稽
    '[cq:face,id=179]',  # 狗头
    '[cq:face,id=169][cq:face,id=178]',  # 枪指滑稽
    '[cq:face,id=178][cq:face,id=67]',   # 滑稽心碎
    '[cq:face,id=178][cq:face,id=146]',  # 滑稽生气
    '😂', '😳'
)

# 复读机 模糊匹配
repeater_naturalWord = ('吾乃', '辣鸡', '没想到你是这样的')

# 复读机 复读几率 0-1
repeater_probability = 0.3
