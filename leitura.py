gabarito = str()
cont = int(0)
for i in open('gabarito.csv', 'r'):
    if cont > 0: gabarito += i[4]
    else: cont += 1