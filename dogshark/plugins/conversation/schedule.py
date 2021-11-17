from nonebot import on_regex
from nonebot.rule import to_me
from nonebot.adapters.cqhttp.event import MessageEvent
from nonebot.adapters import Bot

# TODO: Implement database
schedule_stream = None

get_current_stream = on_regex(r'^#查询.*直播计划$', rule=to_me())

@get_current_stream.handle()
async def _(bot: Bot, event: MessageEvent):
    # TODO: Check message source.
    # Only response to certain group and SUPERUSERS
    # Database lookup: GroupID -> streamer -> Schedule

    msg = '摸了'
    if schedule_stream:
        msg = schedule_stream
    await get_current_stream.finish(msg)

# TODO: Implement schedule setting