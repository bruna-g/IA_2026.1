string = "123450678"
# pos = string.find('4')
# new = string[:pos] + '5' + '4' + string[pos+2:]
# print(new)

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

pos = string.find('0')
aux = string[pos+3]
est_atual_mod = string[:pos] + aux + string[pos+1:pos+3] + '0' + string[pos+4:]
print(est_atual_mod)

acoes = acoes_possiveis(string)
print(acoes)

