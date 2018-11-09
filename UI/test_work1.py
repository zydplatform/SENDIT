import unittest
from work1 import check_order_status
class TestOrder(unittest.TestCase):
    def test_order_status(self):
        order_id = 32
        self.assertEqual(check_order_status(order_id),True)
    def test_num_not_present(self):
        order_id = -1
        self.assertEqual(check_order_status(order_id), False)
        self.assertFalse(check_order_status(order_id),True)
    # test if an input is an integer
    def test_id(self):
        order_id = 2
        self.assertEqual(check_order_status(order_id),True)
        