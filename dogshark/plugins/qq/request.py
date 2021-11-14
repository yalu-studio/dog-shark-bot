from nonebot import on_request
from nonebot.adapters.cqhttp import Bot, GroupRequestEvent
from nonebot.adapters.cqhttp.event import FriendRequestEvent

request = on_request()

@request.handle()
async def _(bot: Bot, event:GroupRequestEvent):
    agreed = event.sub_type == "invite" \
             and event.get_user_id() in bot.config.superusers
    await bot.set_group_add_request(flag=event.flag,
                                        sub_type=event.sub_type,
                                        approve=agreed,
                                        reason='汪')

@request.handle()
async def _(bot: Bot, event:FriendRequestEvent):
    agreed = event.get_user_id() in bot.config.superusers
    await bot.set_friend_add_request(flag=event.flag,
                                     approve=agreed)