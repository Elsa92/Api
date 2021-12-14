import requests

from Api_Wework.Common.basepage import BasePage


class Tag(BasePage):

    def add(self,tagname):
        data = {
            "tagname": tagname

        }
        r = requests.request('POST', self.Base_url+f'tag/create?access_token={self.token}', json=data)
        return r

    def update(self,tagid,tagname):
        data = {
            "tagname": tagname,
            "tagid": tagid
        }
        r = requests.request('POST', self.Base_url+f'tag/update?access_token={self.token}', json=data)
        return r
