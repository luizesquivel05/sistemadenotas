gabarito = input('Digite o gabarito da prova: ').lower() # leitura do gabarito e o deixa em minúsculo.
qtdAlunos = int(input('Digite a quantidade de alunos: ')) # leitura da quantidade de alunos.
dados = list() # lista para armazenar informações dos estudantes.

# funcao que irá receber as informações dos estudantes e envia para a lista:
def infoAlunos(qtdAlunos, gabarito):
    for i in range(qtdAlunos):
        matricula = int(input('Matricula do Aluno: '))
        nome = str(input('Nome do aluno: ').lower())
        resp = str(input('Resposta do aluno: ').lower())
        nota = calcularNota(resp, gabarito)
        dados.append({'nome': nome, 'matricula': matricula, 'nota': nota})

# funcao que irá calcular a notas:
def calcularNota(resp, gaba):
    nota = 0
    for x in range(len(gaba)):
        if resp[x] == gaba[x]:
            nota += 1
    return nota

# função que usará para ordenar a lista com os nomes dos estudantes:
def ordenarNome(qtdAlunos):
    for i in range(qtdAlunos):
        ordenar = sorted(dados, key=lambda row: row['nome']) # esse comando lambda que realizará uma filtragem das linhas a partir da coluna nome.
        print(ordenar[i])

# função que irá ser usada para ordenar a lista de informações dos estudantes a partir da ordem crescente de notas:        
def ordenarNota(qtdAlunos):
    for i in range(qtdAlunos):
        ordenar = sorted(dados, key=lambda row: row['nota']) # esse comando lambda que realizará filtragem de linhas a partir da coluna nota.
        print(ordenar[i])