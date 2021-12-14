import allure

from Api_Wework.APi.member import Member

@allure.feature('管理成员')
class TestMember:

    def setup_class(self):
        self.member = Member()

    @allure.story('添加成员')
    @allure.title('成功添加成员')
    def test_add_member(self, member_info):
        with allure.step('添加成员'):
            r = self.member.add_member(*member_info)
        with allure.step('断言：判断errcode是否是0'):
            assert r.json().get('errcode') == 0

    @allure.story('读取成员')
    @allure.title('成功读取成员')
    def test_get_member(self, member_info):
        with allure.step('添加成员'):
            self.member.add_member(*member_info)
        with allure.step('读取该成员'):
            r = self.member.get_member(member_info[0])
        with allure.step('断言：判断errcode是否是0'):
            assert r.json().get('errcode') == 0

    @allure.story('更新成员')
    @allure.title('成功更新成员')
    def test_update_member(self, member_info):
        with allure.step('添加成员'):
            self.member.add_member(*member_info)
        with allure.step('更新该成员'):
            r = self.member.update_member(member_info[0])
        with allure.step('断言：判断errcode是否是0'):
            assert r.json().get('errcode') == 0

    @allure.story('删除成员')
    @allure.title('成功删除成员')
    def test_delete_member(self, member_info):
        with allure.step('添加成员'):
            self.member.add_member(*member_info)
        with allure.step('删除该成员'):
            r = self.member.delete_member(member_info[0])
        with allure.step('断言：判断errcode是否是0'):
            assert r.json().get('errcode') == 0
