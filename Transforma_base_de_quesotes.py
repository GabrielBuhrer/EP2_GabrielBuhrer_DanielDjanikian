def transforma_base(lista):
    facil=[]
    medio=[]
    dificil=[]        

    for dicionarios in lista:
        dificulade = dicionarios['nivel']
        if dificulade=='facil':
            facil.append(dicionarios)
        elif dificulade=='medio':
            medio.append(dicionarios)
        else:
            dificil.append(dicionarios)
    dici_resp={}
    if lista!=[]:
        if facil!=[]:
            dici_resp['facil']=facil
        if medio!=[]:    
            dici_resp['medio']=medio
        if dificil!=[]:    
            dici_resp['dificil']=dificil
        return dici_resp
    else:
        return dici_resp        
    
    