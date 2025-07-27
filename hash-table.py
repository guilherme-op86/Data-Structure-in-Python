class Node:
    def __init__(self, sigla, nomeEstado):
        self.sigla = sigla
        self.nomeEstado = nomeEstado
        self.proximo = None

class LinkedList:
    def __init__(self):
        self.head = None

    def inserirDados(self, sigla, nomeEstado):
        novo_node = Node(sigla, nomeEstado)
        if(self.head == None):
            self.head = novo_node
            return
        else:
            novo_node.proximo = self.head
            self.head = novo_node
            return

    def imprimirDados(self):
        node_atual = self.head
        while(node_atual != None):
            print(f'{node_atual.sigla}: {node_atual.nomeEstado}', end= ' -> ')
            node_atual = node_atual.proximo
        print(None)

class TabelaHash:
    def __init__(self):
        self.tamanho = 10
        self.bucket = [LinkedList() for i in range(0, self.tamanho)]

    def funcaoHash(self, k):
        k = list(k)
        return (ord(k[0]) + ord(k[1])) % self.tamanho

    def verificarIndice(self, sigla):
        if(sigla == 'DF'):
            print('A sigla DF deve ser inserida no índice 7 da tabela')
        else:
            pos = self.funcaoHash(sigla)
            print(f'A sigla {sigla} deve ser inserida no indice {pos} da tabela')

    def buscarSigla(self, sigla):
        if (sigla == 'DF'):
            print(f'O estado do DF está no indíce 7 da da tabela')
            return
        else:
            pos = self.funcaoHash(sigla)
            node_atual = self.bucket[pos].head
            while (node_atual != None):
                if (node_atual.sigla == sigla):
                    print(f'O estado de {sigla} está no índice {pos} da tabela')
                    return
                node_atual = node_atual.proximo
                print(f'O estado de {sigla} não consta na tabela')

    def inserir(self, sigla, nomeEstado):
        if(sigla == 'DF'):
            self.bucket[7].inserirDados(sigla, nomeEstado)
        else:
            pos = self.funcaoHash(sigla)
            self.bucket[pos].inserirDados(sigla, nomeEstado)

    def imprimir(self):
        for i in range(0, self.tamanho):
            print(f'{i}-', end= ' ')
            self.bucket[i].imprimirDados()



tabela = TabelaHash()
'''tabela.inserir("AC", "Acre")
tabela.inserir("AL", "Alagoas")
tabela.inserir("AP", "Amapá")
tabela.inserir("AM", "Amazonas")
tabela.inserir("BA", "Bahia")
tabela.inserir("CE", "Ceará")
tabela.inserir("DF", "Distrito Federal")
tabela.inserir("ES", "Espírito Santo")
tabela.inserir("GO", "Goiás")
tabela.inserir("MA", "Maranhão")
tabela.inserir("MT", "Mato Grosso")
tabela.inserir("MS", "Mato Grosso do Sul")
tabela.inserir("MG", "Minas Gerais")
tabela.inserir("PA", "Pará")
tabela.inserir("PB", "Paraíba")
tabela.inserir("PR", "Paraná")
tabela.inserir("PE", "Pernambuco")
tabela.inserir("PI", "Piauí")
tabela.inserir("RJ", "Rio de Janeiro")
tabela.inserir("RN", "Rio Grande do Norte")
tabela.inserir("RS", "Rio Grande do Sul")
tabela.inserir("RO", "Rondônia")
tabela.inserir("RR", "Roraima")
tabela.inserir("SC", "Santa Catarina")
tabela.inserir("SP", "São Paulo")
tabela.inserir("SE", "Sergipe")
tabela.inserir("TO", "Tocantins")
tabela.inserir("GP", "Guilherme Oliveira de Paula")'''

tabela.verificarIndice("DF")

