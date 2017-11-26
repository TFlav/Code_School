sale = int(input('How many boxes do you want to buy? '))
if sale > 10 and sale < 100:
    print(sale)
    sale = sale - 10
    print(sale)
    c = (sale * 20) * 0.9
    print(c)
    sale = c + sale + 200
    print('$'+str(sale))
elif sale > 1 and sale <= 9:
    sale = sale * 20
    print('$'+str(sale))
elif sale >= 100:
    DC = sale * 0.2
    total = (sale - 20)  * DC
    print('$'+str(total))
else:
    print('Invalid number')
