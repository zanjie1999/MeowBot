# coding=utf-8

# Sparkle Meow Bot
# chat 聊天模块(自动回复)
# v2.0

import jieba

from config import chat_rule as rule

async def chat(context):
    return False