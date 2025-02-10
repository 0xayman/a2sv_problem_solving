# Problem: Apply Discount Every n Orders - https://leetcode.com/problems/apply-discount-every-n-orders/description/

class Cashier:

    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.n = n
        self.discount = discount
        self.products = products
        self.prices = prices
        self.current_customer = 1
        self.product_price = {}

        for i in range(len(products)):
            self.product_price[products[i]] = prices[i]

    def getBill(self, product: List[int], amount: List[int]) -> float:
        bill = 0
        for i in range(len(product)):
            bill += amount[i] * self.product_price[product[i]]
        
        if self.current_customer % self.n == 0:
            bill = bill * ((100 - self.discount) / 100)

        self.current_customer += 1
        return bill 




# Your Cashier object will be instantiated and called as such:
# obj = Cashier(n, discount, products, prices)
# param_1 = obj.getBill(product,amount)