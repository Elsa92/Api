import requests

from Api_Wework.Common.basepage import BasePage


class Department(BasePage):

    def create_department(self,depart_name,parentid = 1):
        data = {
            "name":depart_name,
            "parentid": parentid
        }

        r = requests.request('POST', self.Base_url+f'department/create?access_token={self.token}',json=data)
        return r

    def update_department(self,depart_id,depart_name):
        data = {
            'id': depart_id,
            'name': depart_name
        }
        r= requests.request('POST', self.Base_url+f'department/update?access_token={self.token}', json=data)
        return r

    def delete_department(self,depart_id):
        r = requests.request('GET', self.Base_url+f'department/delete?access_token={self.token}&id={depart_id}')
        return r

    def get_department(self):
        r = requests.request('GET',self.Base_url+f'department/list?access_token={self.token}&id=1')
        return r


