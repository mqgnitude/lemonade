import unittest
from py.game_engine import Engine
class TestFinancials(unittest.TestCase):
    def setUp(self):
        self.engine = Engine("Easy")
    def test_revenue_calculation(self):
        self.engine.state.price = 10
        self.engine.state.inventory = 1000
        self.engine.calculate_demand = lambda: 10
        self.engine.process_turn()
        self.assertEqual(self.engine.state.total_revenue, 100.0)
    def test_buying_inventory(self):
        initial_cash = self.engine.state.cash
        cost = self.engine.product.cost_per_unit * 10
        success, msg = self.engine.buy_inventory(10)
        self.assertTrue(success)
        self.assertEqual(self.engine.state.inventory, 60)
        self.assertEqual(self.engine.state.cash, initial_cash - cost)
    def test_bankruptcy_limit(self):
        self.engine.state.cash = 0
        success, msg = self.engine.buy_inventory(100)
        self.assertFalse(success)
if __name__ == '__main__':
    unittest.main()