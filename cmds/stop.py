import commands
import define

def stop(user_id, token, *args):
    if str(user_id) in define.scheduler.keys():
        define.scheduler[str(user_id)].shutdown(wait=False)
        define.scheduler.pop(str(user_id), None)
        return "Окей, заканчиваю. Если что - знаешь, где меня найти &#128521;"
    else:
        return "Мы и не начинали вроде как(:"

stop_command = commands.Command()

stop_command.keys = ["стоп", "остановись", "выход", "stop"]
stop_command.description = "завершу свою работу и перестану тебя донимать сообщениями"
stop_command.process = stop