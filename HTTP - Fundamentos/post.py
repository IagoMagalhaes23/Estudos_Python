"""
    Autor: Iago Magalhães
    Descrição:
        - Exemplo de uma requisição http (POST)
"""

#Realizando post
import requests 
API_ENDPOINT = "http://pastebin.com/api/api_post.php"
API_KEY = "XXXXXXXXXXXXXXXXX"
source_code = 
data = {'api_dev_key':API_KEY, 
        'api_option':'paste', 
        'api_paste_code':source_code, 
        'api_paste_format':'python'} 
r = requests.post(url = API_ENDPOINT, data = data) 
pastebin_url = r.text 
print("The pastebin URL is:%s"%pastebin_url)