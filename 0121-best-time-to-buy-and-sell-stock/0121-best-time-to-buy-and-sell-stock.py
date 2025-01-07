class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0


        min_price = sys.maxsize
        # 최솟값과 최댓값을 계속 갱신
        for price in prices:
            min_price = min(min_price, price) # 주식 구매 가격을 구할 때 최소값을 찾음
            profit = max(profit, price - min_price) # 최대 이익을 찾음 "price(=판매가격) - min_price(=구매가격)"을 계산하여 최대 이익을 찾음
        return profit

            