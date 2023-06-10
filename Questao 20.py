#Escreva uma função que receba uma lista de dicionários, onde cada dicionário representa um aluno com as 
#chaves "nome" e "nota". A função deve retornar o nome do aluno com a maior nota.

def dicionario():
    lista = []
    for i in range(2):
        nome = input(f"Digite o nome do aluno {i+1}: ")
        nota = float(input(f"Digite a nota do aluno {i+1}: "))
        lista.append({"nome": nome, "nota": nota})

    maiorNota = 0
    alunoMaiorNota = ""

    for aluno in lista:
        nota = aluno["nota"]
        if nota > maiorNota:
            maiorNota = nota
            alunoMaiorNota = aluno["nome"]

    return alunoMaiorNota



aluno = dicionario()
print("Aluno com maior nota:", aluno)
