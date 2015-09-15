import requests

url = 'http://179.156.26.52:8000'
# url = 'http://192.168.1.95:8000'

payload = {'remetente': '5584999923633', 'mensagem': 'Jean, deu certo boe.'}

r = requests.post(url, json=payload)
