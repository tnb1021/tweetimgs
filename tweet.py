import requests
import twitter
import urllib.request
import requests
from requests_oauthlib import OAuth1Session
import json


CK=''
CS=''
AT=''
AS=''
twitter = OAuth1Session(CK,CS,AT,AS)

url_media = "https://upload.twitter.com/1.1/media/upload.json"
url_text = "https://api.twitter.com/1.1/statuses/update.json"

img_url = ['https://1.bp.blogspot.com/-SWOiphrHWnI/XWS5x7MYwHI/AAAAAAABUXA/i_PRL_Atr08ayl9sZy9-x0uoY4zV2d5xwCLcBGAs/s1600/pose_dance_ukareru_man.png',
            'https://1.bp.blogspot.com/-CSIokkL0VJc/XVKgHNKp2QI/AAAAAAABUHU/znkuxlOlQ5giZ3gDbks7KAK3TJnT2q1XwCLcBGAs/s1600/kotowaza_hato_mamedeppou.png',
            'https://1.bp.blogspot.com/-8sMAiPmvFuo/XVjgKN2BXoI/AAAAAAABUM0/IfTQp8hHWRsVk_u7s84OE6yvFJ5ekpnLwCLcBGAs/s1600/kid_seikaku_uchiki_girl.png',
            'https://1.bp.blogspot.com/-ahlT7Kd7-T0/XVjgJ3hrbFI/AAAAAAABUMw/MV4su85SnoAMYnSitR9DXVgNFuorpprwQCLcBGAs/s1600/kid_seikaku_uchiki_boy.png']

def call():    
    media_id = []
    for i in range(4):
        headers = {"User-Agent": "Mozilla/5.0"}
        request = urllib.request.Request(url=img_url[i],headers=headers)
        response = urllib.request.urlopen(request)
        data = response.read()
        files = {"media" : data}
        req_media = twitter.post(url_media,files = files)
        media_id.append(json.loads(req_media.text)['media_id_string'])
    media_id= ','.join(media_id)
    status = "投稿テスト"
    params = {"status": status, "media_ids": media_id}
    twitter.post(url_text,params=params)
    
        
if __name__ =='__main__':
    call()

            

