import vk_functionality as vk_func
from commands import cmds as cmd_lst
from define import CMDS_PATH
import os
from importlib import import_module

def get_answer(user_id, token, body):
    msg = """Не понял, что ты имел в виду. &#128576;
        Посмотри справку, отправив мне "?", и попробуй еще раз! &#128119;"""

    bodies = body.split()
    if len(bodies) != 0:
        for cmd in cmd_lst:
            if bodies[0].lower() in cmd.keys:
                msg = cmd.process(user_id, token, *bodies[1:])
    return msg

def load_cmds():
    print(os.getcwd())
    files = sorted(os.listdir(CMDS_PATH))
    modules = filter(lambda x: x.endswith(".py"), files)
    for module in modules:
        import_module("cmds." + module[:-3])
    pass

def answer(data, token):
   load_cmds()

   user_id = data["user_id"]
   msg = get_answer(user_id, token, data["body"])
   vk_func.send_msg(user_id, token, msg)
   pass