from nonebot import on_regex, on_command
from nonebot.rule import to_me
from nonebot.adapters.cqhttp.event import MessageEvent, Message
from nonebot.adapters import Bot

NO_RESPONSE_IMG = '/assets/images/no-response.jpg'

test = on_regex(r'^测试测试$', rule=to_me(), block=True)
@test.handle()
async def _(bot: Bot, event: MessageEvent):
    await test.finish('啊————')

response = on_command('', rule=to_me(), priority=999)
@response.handle()
async def _(bot: Bot, event: MessageEvent):
    msg = Message(f'[CQ:image,file=file://{NO_RESPONSE_IMG}]')
    await response.finish(msg)