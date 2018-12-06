from flask import Flask, json, request
import os
import define
import msgHandler

app = Flask(__name__)

#app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", define.SECRET_KEY)

@app.route('/')
def mainpage():
    return "Backend of Avito Notificatons VK Bot"

@app.route('/', methods=['POST'])
def processing():
    data = json.loads(request.data)

    if data["type"] == "confirmation":
            return define.vk_confirm_token
    elif data["type"] == "message_new":
        msgHandler.answer(data["object"], define.vk_msg_access_token)
        return "OK"
    else:
        return "Not valid"


port = int(os.environ.get("PORT", 5000))
app.run(host="0.0.0.0", port=port, debug=True)