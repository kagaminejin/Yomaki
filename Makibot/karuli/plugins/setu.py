from nonebot import on_command, on_startswith
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event
from nonebot.adapters.cqhttp.message import Message

import urllib3
import json
import requests

today = on_command("setu", aliases={'涩图', }, priority=5)

@today.handle()
async def handle_first_receive(bot: Bot, event: Event, state: T_State):
  args = str(event.get_message()).strip()
  try:
    url = 'https://api.lolicon.app/setu/v2'
    params = {
     "tag": [
     ["幼女", "萝莉","少女"],
     ["白丝", "黑丝"],
     ]
     }
    check_data = requests.request("post", url, params=params)
    check_data = check_data.json()
    data_json = json.dumps(check_data, ensure_ascii=False)
    data = json.loads(data_json)
    path = '.\\test.txt'
# 打开文件
    f = open(path, "w+")
    f.write(str(data))
    f.close()
    img_url = data['data'][0]['urls']["original"]
    cq = "[CQ:image,file=" + img_url + ",id=40000]"
    await today.send(Message(cq))
  except :
    await today.send("获取失败:\n服务器错误")