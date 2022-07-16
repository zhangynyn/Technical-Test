import argparse

from constants import Province, ProvinceTax, OrderDiscount

class OrderTotalPriceCalculator:
    @staticmethod
    def parse_arguments():
        parser = argparse.ArgumentParser(description='Process some integers.')
        parser.add_argument('items', type=int,
                    help='number of itmes')
        parser.add_argument('price', type=float,
                    help='price')
        parser.add_argument('province', type=str,
                    help='province')
        arguments = parser.parse_args()
        items = arguments.items
        price = arguments.price
        province = arguments.province
        return OrderTotalPriceCalculator(items, price, province)

    def __init__(self, items=None, price=None, province=None) -> None:
        if items is None or items < 0:
            print('Invalid number of items.')
            return
        self._items = items
        if price is None or price < 0:
            print('Invalid price.')
            return
        self._price = price
        if province is None or province not in Province.all_members():
            print("Invalid province.")
            return
        self._province = Province(province)
        self._base = self._items * self._price
    
    def _get_province_tax_rate(self):
        return ProvinceTax[self._province]
    
    def _get_order_discount_rate(self):
        thresholds = sorted(OrderDiscount.keys())
        target_threshold = None
        for i in range(len(thresholds)):
            if i == len(thresholds) - 1:
                target_threshold = thresholds[-1]
            elif self._base >= thresholds[i] and self._base < thresholds[i + 1]:
                target_threshold = thresholds[i]
                break
        discount_rate = OrderDiscount[target_threshold]

        return discount_rate
            
    def get_order_total_price(self):
        discount = self._base * (1-self._get_order_discount_rate())
        after_tax = discount * (1 + self._get_province_tax_rate())
        print("$%.2f" % round(after_tax, 2))

def total_cost(item_counts, unit_price):
    return item_counts * unit_price


if __name__ == "__main__":
    a = OrderTotalPriceCalculator.parse_arguments()
    a.get_order_total_price()
    
    