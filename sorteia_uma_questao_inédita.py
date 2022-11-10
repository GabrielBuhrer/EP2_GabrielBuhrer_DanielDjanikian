import random
def sorteia_questao(dicionário,nível):
   
    for chaves in dicionário:
        if chaves==nível:
            x=len(dicionário[chaves])
            coloque=x-1
            i=random.randint(0,coloque)
            z=dicionário[chaves]
            return z[i]
def sorteia_questao_inedita(dicionário,nível,lista):
    continuar=True
    while continuar:
        questao=sorteia_questao(dicionário,nível)
        if questao not in lista:
            
            lista.append(questao)
            continuar=False
            return questao