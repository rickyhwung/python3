principal_amount = 100
print('principa amount:{}'.format(principal_amount))
for i in range(1, 9):
    principal_amount = principal_amount * 1.05
    print('year {}: ${}'.format(i, principal_amount))
