#coding:utf-8

import unittest
import HTMLTestRunnerCN
import time
import os


class TEST(unittest.TestCase):
    def setUp(self):
        self.age = 32
        self.name   = "小D课堂"
        print("setUp method")

    def test_one(self):
        print("test_one 二当家小D来了")
        self.assertEqual(self.name,"小D课堂",msg = "名字不对")

    # def test_two(self):
    #     print("test_two 第二个测试")
    #     self.assertFalse('XD'.isupper(),msg = "不是大写")

    def test_three(self):
        print("test_three 第三个测试")
        self.assertEqual(self.age,32)

    def tearDown(self):
        print("tearDown")
        self.assertEqual('foo'.upper(),'FOO')


if __name__ == "__main__":

    print(123)
    suite = unittest.TestSuite()
    suite.addTest(TEST("test_one"))
    # suite.addTest(TEST("test_two"))
    suite.addTest(TEST("test_three"))

    # report_dir = './test_report'
    # # 报告命名时间格式化
    # now = time.strftime("%Y-%m-%d %H_%M_%S")
    # # 报告文件完整路径
    # report_name = report_dir + '/' + now + 'result.html'
    # print(report_name)

    file_name = time.strftime("%Y-%m-%d %H_%m_%S",time.localtime())
    print(file_name)

    # report_path = os.path.join(os.getcwd(), "Day13")
    # report_abspath = os.path.join(report_path, "result.html")
    # fp = open(report_abspath, "wb")

    fp = open("./"+file_name+"_result.html","wb")
    runner = HTMLTestRunnerCN.HTMLTestReportCN(stream=fp,title="测试报告",description="测试执行情况")
    runner.run(suite)
    fp.close()
    print(456)