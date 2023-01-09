import funcoes as fn
import texto as txt

gabarito = input('Digite o gabarito da prova: ').lower()
qtdAlunos = int(input('Digite a quantidade de alunos: '))
info = fn.infoAlunos(qtdAlunos, gabarito)
loop = 1
while loop == 1:
    print(txt.menu())
    opcao = int(input())
    print('\n')
    if opcao == 1:
        ordenar = fn.ordenarNome(qtdAlunos)
    if opcao == 2:
        ordenar = fn.ordenarNota(qtdAlunos)
    if opcao == 3:
        ordenar = fn.ordemMaior7(qtdAlunos)
    if opcao == 4:
        ordenar = fn.ordemMenor7(qtdAlunos)
    if opcao == 5:
        aprovacao = fn.percentualAprovacao(qtdAlunos)
    if opcao == 6:
        frequencia = fn.maiorFrequencia(qtdAlunos)
    if opcao == 7:
        maior = fn.maiorNota(qtdAlunos)
    if opcao == 8:
        menor = fn.menorNota(qtdAlunos)
    if opcao == 9:
        media = fn.mediaTurma(qtdAlunos)
    print('\n')
    print('Deseja voltar para o menu? Digite 1 para SIM e 0 para NÃO')
    loop = int(input())
    print('\n')