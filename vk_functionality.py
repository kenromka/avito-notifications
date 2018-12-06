import vk

session = vk.Session()
api = vk.API(session, v=5.5)

def send_msg(user_id, token, message):
    api.messages.send(
        access_token=token,
        user_id=str(user_id),
        message=message
    )
    pass