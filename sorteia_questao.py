import random
def sorteia_questao(dicionário,nível):
    for chaves in dicionário:
        if chaves==nível:
            x=len(dicionário[chaves])
            coloque=x-1
            i=random.randint(0,coloque)
            z=dicionário[chaves]
            return z[i]
