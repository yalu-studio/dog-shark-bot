from nonebot import on_notice
from nonebot.adapters.cqhttp import Bot, Message, GroupIncreaseNoticeEvent

notice = on_notice()

@notice.handle()
async def _(bot: Bot, event: GroupIncreaseNoticeEvent):
    _at = f"[CQ:at,qq={event.get_user_id()}]"
    msg = Message(_at + '欢迎!\n＼＼\٩(๑`^´๑)۶//／／')
    await notice.finish(message=msg)