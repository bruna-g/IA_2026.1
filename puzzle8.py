from collections import deque

def BFS(problema):
    if paridade(problema.est_inicial) > 0:
        return False
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
    if paridade(problema.est_inicial) > 0:
        return False
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
            print(f"Passo {no_imprimir.profund}: Ação '{no_imprimir.acao}' -> Estado: {no_imprimir.est_atual} -> Profundidade: {no_imprimir.profund}")
        else:
            print(f"Passo 0: Estado Inicial -> Estado: {no_imprimir.est_atual}")
    
    print(f"\nSolução encontrada em {child.profund} movimentos.")

    
def main():
    # result_bfs, nos_visitados_bfs = BFS(Problem("132045768"))
    # if result_bfs == False:
    #     print("Não há solução em BFS.")
    # else:
    #     reconstruir_cam(result_bfs)
    #     print(f"Número de nós visitados: {nos_visitados_bfs}")

    result_dfs, nos_visitados_dfs = DFS(Problem("132045768"))
    if result_dfs == False:
        print("Não há solução em DFS.")
    else:
        reconstruir_cam(result_dfs)
        print(f"Número de nós visitados: {nos_visitados_dfs}")
    

main()