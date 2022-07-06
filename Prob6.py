# Problem 6
purchase = float(input('Amount of purchase: '))
installment = float(input('Number of installment: '))
total_purchase = (0.05 * purchase) 
cost = total_purchase / installment
print(f'This is the total number of purchases: {total_purchase}')
print(f'Each installment will cost: {cost:.2f}')

