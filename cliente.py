import requests
import json

url = 'http://127.0.0.1:8000'

payload = {'remetente': '84997000080', 'menssagem': 'Isso aqui esta dando certo Fi.'}

r = requests.post(url, json=payload)
