prices = [7,1,5,3,6,4]
actual = 0
# for i in range(len(prices)):
#     local = 0
#     for j in range(i, len(prices)):
#         local = prices[j]-prices[i]
#         if local>=actual:
#             actual = local
#########################
# right = len(prices)-1
# left = 0
# while left<right:
#     if prices[right]-prices[left] > actual:
#         actual = prices[right]-prices[left]
#     left +=1
#     right -=1
#########################
# return actual
#########################
min = prices[0]
profit = 0
for i in range(len(prices)):
    if prices[i] < min:
        min = prices[i]
    profit_1 = prices[i] - min
    if profit_1 > profit:
        profit = profit_1

print(profit)