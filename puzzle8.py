from collections import deque
import sys

def BFS(problema):
    node = Node(problema.est_inicial, 'pai', None, 0)
    if verifica_est_objetivo(problema.est_inicial):
        return node
    fronteira = deque()
    fronteira.append(node)
    alcancados = set()
    alcancados.add(problema.est_inicial)
    nos_expandidos = 0
    while fronteira:
        node = fronteira.popleft()
        nos_expandidos += 1
        for child in expand(node):
            s = child.est_atual
            if verifica_est_objetivo(s):
                return child, nos_expandidos
            if s not in alcancados:
                alcancados.add(s)
                fronteira.append(child)
    return False, nos_expandidos

def DFS(problema):
    node = Node(problema.est_inicial, 'pai', None, 0)
    if verifica_est_objetivo(problema.est_inicial):
        return node
    fronteira = []
    fronteira.append(node)
    alcancados = set()
    alcancados.add(problema.est_inicial)
    nos_expandidos = 0
    while fronteira:
        node = fronteira.pop()
        nos_expandidos += 1
        for child in expand(node):
            s = child.est_atual
            if verifica_est_objetivo(s):
                return child, nos_expandidos
            if s not in alcancados:
                alcancados.add(s)
                fronteira.append(child)
    return False, nos_expandidos

class Node:
    def __init__(self, est_atual, node_pai, acao, profund):
        self.est_atual = est_atual
        self.node_pai = node_pai
        self.acao = acao
        self.profund = profund

class Problem:
    def __init__(self, est_inicial):
        self.est_inicial = est_inicial

def verifica_est_objetivo(est):
    if est == "123456780":
        return True
    else:
        return False
    
def expand(node):
    s = node.est_atual
    acoes = acoes_possiveis(s)
    for acao in acoes:
        s_linha = aplicar_acao(acao, node.est_atual)
        yield Node(s_linha, node, acao, node.profund + 1)
    
def acoes_possiveis(est_atual):
    pos = est_atual.find('0')
    acoes = [['dir','baixo'], 
            ['esq', 'dir', 'baixo'],
            ['esq', 'baixo'],
            ['dir', 'cima', 'baixo'],
            ['esq', 'dir', 'cima', 'baixo'],
            ['esq', 'cima', 'baixo'],
            ['dir', 'cima',],
            ['esq', 'dir', 'cima'],
            ['esq', 'cima']]
    return acoes[pos]

def aplicar_acao(acao, est_atual):
    pos = est_atual.find('0')
    if acao == 'esq':
        aux = est_atual[pos-1]
        est_atual_mod = est_atual[:pos-1] + '0' + aux + est_atual[pos+1:]
        return est_atual_mod
    
    elif acao == 'dir':
        aux = est_atual[pos+1]
        est_atual_mod = est_atual[:pos] + aux + '0' + est_atual[pos+2:]
        return est_atual_mod
    
    elif acao == 'cima':
        aux = est_atual[pos-3]
        est_atual_mod = est_atual[:pos-3] + '0' + est_atual[pos-2:pos] + aux + est_atual[pos+1:]
        return est_atual_mod
    
    elif acao == 'baixo':
        aux = est_atual[pos+3]
        est_atual_mod = est_atual[:pos] + aux + est_atual[pos+1:pos+3] + '0' + est_atual[pos+4:]
        return est_atual_mod
    
def paridade(estado: str) -> int:
    arr = [c for c in estado if c != '0']
    inversoes = 0

    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                inversoes += 1

    return inversoes % 2  # 0 = par, 1 = ímpar

def reconstruir_cam(child):
    caminho = []
    node_atual = child
    
    while node_atual.node_pai != 'pai':
        caminho.append(node_atual)
        node_atual = node_atual.node_pai

    caminho.append(node_atual)

    while caminho:
        no_imprimir = caminho.pop()
        if no_imprimir.acao:
            print(f"Passo {no_imprimir.profund}: Ação '{no_imprimir.acao}' -> Estado: {no_imprimir.est_atual} -> Profundidade: {no_imprimir.profund} -> Pai: {no_imprimir.node_pai.est_atual}")
        else:
            print(f"Passo 0: Estado Inicial -> {no_imprimir.est_atual}")
    
    print(f"\nSolução encontrada em {child.profund} movimentos.")

    
def main():
    if len(sys.argv) != 3:
        print("Uso: python puzzle8.py <algoritmo> <estado_inicial>")
        print("Exemplo: python puzzle8.py BFS 123406758")
        return

    algoritmo = sys.argv[1].upper()
    estado_inicial = sys.argv[2]

    if len(estado_inicial) != 9 or not estado_inicial.isdigit():
        print("Erro: O estado inicial deve ser uma string de 9 dígitos.")
        return
    
    if paridade(estado_inicial) > 0:
        print("A paridade inicial é ímpar, não há solução.")
        return

    if algoritmo == "BFS":
        print("######### Busca em Largura (BFS) #########")
        result, nos_visitados = BFS(Problem(estado_inicial))
        if not result:
            print("Não há solução para este estado inicial.")
        else:
            reconstruir_cam(result)
            print(f"Número de nós expandidos: {nos_visitados}\n")
    elif algoritmo == "DFS":
        print("######### Busca em Profundidade (DFS) #########")
        result, nos_visitados = DFS(Problem(estado_inicial))
        if not result:
            print("Não há solução para este estado inicial.")
        else:
            reconstruir_cam(result)
            print(f"Número de nós expandidos: {nos_visitados}")
    else:
        print(f"Erro: Algoritmo '{sys.argv[1]}' não reconhecido. Use BFS ou DFS.")
    

main()