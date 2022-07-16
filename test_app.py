import unittest
from app import OrderTotalPriceCalculator
from unittest.mock import patch

@patch("app.print")
class TestApp(unittest.TestCase):
    def test_invalid_province(self, mock_print):
        OrderTotalPriceCalculator(1, 1, "CD")
        mock_print.assert_called_once_with("Invalid province.")

    def test_missing_province(self, mock_print):
        OrderTotalPriceCalculator(1, 1)
        mock_print.assert_called_once_with("Invalid province.")
    
    def test_invalid_price(self, mock_print):
        OrderTotalPriceCalculator(1, -1, "ON")
        mock_print.assert_called_once_with("Invalid price.")

    def test_invalid_items(self, mock_print):
        OrderTotalPriceCalculator(-10, 1, "ON")
        mock_print.assert_called_once_with("Invalid number of items.")

    def test_order_discount1(self, mock_print):
        calculator = OrderTotalPriceCalculator(10, 20, "ON")
        calculator.get_order_total_price()
        mock_print.assert_called_once_with("$226.00")
   
    def test_order_discount2(self, mock_print):
        calculator = OrderTotalPriceCalculator(100, 20, "ON")
        calculator.get_order_total_price()
        mock_print.assert_called_once_with("$2192.20")
    
    def test_order_discount3(self, mock_print):
        calculator = OrderTotalPriceCalculator(100, 55, "ON")
        calculator.get_order_total_price()
        mock_print.assert_called_once_with("$5904.25")
    
    def test_order_discount4(self, mock_print):
        calculator = OrderTotalPriceCalculator(100, 70, "ON")
        calculator.get_order_total_price()
        mock_print.assert_called_once_with("$7356.30")
    
    def test_order_discount5(self, mock_print):
        calculator = OrderTotalPriceCalculator(100, 150, "ON")
        calculator.get_order_total_price()
        mock_print.assert_called_once_with("$15255.00")
        
    def test_order_discount6(self, mock_print):
        calculator = OrderTotalPriceCalculator(0, 150, "ON")
        calculator.get_order_total_price()
        mock_print.assert_called_once_with("$0.00")
    
        
if __name__ == "__main__":
    unittest.main()
