import texto as txt
import leitura as lt
import os
import loginecadastro as lg

dados = list() # lista para armazenar informações dos estudantes.,


# Função para validação dos dados de nome de usuário e senha:
def autenticar(nome_de_usuario, senha):
    for usuario in lg.usuarios:
        if usuario["login"] == nome_de_usuario and usuario["senha"] == senha:
            return True
    return False

# Função que realiza leitura de nome de usuário e senha e, em seguida, valida:
def fazerLOGIN():
    i = 4
    while i >= 0:
        nome_de_usuario = input("Nome de usuário: ")
        senha = input("Senha: ")
        if autenticar(nome_de_usuario, senha):
            os.system('cls')
            break
        else:
            print("Falha no login. Por favor, tente novamente.")
            i -= 1
    else:
        return "max"
# funcao que irá receber as informações dos estudantes e envia para a lista:
def infoAlunos(qtdAlunos, gabarito):
    for i in range(qtdAlunos):
        matricula = int(input('Matricula do Aluno: '))
        nome = str(input('Nome do aluno: ').lower())
        resp = str(input('Resposta do aluno: ').lower())
        nota = calcularNota(resp, gabarito, csv="N")
        dados.append({'nome': nome, 'matricula': matricula, 'nota': nota})
            
# funcao que irá receber as informações dos estudantes a partir do csv:
def infoalunosCSV():
    for i in open('respostas.csv', 'r'):
        aux = i.split(';')
        matricula = aux[0][10:]
        nome = aux[1][5:]
        resps = aux[2][10:]
        nota = calcularNota(resp=resps, gaba=lt.gabarito, csv="S")
        dados.append({'nome': nome, 'matricula': matricula, 'nota': nota})
    return dados

# funcao que irá calcular a notas:
def calcularNota(resp, gaba, csv):
    nota = 0
    if csv == "N":
        for x in range(len(gaba)):
            if resp[x] == gaba[x]:
                nota += 1
        return nota
    else:
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
    ordem = list()  # usada para ordenar a lista
    for i in range(qtdAlunos):
        nota = dados[i]['nota']
        ordem.append(nota)
    unicos = set(ordem) # traz valores únicos
    aux = dict()
    aux1 = list() # traz lista das frequências
    for i in unicos:
        freq = ordem.count(i)
        aux[i] = freq
        aux1.append(freq)      
    maiorFREQ = max(aux1) # traz a maior frequência
    res = list() # traz a resposta final
    for j in aux:
        if aux[j] == maiorFREQ:
            res.append(j)
    print("A nota com maior frequencia é: " + str(res))
    
# função que irá apresentar a maior nota dentre os estudantes:
def maiorNota(qtdAlunos):
    notas = list()
    for i in range(qtdAlunos):
        nota = dados[i]['nota']
        notas.append(nota)
        maiorNota = max(notas)
    for i in range(qtdAlunos):
        if notas[i] == maiorNota:
            print(dados[i])
            
# função que irá apresentar a menor nota dentre os estudantes:
def menorNota(qtdAlunos):
    notas = list()
    for i in range(qtdAlunos):
        nota = dados[i]['nota']
        notas.append(nota)
        menorNota = min(notas) # O método min() é usado para pegar a menor nota
    for i in range(qtdAlunos):
        if notas[i] == menorNota:
            print(dados[i])
            
# função que irá apresentar a média da turma:
def mediaTurma(qtdAlunos):
    nota = 0
    for i in range(qtdAlunos):
        nota += dados[i]['nota']
    media = (nota/qtdAlunos)
    print(f'A média da turma é: {media:,.2f}')

# funcao do menu:
def menu(csv):
    if csv != "csv":
        qtdAlunos = int(input('Digite a quantidade de alunos: '))
        while qtdAlunos <= 0:
            print('É necessário ter 1 ou mais estudantes! Tente novamente...')
            qtdAlunos = int(input('Digite a quantidade de alunos: '))
        gabarito = str(input('Digite o gabarito: '))
        while qtdAlunos == "":
            print('É necessário ter 1 ou mais questões! Tente novamente...')
            qtdAlunos = int(input('Digite a quantidade de alunos: '))
        infoalunos = infoAlunos(qtdAlunos, gabarito)
        loop = 1
        while loop == 1:
            print(txt.menu)
            opcao = int(input())
            print('\n')
            if opcao == 1:
                ordenarNome(qtdAlunos)
            if opcao == 2:
                ordenarNota(qtdAlunos)
            if opcao == 3:
                ordemMaior7(qtdAlunos)
            if opcao == 4:
                ordemMenor7(qtdAlunos)
            if opcao == 5:
                percentualAprovacao(qtdAlunos)
            if opcao == 6:
                maiorFrequencia(qtdAlunos)
            if opcao == 7:
                maiorNota(qtdAlunos)
            if opcao == 8:
                menorNota(qtdAlunos)
            if opcao == 9:
                mediaTurma(qtdAlunos)
            print('\n')
            print('Deseja voltar para o menu? Digite 1 para SIM e 0 para NÃO')
            loop = int(input())
            if loop == 1: os.system('cls')
            print('\n')
    else:
        qtdAlunos = int(input('Digite a quantidade de alunos: '))
        infoalunosCSV()
        gabarito = lt.gabarito
        loop = 1
        while loop == 1:
            print(txt.menu)
            opcao = int(input())
            print('\n')
            if opcao == 1:
                ordenarNome(qtdAlunos)
            if opcao == 2:
                ordenarNota(qtdAlunos)
            if opcao == 3:
                ordemMaior7(qtdAlunos)
            if opcao == 4:
                ordemMenor7(qtdAlunos)
            if opcao == 5:
                percentualAprovacao(qtdAlunos)
            if opcao == 6:
                maiorFrequencia(qtdAlunos)
            if opcao == 7:
                maiorNota(qtdAlunos)
            if opcao == 8:
                menorNota(qtdAlunos)
            if opcao == 9:
                mediaTurma(qtdAlunos)
            print('\n')
            print('Deseja voltar para o menu? Digite 1 para SIM e 0 para NÃO')
            loop = int(input())
            if loop == 1: os.system('cls')
            print('\n')