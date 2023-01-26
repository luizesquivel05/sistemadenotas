gabarito = str()
for i in open('gabarito.csv', 'r'):
    gabarito += i[10]
print(gabarito)