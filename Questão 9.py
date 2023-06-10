#Um banco precisa armazenar as informações dos clientes em uma lista encadeada simples. 
#Cada cliente possui nome, número da conta e saldo. 
#Implemente as operações de inserir, remover e pesquisar um cliente na lista. 
#A cada operações, mostrar a lista em “formado de tabela”.

class Item:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None

class Lista:
    def __init__(self):
        self.cabeca = None
        self.tamanho = 0
    
    def is_empty(self):
        return self.cabeca is None
        
    def inserirInicio(self, valor):
        novo_item = Item(valor)
        novo_item.proximo = self.cabeca
        self.cabeca = novo_item
        self.tamanho += 1
        
    def inserirFim(self, valor):
        novo_item = Item(valor)
        if self.is_empty():
            self.cabeca = novo_item
        else:
            atual = self.cabeca
            while atual.proximo is not None:
                atual = atual.proximo
            atual.proximo = novo_item
        self.tamanho += 1
        
    def removerInicio(self):
        if self.is_empty():
            print('A lista está vazia!')
        else:
            self.cabeca = self.cabeca.proximo
            self.tamanho -= 1

    def removerFim(self):
        if self.is_empty():
            print('A lista está vazia!')
        elif self.cabeca.proximo is None:
            self.cabeca = None
            self.tamanho -= 1
        else:
            atual = self.cabeca
            anterior = None
            while atual.proximo is not None:
                anterior = atual
                atual = atual.proximo
            anterior.proximo = None
            self.tamanho -= 1

    def pesquisar(self, dado):
        if self.is_empty():
            print('A lista está vazia!')
        else:
            atual = self.cabeca
            while atual is not None:
                if atual.dado['numConta'] == dado:
                    return atual.dado
                atual = atual.proximo
            return None

    def mostrar(self):
        if self.is_empty():
            print('A lista está vazia!')
        else:
            print('Nome\t\tNúmero da Conta\tSaldo')
            atual = self.cabeca
            while atual is not None:
                cliente = atual.dado
                print(f"{cliente['nome']}\t{cliente['numConta']}\t\t{cliente['saldo']}")
                atual = atual.proximo
            
def clientes():
    lista = Lista()
    
    while True:
        print('Escolha uma função digitando o número referente')
        print('1 - Inserir Dados')
        print('2 - Remover')
        print('3 - Tamanho')
        print('4 - Mostrar')
        print('5 - Sair')
       
        opcao = input('Digite um número referente a uma função: ')
        
        if not opcao.isdigit():
            print('Opção inválida. Digite um número.')
            continue
        
        opcao = int(opcao)
       
        if opcao == 5:
            print('Você saiu!')
            break
        
        if opcao == 1:
            nome = input('Nome: ')
            numConta = input('Número da conta: ')
            saldo = float(input('Saldo: '))
            cliente = {
                'nome': nome,
                'numConta': numConta,
                'saldo': saldo
            }
            lista.inserirInicio(cliente)
            
            print('As informações foram adicionadas!')
            lista.mostrar()
        
        elif opcao == 2:
            dadoRemover = input('Digite o número da conta do cliente a ser removido: ')
            cliente = lista.pesquisar(dadoRemover)
            if cliente is not None:
                lista.removerInicio()
                print('Cliente removido com sucesso!')
            else:
                print('Cliente não encontrado na lista.')
        
        elif opcao == 3:
            print(f'O tamanho da lista é {lista.tamanho}')
        
        elif opcao == 4:
            lista.mostrar()

clientes()
