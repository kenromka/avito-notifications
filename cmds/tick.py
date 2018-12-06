import commands
import define

def tick(user_id, token, *args):
    time = define.update_time.get(str(user_id), 3)
    for num in args:
        try:
            time = int(num)
        except:
            continue
    define.update_time[str(user_id)] = time
    return f"Договорились, буду писать не чаще раза в {define.update_time.get(str(user_id), 3)} мин. &#8987;"

tick_command = commands.Command()

tick_command.keys = ["тик", "tick", "время", "update"]
tick_command.description = "введи 'тик [время_в_минутах]' и так часто я буду проверять новые объявления.\nпо умолчанию стоит 3 мин."
tick_command.process = tick