def valida_questao(dicio):
    print(dicio)
    niveis=['facil','medio','dificil']
    opcoes_certas=['A','B','C','D']
    dicio_resp={}
    dici_opc={}
    o1=0
    t=0
    titulo_vazio=0
    n=0
    o=0
    ch=0
    q=0
    n1=0
    A=0
    B=0
    C=0
    D=0
    q_opc=0
    a = 0
    b = 0
    c = 0
    d = 0  
    for chaves in dicio:
        if chaves=='titulo':
            t=t+1
            
            if dicio[chaves].strip()=='':
                titulo_vazio=1


        elif chaves=='nivel':
            n=n+1
            
            if dicio[chaves] not in niveis:
                n1=1
        elif chaves=='opcoes':
            o=o+1
            
            for chave in dicio['opcoes']:
                
                z=dicio['opcoes']
                if chave=='A':
                    x=z[chave]
                    x=x.strip()
                    
                    a=1
                    if x=='':
                        A=1
                if chave=='B':
                    x=z[chave]
                    x=x.strip()
                    b=1
                    if x=='':
                        B=1
                if chave=='C':
                    x=z[chave]
                    x=x.strip()
                    c=1
                    if x=='':
                        C=1
                if chave=='D':
                    x=z[chave]
                    x=x.strip()
                    d=1
                    if x=='':
                        D=1
                q_opc=q_opc+1        

                                

                        
        elif chaves=='correta':
            ch=ch+1
             
            
            if dicio[chaves] not in opcoes_certas:
                o1=1
        q=q+1        
    print(A)
    print(B)
    print(C)
    print(D)
    print(q_opc)
    if t==0:
        dicio_resp['titulo']='nao_encontrado'
    if q!=4:
        dicio_resp['outro']='numero_chaves_invalido'
    if titulo_vazio!=0:
        dicio_resp['titulo']='vazio'
    if n==0:
        dicio_resp['nivel']='nao_encontrado'
    if n1!=0:
        dicio_resp['nivel']='valor_errado'
    if o==0:
        dicio_resp['opcoes']='nao_encontrado'
    if q_opc!=4 and o!=0:
        dicio_resp['opcoes']='tamanho_invalido'
    if a==0 or b==0 or c==0 or d==0:
        if q_opc==4:
            dicio_resp['opcoes']='chave_invalida_ou_nao_encontrada'
    if A==1:
        dici_opc['A']='vazia'
        dicio_resp['opcoes']=dici_opc
    if B==1:
        dici_opc['B']='vazia'
        dicio_resp['opcoes']=dici_opc
    if C==1:
        dici_opc['C']='vazia'
        dicio_resp['opcoes']=dici_opc
    if D==1:
        dici_opc['D']='vazia'
        dicio_resp['opcoes']=dici_opc
    if ch==0:
        dicio_resp['correta']='nao_encontrado'
    if o1!=0:
        dicio_resp['correta']='valor_errado'
      
    return dicio_resp