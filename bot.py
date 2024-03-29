
import os
try:
    import nonebot2
except ImportError:
    cmd1 = 'pip install nonebot2'
    os.system(cmd1)
try:
    from nonebot.adapters.cqhttp import Bot as CQHTTPBot
except ImportError:
    cmd2 = 'pip install nonebot-adapter-cqhttp'
    os.system(cmd2)

import nonebot
from nonebot.adapters.cqhttp import Bot as CQHTTPBot

nonebot.init()
driver = nonebot.get_driver()
driver.register_adapter("cqhttp", CQHTTPBot)
nonebot.load_builtin_plugins()
nonebot.load_plugins("karuli/plugins")

app = nonebot.get_asgi()

if __name__ == "__main__":
    nonebot.run()

input("please input any key to exit!")
