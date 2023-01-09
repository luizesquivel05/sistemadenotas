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
  
# função que irá ser usada para ordenar a lista de informações dos estudantes a partir da ordem crescente de notas, para alunos aprovados (nota maior que 7):
def ordemMaior7(qtdAlunos):
    ordenar = sorted(dados, key=lambda row: row['nota']) # esse comando lambda que realizará filtragem de linhas a partir da coluna nota.
    for i in range(qtdAlunos): 
        if ordenar[i]['nota'] >= 7: # limita o filtro para notas maior ou igual a 7
            aux = ordenar[i]
            print(aux)
            
# função que irá ser usada para ordenar a lista de informações dos estudantes a partir da ordem decrescente de notas, para alunos reprovados (nota menor que 7):
def ordemMenor7(qtdAlunos):
    ordenar = sorted(dados, key=lambda row: row['nota'], reverse=True) # esse comando lambda que realizará filtragem de linhas a partir da coluna nota.
    for i in range(qtdAlunos):
        if ordenar[i]['nota'] < 7: # limita o filtro para notas menores que 7
            aux = ordenar[i]
            print(aux)
            
# função que irá apresentar o percentual de estudantes que foram aprovados na turma:
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
    
# função que irá apresentar as notas que mais se repetem:
def maiorFrequencia(qtdAlunos):
    ordem = list()
    for i in range(qtdAlunos):
        nota = dados[i]['nota']
        ordem.append(nota)
        res = max(set(ordem), key=ordem.count) # método max() usado para pegar maiores notas e método set() usado para limitar para remover duplicados.
    print("A nota com maior frequencia é: " + str(res))