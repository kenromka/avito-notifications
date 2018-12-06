import commands
import define
import searchers
from random import randint
from apscheduler.schedulers.background import BackgroundScheduler

def start(user_id, token, *args):
    define.scheduler[str(user_id)] = BackgroundScheduler()
    session = searchers.init_session(searchers.TLSAdapter())
    
    link = None
    for s in args:
        if str(s).find("avito.ru") != -1:
            link = str(s)
            break

    if link == None:
        return "Ты что-то ввел неправильно :с \n Попробуй еще раз или напиши 'помощь'"

    define.scheduler[str(user_id)].add_job(
        lambda: searchers.continious_search(session, args[0], user_id, token, define.proxies), 
        "interval",
        seconds=randint(
            int(define.update_time.get(str(user_id), 3)*6*9),
            int(define.update_time.get(str(user_id), 3)*11*6)
            )
    )
    define.scheduler[str(user_id)].start()
    return "Хорошо, начинаем"

start_command = commands.Command()

start_command.keys = ["старт", "start", "go"]
start_command.description = "запустить меня. добавь через пробел ссылку на нужный тебе поиск в авито и я буду присылать уведомления о новых сообщениях там\n\nпример: start https://www.avito.ru/moskva/kvartiry?s=104&s_trg=11"
start_command.process = start