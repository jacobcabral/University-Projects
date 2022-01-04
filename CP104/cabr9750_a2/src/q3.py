"""
------------------------------------------------------------------------
[calculates the profits from a percent and a sales total]
------------------------------------------------------------------------
Author: Jacob Cabral
ID:     190689750
Email:  cabr9750@mylaurier.ca
__updated__ = "2019-09-17"
------------------------------------------------------------------------
"""
total_sales = float(input("Enter the total amout of sales: "))
ANNUAL_PROFIT = 0.23
final_profit = total_sales * ANNUAL_PROFIT

print("Projected Profits")
print("--------------------")
print("Total Sales :$", total_sales)
print("Annual profit: %",ANNUAL_PROFIT*100)
print("--------------------")
print("Profit: $",final_profit)


