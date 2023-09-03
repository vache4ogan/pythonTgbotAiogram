import requests

nums = "123456789"

symbols = "йцукенгшщзхъфывапролджэячсмитьбюё qwertyuiopasdfghjklzxcvbnm,.';!?"

token = '6475977596:AAHcPZY74-FZVO7iLz7zadjC18JabpbNGWs'


def Spam(id, text):
    response = requests.get("https://api.telegram.org/bot" + token + "/sendMessage", params={
        'chat_id': id,
        'text': text
    }
                            )
