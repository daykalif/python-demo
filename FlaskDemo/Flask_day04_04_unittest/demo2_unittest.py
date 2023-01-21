import json
import unittest
from demo2 import app


class LoginTestCase(unittest.TestCase):
    def setUp(self):
        app.testing = True  # 开启后可以显示错误在哪一行出现
        """在开始执行测试的方法之后会调用该方法，该方法里面可以做一些初始化操作"""
        self.client = app.test_client()

    def tearDown(self):
        pass

    # 单元测试的方法要以test开头
    def test_empty_username_password(self):
        # 1.如果传入的参数不足，会返回errcode=-2
        response = app.test_client().post('/login', data={})
        resp_data = response.data
        json_dict = json.loads(resp_data)

        print(json_dict)

        self.assertIsNotNone(json_dict, '未获取到返回值')
        self.assertIn("errcode", json_dict, "返回数据格式不正确")
        errcode = json_dict.get("errcode")
        self.assertEqual(errcode, -2, "返回的状态码错误")

        # 2.如果传入的账号与密码不正确会返回errcode=-1
        # 3.如果账号与密码正确，errcode=0
