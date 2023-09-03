import requests

nums = "123456789"

symbols = "йцукенгшщзхъфывапролджэячсмитьбюё qwertyuiopasdfghjklzxcvbnm,.';!?"

token = 'token'


def Spam(id, text):
    response = requests.get("https://api.telegram.org/bot" + token + "/sendMessage", params={
        'chat_id': id,
        'text': text
    }
                            )
