from nonebot import on_request
from nonebot.rule import Rule
from nonebot.typing import T_State
from nonebot.adapters.cqhttp import Bot, GroupRequestEvent
from nonebot.adapters.cqhttp.event import FriendRequestEvent

def friend_add():
    async def _friend_add(bot: Bot, event: FriendRequestEvent, state: T_State) -> bool:
        return event.request_type == 'friend'
    return Rule(_friend_add)

def group_invite():
    async def _group_invite(bot: Bot, event: GroupRequestEvent, state: T_State) -> bool:
        return event.request_type == 'group'
    return Rule(_group_invite)

group_invite = on_request(group_invite())
@group_invite.handle()
async def agree_group_invite(bot: Bot, event:GroupRequestEvent):
    agreed = event.sub_type == "invite" \
             and str(event.user_id) in bot.config.superusers
    await bot.set_group_add_request(flag=event.flag,
                                        sub_type=event.sub_type,
                                        approve=agreed,
                                        reason='汪')

friend_request = on_request(friend_add())
@friend_request.handle()
async def agree_friend_request(bot: Bot, event:FriendRequestEvent):
    agreed = str(event.user_id) in bot.config.superusers
    await bot.set_friend_add_request(flag=event.flag,
                                     approve=agreed)