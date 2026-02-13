from flask import Flask, request
import requests

TOKEN = "HCHHI0POOCCEBRLYAKZCOJQOPWHFEZVNLUNDCFEWXIBNTVTGOTUVZYIBIOJHMAZR"
API_URL = f"https://botapi.rubika.ir/v3/{TOKEN}/"

app = Flask(__name__)

# فونت مپ حرفه‌ای
normal = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
fancy  = "𝑨𝑩𝑪𝑫𝑬𝑭𝑮𝑯𝑰𝑱𝑲𝑳𝑴𝑵𝑶𝑷𝑸𝑹𝑺𝑻𝑼𝑽𝑾𝑿𝒀𝒁𝒂𝒃𝒄𝒅𝒆𝒇𝒈𝒉𝒊𝒋𝒌𝒍𝒎𝒏𝒐𝒑𝒒𝒓𝒔𝒕𝒖𝒗𝒘𝒙𝒚𝒛"

def to_fancy(text):
    result = ""
    for char in text:
        if char in normal:
            result += fancy[normal.index(char)]
        else:
            result += char
    return result

def send_message(chat_id, text):
    url = API_URL + "sendMessage"
    data = {
        "chat_id": chat_id,
        "text": text
    }
    requests.post(url, json=data)

@app.route('/', methods=['POST'])
def webhook():
    data = request.json
    chat_id = data["chat_id"]
    text = data.get("text","")

    if text == "/start":
        send_message(chat_id, "اسم خود را به انگلیسی بفرستید:")
    else:
        fancy_name = to_fancy(text)
        tag = fancy_name + " ✸ اسـرافـیـل"
        send_message(chat_id, f"✦ Your Tag Is Ready ✦\n\n{tag}")

        welcome = """━━━━━━━━━━━━

به خانواده اسرافیل خوش اومدی ✸

تگدارا:
https://rubika.ir/joing/+JEFIFDJI0SIBXUPPFDCYTULBLZIBBUDE

شعبه ها:
https://rubika.ir/pov_YaDeGaR/BEJIDBJBBECIAFEF

قوانین:
https://rubika.ir/pov_YaDeGaR/BEJJBHJFAJIGIFEF
"""
        send_message(chat_id, خوش آمدید 💙)

    return "ok"

if __name__ == "__main__":
    app.run()
