import allure

from Api_Wework.APi.tag import Tag

@allure.feature('标签管理')
class TestTag:

    def setup_class(self):
        self.tag = Tag()

    @allure.story('添加标签')
    @allure.title('成功添加标签')
    def test_add_tag(self,get_name):
        with allure.step('添加标签'):
            r = self.tag.add(get_name)
        with allure.step('断言：判断errcode是否是0'):
            assert r.json().get('errcode') == 0

    @allure.story('更新标签')
    @allure.title('成功更新标签')
    def test_update_tag(self, get_name):
        with allure.step('添加标签'):
            new_tag = self.tag.add(get_name).json()
        with allure.step('更新该标签'):
            new_r = self.tag.update(new_tag.get('tagid'), get_name)
        with allure.step('断言：判断errcode是否是0'):
            assert new_r.json().get('errcode') == 0



