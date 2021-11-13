import nonebot
from nonebot.adapters.cqhttp import Bot

nonebot.init()
nonebot.get_driver().register_adapter("cqhttp", Bot)

nonebot.load_builtin_plugins()
nonebot.load_plugins('plugins')

nonebot.run()