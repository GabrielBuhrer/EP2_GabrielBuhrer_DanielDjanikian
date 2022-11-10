import random
def gera_ajuda(questao):
    questões=['A','B','C','D']
    certa=questao["correta"]
    questões_para_sortear=[]
    questões_ja_sorteadas=[]

    for valores in questões:
        if valores!=certa:
            questões_para_sortear.append(valores)

    #numero_questoes_sorteadas=random.randint(1,2)
    numero_questoes_sorteadas=1
    if numero_questoes_sorteadas==1:
        numero=random.randint(0,2)
        questao_sorteada=questões_para_sortear[numero]
        Errada= questao['opcoes'][questao_sorteada]
        resp="DICA:"+"\n"+'Opções certamente erradas: '+ Errada
        return resp
    else:
        while len(questões_ja_sorteadas)<=2:
            numero=random.randint(0,2)
            questao_sorteada=questões_para_sortear[numero]
            if questao_sorteada not in questões_ja_sorteadas:
                questões_ja_sorteadas.append(questao_sorteada)
        Errada=questao['opcoes'][questões_ja_sorteadas][0]
        Errada1=questao['opcoes'][questões_ja_sorteadas][1]        
        resp="DICA:"+"\n"+'Opções certamente erradas: '+ Errada + Errada1
        return resp         
                
                


