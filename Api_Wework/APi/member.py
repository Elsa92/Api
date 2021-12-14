import requests

from Api_Wework.Common.basepage import BasePage


class Member(BasePage):

    def add_member(self, userid, name, mobile, department=[1, 2], **kwargs):
        data = {
            'name': name,
            'userid': userid,
            'mobile': mobile,
            'department': department
        }
        data.update(kwargs)
        r = requests.request('POST', self.Base_url+f'user/create?access_token={self.token}', json=data)
        return r

    def get_member(self, userid):
        r = requests.request('GET', self.Base_url+f'user/get?access_token={self.token}&userid={userid}')
        return r

    def update_member(self, userid):
        data = {
            'userid': userid
        }
        r = requests.request('POST', self.Base_url+f'user/update?access_token={self.token}', json=data)
        return r

    def delete_member(self, userid):
        r = requests.request('GET', self.Base_url+f'user/delete?access_token={self.token}&userid={userid}')
        return r

    def batch_delete_member(self, useridlist):
        data = {
            'useridlist': useridlist
        }
        r = requests.request('POST', self.Base_url+f'user/batchdelete?access_token={self.token}', json=data)
        return r


