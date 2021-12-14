import requests


class BasePage:
    Base_url = 'https://qyapi.weixin.qq.com/cgi-bin/'
    Cropid = 'wwaa89f195bc7712dc'
    Cropsecret = 'oTZk7TaP6uCldmbEIVD6yvbumw3kyqgqyM9Snk6ptBo'

    def __init__(self):
        self.token = self.get_token()

    def get_token(self):
        r = requests.get(self.Base_url+f"gettoken?corpid={self.Cropid}&corpsecret={self.Cropsecret}")
        return r.json().get('access_token')

    def send(self,method,url,**kwargs):
        url = self.Base_url+url
        requests.request(method,url,**kwargs)

