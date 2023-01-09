# gabarito: abdebaabcd

def calcularNota(resp, gaba):
    nota = 0
    for x in range(len(gaba)):
        if resp[x] == gaba[x]:
            nota += 1
    return nota

def infoAlunos(qtdAlunos, gabarito):
    for i in range(qtdAlunos):
        matricula = int(input('Matricula do Aluno: '))
        nome = str(input('Nome do aluno: ').lower())
        resp = str(input('Resposta do aluno: ').lower())
        nota = calcularNota(resp, gabarito)
        dados.append({'nome': nome, 'matricula': matricula, 'nota': nota})


def ordenarNome(qtdAlunos):
    for i in range(qtdAlunos):
        ordenar = sorted(dados, key=lambda row: row['nome'])
        print(ordenar[i])


def ordenarNota(qtdAlunos):
    for i in range(qtdAlunos):
        ordenar = sorted(dados, key=lambda row: row['nota'])
        print(ordenar[i])


def ordemMaior7(qtdAlunos):
    ordenar = sorted(dados, key=lambda row: row['nota'])
    for i in range(qtdAlunos):
        if ordenar[i]['nota'] >= 7:
            aux = ordenar[i]
            print(aux)


def ordemMenor7(qtdAlunos):
    ordenar = sorted(dados, key=lambda row: row['nota'], reverse=True)
    for i in range(qtdAlunos):
        if ordenar[i]['nota'] < 7:
            aux = ordenar[i]
            print(aux)


def percentualAprovacao(qtdAlunos):
    cont = 0
    aprovado = 0
    for i in range(qtdAlunos):
        if dados[i]['nota'] >= 7:
            aprovado += 1
            cont += 1
        else:
            cont += 1
    percent = (aprovado/cont)*100
    print(f'O percentual de aprovação é {percent:,.2f}%')


def maiorFrequencia(qtdAlunos):
    ordem = list()
    for i in range(qtdAlunos):
        nota = dados[i]['nota']
        ordem.append(nota)
        res = max(set(ordem), key=ordem.count)
    print("A nota com maior frequencia é: " + str(res))


def maiorNota(qtdAlunos):
    notas = list()
    for i in range(qtdAlunos):
        nota = dados[i]['nota']
        notas.append(nota)
        maiorNota = max(notas)
    for i in range(qtdAlunos):
        if notas[i] == maiorNota:
            print(dados[i])


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
info = infoAlunos(qtdAlunos, gabarito)
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
        ordenar = ordenarNome(qtdAlunos)
    if opcao == 2:
        ordenar = ordenarNota(qtdAlunos)
    if opcao == 3:
        ordenar = ordemMaior7(qtdAlunos)
    if opcao == 4:
        ordenar = ordemMenor7(qtdAlunos)
    if opcao == 5:
        aprovacao = percentualAprovacao(qtdAlunos)
    if opcao == 6:
        frequencia = maiorFrequencia(qtdAlunos)
    if opcao == 7:
        maior = maiorNota(qtdAlunos)
    if opcao == 8:
        menor = menorNota(qtdAlunos)
    if opcao == 9:
        media = mediaTurma(qtdAlunos)
    print('\n')
    print('Deseja voltar para o menu? Digite 1 para SIM e 0 para NÃO')
    loop = int(input())
    print('\n')
