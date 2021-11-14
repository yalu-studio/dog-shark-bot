from nonebot import on_notice
from nonebot.adapters.cqhttp import Bot, Message, GroupIncreaseNoticeEvent

WELCOME_MEME = 'file:///images/welcome.jpg'

notice = on_notice()

@notice.handle()
async def _(bot: Bot, event: GroupIncreaseNoticeEvent):
    _at = f"[CQ:at,qq={event.get_user_id()}]"
    _meme = f"[CQ:image,file={WELCOME_MEME}]"
    msg = Message(_at + '欢迎!\n＼＼\٩(๑`^´๑)۶//／／' + _meme)
    await notice.finish(message=msg)