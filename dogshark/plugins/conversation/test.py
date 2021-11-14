from nonebot import on_command
from nonebot.rule import to_me
from nonebot.adapters.cqhttp.event import MessageEvent
from nonebot.adapters import Bot

test = on_command('测试测试', to_me())

@test.handle()
async def _(bot: Bot, event: MessageEvent):
    await test.finish('啊————')