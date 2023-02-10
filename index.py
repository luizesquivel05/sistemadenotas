import funcoes as fn
import texto as txt

if fn.fazerLOGIN() != "max":
    print(txt.start)
    requisito = str(input()).lower()
    print(fn.menu(csv=requisito))
else:
    print('Você ultrapassou o limite de tentativas!! O sistema foi desligado x-x')