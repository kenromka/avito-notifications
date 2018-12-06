import requests
from urllib3.poolmanager import PoolManager
import ssl
import re
import define
from vk_functionality import send_msg

class TLSAdapter(requests.adapters.HTTPAdapter):
    def init_poolmanager(self, connections, maxsize, block=False):
        self.poolmanager = PoolManager(
            num_pools=connections,
            maxsize=maxsize,
            block=block,
            ssl_version=ssl.PROTOCOL_TLSv1_2
            )

def init_session(adapter):
    session = requests.Session()
    session.mount('https://', adapter)
    #session.cookies.clear()

    return session

def improve_link(link):
    return link+"&s=104"

def continious_search(session, link, user_id, token, proxies=None):
    link = improve_link(link)
    r = session.get(
                link,
                proxies=proxies,
                headers = {
                    "Host": "www.avito.ru",
                    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0",
                    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                    "Accept-Language": "en-US,en;q=0.5",
                    "Accept-Encoding": "gzip, deflate, br",
                    "Connection": "keep-alive",
                    "Upgrade-Insecure-Requests": "1",
                    "Pragma": "no-cache",
                    "Cache-Control": "no-cache"
                },
                allow_redirects=False
    )
    if r.status_code != 200:
        send_msg(user_id, token, "Упс, кажется avito меня заблокировал")
        print("BLOCK", r.status_code, r.text, sep="\n")
        pass
    new_lst = re.finditer(
                    r"(item-description-title-link\")([^/]*)([^\"]*)",
                    r.text
            )
    exist_lst = [i[3] for i in new_lst]

    res = list(set(exist_lst) - set(define.exist_lsts.get(str(user_id), exist_lst)))
    send(user_id, token, res)
    define.exist_lsts[str(user_id)] = exist_lst
    pass

def send(user_id, token, items):
    if len(items) != 0:
        send_msg(
                user_id,
                token,
                f"Появились новые объявления: {len(items)} шт."
            )
    for n, item in enumerate(items):
        if n < 10:
            send_str = f"{n+1}&#8419; объявление:\n https://www.avito.ru{item}"
        else:
            send_str = f"{n+1} объявление:\n https://www.avito.ru{item}"
        send_msg(
            user_id,
            token,
            send_str
        )
    pass