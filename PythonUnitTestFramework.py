import unittest

def setUpModule():
    print("Before class")
def tearDownModule():
    print("after class")
class appTesting(unittest.TestCase):
    @classmethod
    def setUp(self) :
        print("Before every method")
    @classmethod
    def tearDown(self) :
        print("after every method")
    @classmethod
    def setUpClass(cls) :
        print("Only one time before all method")
    @classmethod
    def tearDownClass(cls):
        print("Only one time after all method")

    @unittest.SkipTest
    def test_search(self):
        print("This is search method")

    def test_advance(self):
        print("This is advance method")

    @unittest.skip("This method skipped")
    def test_preRecharge(self):
        print("This is pre Recharge")

    def test_postRecharge(self):
        print("This is post recharge")

if __name__== "__main__":
    unittest.main()
