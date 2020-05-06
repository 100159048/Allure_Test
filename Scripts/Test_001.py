import pytest,allure
class Test_abc:

    #描述
    @allure.description("这是一个一直执行成功的测试用例")
    #测试步骤
    @allure.step(title="第二个测试")

    @allure.severity(allure.severity_level.BLOCKER)
    #@pytest.allure.severity(pytest.allure.severity_level.BLOCKER)
    def test_001(self):

        assert True

    # @allure.step(title="第一个测试")
    # def test_002(self):
    #     # allure.attach("这是个描述", "试一下啊")
    #     assert False
