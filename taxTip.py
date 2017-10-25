tax_rate = 0.05 #in python we represent 5% as 0.05
tip_rate = 0.18

cost_of_meal = float(input("Pls enter  cost of your meal:"))

tax = cost_of_meal * tax_rate
tip = cost_of_meal * tip_rate

total = cost_of_meal + tax + tip

print(total)