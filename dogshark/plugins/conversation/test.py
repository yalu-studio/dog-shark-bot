from nonebot import on_message, on_command
from nonebot.permission import SUPERUSER
from nonebot.rule import regex, to_me
from nonebot.adapters.cqhttp.event import MessageEvent
from nonebot.adapters import Bot

test = on_message(to_me() & regex(r'^测试测试$'))

@test.handle()
async def test_reply(bot: Bot, event: MessageEvent):
    await bot.send(event, '啊————')