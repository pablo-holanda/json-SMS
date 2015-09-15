import requests
import json

url = 'http://192.168.1.95:8000'

payload = {'remetente': '5584997000080', 'menssagem': 'Isso aqui esta dando certo Fi.'}

r = requests.post(url, json=payload)
