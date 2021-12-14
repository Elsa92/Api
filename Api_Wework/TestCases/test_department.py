import allure

from Api_Wework.APi.department import Department

@allure.feature('部门管理')
class TestDepart:

    def setup_class(self):
        self.depart = Department()

    @allure.story('创建部门')
    @allure.title('成功创建部门')
    def test_create_depart(self,depart_name):
        with allure.step('创建部门'):
            r = self.depart.create_department(depart_name)
        with allure.step('断言：判断errcode是否是0'):
            assert r.json().get('errcode') == 0

    @allure.story('更新部门')
    @allure.title('成功更新部门')
    def test_update_depart(self,depart_name):
        with allure.step('创建新部门'):
            new_depart = self.depart.create_department(depart_name)
        with allure.step('更新该部门'):
            r = self.depart.update_department(new_depart.json().get('id'),depart_name)
        with allure.step('断言：判断errcode是否是0'):
            assert r.json().get('errcode') == 0

    @allure.story('删除部门')
    @allure.title('成功删除部门')
    def test_delete_depart(self,depart_name):
        with allure.step('创建新部门'):
            new_depart = self.depart.create_department(depart_name)
        with allure.step('删除该部门'):
            r = self.depart.delete_department(new_depart.json().get('id'))
        with allure.step('断言：判断errcode是否是0'):
            assert r.json().get('errcode') == 0

    @allure.story('获取部门列表')
    @allure.title('成功获取部门列表')
    def test_get_depart(self):
        with allure.step('获取部门列表'):
            r = self.depart.get_department()
        with allure.step('断言：判断errcode是否是0'):
            assert r.json().get('errcode') == 0

