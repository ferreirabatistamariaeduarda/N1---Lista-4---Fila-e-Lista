class Item:
    def __init__(self, nome, telefone):
        self.dado = {'nome': nome, 'telefone': telefone}
        self.proximo = None
        self.anterior = None

class Lista:
    def __init__(self):
        self.cabeca = None
        self.calda = None
        self.tamanho = 0

    def is_empty(self):
        return self.cabeca is None

    def inserirInicio(self, nome, telefone):
        novo_item = Item(nome, telefone)
        if self.is_empty():
            self.cabeca = novo_item
            self.calda = novo_item
        else:
            novo_item.proximo = self.cabeca
            self.cabeca.anterior = novo_item
            self.cabeca = novo_item
        self.tamanho += 1

    def inserirFim(self, nome, telefone):
        novo_item = Item(nome, telefone)
        if self.is_empty():
            self.cabeca = novo_item
            self.calda = novo_item
        else:
            novo_item.anterior = self.calda
            self.calda.proximo = novo_item
            self.calda = novo_item
        self.tamanho += 1

    def remover(self):
        if self.is_empty():
            print('A lista está vazia')
        else:
            nome = input('Digite o nome da pessoa a ser removida: ')
            atual = self.cabeca
            while atual is not None:
                if atual.dado['nome'] == nome:
                    if atual.anterior is not None:
                        atual.anterior.proximo = atual.proximo
                    else:
                        self.cabeca = atual.proximo

                    if atual.proximo is not None:
                        atual.proximo.anterior = atual.anterior
                    else:
                        self.calda = atual.anterior

                    self.tamanho -= 1
                    print('Pessoa removida com sucesso.')
                    return

                atual = atual.proximo

            print(f'O nome "{nome}" não foi encontrado na agenda')

    def buscar(self):
        if self.is_empty():
            print('A lista está vazia')
        else:
            nome = input('Digite o nome da pessoa a ser buscada: ')
            atual = self.cabeca
            while atual is not None:
                if atual.dado['nome'] == nome:
                    print(f'Nome: {atual.dado["nome"]}, Telefone: {atual.dado["telefone"]}')
                    return

                atual = atual.proximo

            print(f'O nome "{nome}" não foi encontrado na agenda')

    def mostrar(self):
        if self.is_empty():
            print('A lista está vazia')
        else:
            atual = self.cabeca
            while atual is not None:
                print(f'Nome: {atual.dado["nome"]}, Telefone: {atual.dado["telefone"]}')
                atual = atual.proximo


def menu(opcao):
    lista = Lista()

    if opcao == 1:
        for _ in range(3):
            nome = input('Nome: ')
            numTel = input('Número de Telefone: ')
            lista.inserirInicio(nome, numTel)
            print('Dados inseridos com sucesso!')

    elif opcao == 2:
        lista.remover()

    elif opcao == 3:
        lista.buscar()

    elif opcao == 4:
        lista.mostrar()

while True:
    print('Escolha uma função digitando o número referente')

    print('1 - Inserir')
    print('2 - Remover')
    print('3 - Buscar')
    print('4 - Mostrar Agenda')
    print('5 - Sair')

    opcao = int(input('Digite um número referente a uma função: '))

    if opcao == 5:
        print('Você saiu!')
        break

    menu(opcao)
