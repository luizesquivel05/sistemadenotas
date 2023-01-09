import funcoes as fn

# gabarito: abdebaabcd


def menorNota(qtdAlunos):
    notas = list()
    for i in range(qtdAlunos):
        nota = dados[i]['nota']
        notas.append(nota)
        menorNota = min(notas)
    for i in range(qtdAlunos):
        if notas[i] == menorNota:
            print(dados[i])


def mediaTurma(qtdAlunos):
    nota = 0
    for i in range(qtdAlunos):
        nota += dados[i]['nota']
    media = (nota/qtdAlunos)
    print(f'A média da turma é: {media:,.2f}')


gabarito = input('Digite o gabarito da prova: ').lower()
qtdAlunos = int(input('Digite a quantidade de alunos: '))
dados = list()
info = fn.infoAlunos(qtdAlunos, gabarito)
loop = 1
while loop == 1:
    print('\n')
    print('Selecione uma das opções abaixo:\n')
    print('Digite 1 para ver a lista em ordem alfabética dos alunos com o número de matricula e a sua nota.\n')
    print('Digite 2 para ver a lista em ordem crescente de notas com o nome do aluno, o numero da matricula e a sua nota.\n')
    print('Digite 3 para ver a lista em ordem crescente de notas com o nome do aluno, o numero da matricula e a sua nota para os alunos aprovados (>= 7.0).\n')
    print('Digite 4 para ver a lista em ordem decrescente de notas com o nome do aluno, o numero da matricula e a sua nota para os alunos reprovados (< 7.0).\n')
    print('Digite 5 para ver o percentual de aprovação, sabendo-se que a nota mínima para aprovação é >= 7.0.\n')
    print('Digite 6 para ver a nota que teve a maior frequência absoluta.\n')
    print('Digite 7 para ver o aluno com a maior nota (nome, matricula e nota).\n')
    print('Digite 8 para ver o aluno com a menor nota (nome, matricula e nota).\n')
    print('Digite 9 para ver a media da turma.\n')
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
