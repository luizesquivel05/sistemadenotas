gabarito = input('Digite o gabarito da prova: ').lower() # leitura do gabarito e o deixa em minúsculo.
qtdAlunos = int(input('Digite a quantidade de alunos: ')) # leitura da quantidade de alunos.
dados = list() # lista para armazenar informações dos estudantes.

# funcao para receber as informações dos estudantes e envia para a lista:
def infoAlunos(qtdAlunos, gabarito):
    for i in range(qtdAlunos):
        matricula = int(input('Matricula do Aluno: '))
        nome = str(input('Nome do aluno: ').lower())
        resp = str(input('Resposta do aluno: ').lower())
        nota = calcularNota(resp, gabarito)
        dados.append({'nome': nome, 'matricula': matricula, 'nota': nota})

# funcao para calcular a notas:
def calcularNota(resp, gaba):
    nota = 0
    for x in range(len(gaba)):
        if resp[x] == gaba[x]:
            nota += 1
    return nota