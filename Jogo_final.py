import random

quest = [{'titulo': 'Qual o resultado da operação 57 + 32?',
          'nivel': 'facil',
          'opcoes': {'A': '-19', 'B': '85', 'C': '89', 'D': '99'},
          'correta': 'C'},
#12
          {'titulo': 'Qual o resultado da operação 0 - 10?',
          'nivel': 'facil',
          'opcoes': {'A': '5', 'B': '0', 'C': '-10', 'D': '10'},
          'correta': 'C'},

         {'titulo': 'Qual a capital do Brasil?',
          'nivel': 'facil',
          'opcoes': {'A': 'Brasília', 'B': 'Rio de janeiro', 'C': 'São Paulo', 'D': 'Osasco'},
          'correta': 'A'},

         {'titulo': 'Quando é o feriado da Independência do Brasil?',
          'nivel': 'facil',
          'opcoes': {'A': '21 de Abril', 'B': '12 de Outubro', 'C': '07 de Setembro', 'D': '15 de Novembro'},
          'correta': 'C'},

         {'titulo': '_________ é um conjunto de particularidades que caracterizam um grupo de pessoas, uma família ou uma sociedade. É formada por princípios morais, hábitos, costumes, histórias, manifestações religiosas, entre outros. Qual palavra melhor completa o início da frase?',
          'nivel': 'facil',
          'opcoes': {'A': 'Missão', 'B': 'Cultura', 'C': 'Curso superior', 'D': 'Culinária'},
          'correta': 'B'},

         {'titulo': 'Qual destes termos menos tem relação com o fenômeno da globalização?',
          'nivel': 'facil',
          'opcoes': {'A': 'Aculturação', 'B': 'Neoliberalismo', 'C': 'União Europeia', 'D': 'Caldeirão do Huck'},
          'correta': 'D'},

         {'titulo': 'Qual o feriado do aniversário da cidade de São Paulo?',
          'nivel': 'facil',
          'opcoes': {'A': '25 de Janeiro', 'B': '24 de Março', 'C': '9 de Julho', 'D': '12 de Novembro'},
          'correta': 'A'},
#11
          {'titulo': 'Quantas arestas tem um triângulo?',
          'nivel': 'facil',
          'opcoes': {'A': '3', 'B': '2', 'C': '4', 'D': '1'},
          'correta': 'A'},

         {'titulo': 'Qual destas não é uma fruta?',
          'nivel': 'facil',
          'opcoes': {'A': 'Laranja', 'B': 'Maça', 'C': 'Tomate', 'D': 'Abacate'},
          'correta': 'B'},
#18
          {'titulo': 'Qual destas não é ua marca de carro?',
          'nivel': 'facil',
          'opcoes': {'A': 'Ford', 'B': 'BMW', 'C': 'Skoda', 'D': 'Linxus'},
          'correta': 'D'},
#1
          {'titulo': 'Qual é a capital de Portugal?',
          'nivel': 'facil',
          'opcoes': {'A': 'Porto', 'B': 'Madrid', 'C': 'Lisboa', 'D': 'Roma'},
          'correta': 'C'},

          {'titulo': 'Qual é a capital da Espanha?',
          'nivel': 'facil',
          'opcoes': {'A': 'Lisboa', 'B': 'Madrid', 'C': 'Algarve', 'D': 'Maiorca'},
          'correta': 'B'},

         {'titulo': 'Em qual ano o TikTok atingiu 1 bilhão de usuários?',
          'nivel': 'facil',
          'opcoes': {'A': '2019', 'B': '2021', 'C': '2015', 'D': '2018'},
          'correta': 'B'},
         
         {'titulo': 'Qual destes não é um app com foco em streaming de vídeo?',
          'nivel': 'facil',
          'opcoes': {'A': 'Netflix', 'B': 'Disney Plus', 'C': 'TIDAL', 'D': 'HBO Max'},
          'correta': 'C'},
#7
          {'titulo': 'Qual a fórmula da substância água?',
          'nivel': 'facil',
          'opcoes': {'A': 'C02', 'B': 'H302', 'C': 'H20', 'D': 'H202'},
          'correta': 'C'},

         {'titulo': 'Qual destes parques não se localiza em São Paulo?!',
          'nivel': 'facil',
          'opcoes': {'A': 'Ibirapuera', 'B': 'Parque do Carmo', 'C': 'Parque Villa Lobos', 'D': 'Morro da Urca'},
          'correta': 'D'},

         {'titulo': 'Qual destas não é uma linguagem de programação?',
          'nivel': 'facil',
          'opcoes': {'A': 'Miratdes', 'B': 'Python', 'C': 'Lua', 'D': 'C++'},
          'correta': 'A'},

         {'titulo': 'Dentre os listados, qual destes esportes é menos praticado no Brasil?',
          'nivel': 'facil',
          'opcoes': {'A': 'Natação', 'B': 'Vôlei', 'C': 'Ski Cross Country', 'D': 'Futebol'},
          'correta': 'C'},
         
         {'titulo': 'Qual o resultado da operação 5 + 2 * 3?',
          'nivel': 'medio',
          'opcoes': {'A': '21', 'B': '11', 'C': '30', 'D': '10'},
          'correta': 'B'},
#19
          {'titulo': 'Qual o resultado da operação 7 + 2 * 3 + 3 * 2?',
          'nivel': 'medio',
          'opcoes': {'A': '21', 'B': '19', 'C': '22', 'D': '15'},
          'correta': 'B'},
#2
          {'titulo': 'Qual estrela pop americana teve sucesso consecutivo nas paradas de 2015 com os singles Sorry e Love Yourself?',
          'nivel': 'medio',
          'opcoes': {'A': 'Taylor Swift', 'B': 'Eminem', 'C': 'Justin Bieber', 'D': 'Katy Perry'},
          'correta': 'C'},

         {'titulo': 'Qual destas é uma pseudociência que estuda os corpos celestes e as prováveis relações que possuem com a vida das pessoas e os acontecimentos na Terra?',
          'nivel': 'medio',
          'opcoes': {'A': 'Astronomia', 'B': 'Física quântica', 'C': 'Astrologia', 'D': 'Computação'},
          'correta': 'C'},

         {'titulo': 'Qual destas não foi considerada em 2007 uma das sete maravilhas do mundo moderno?',
          'nivel': 'medio',
          'opcoes': {'A': 'Muralha da China', 'B': 'Machu Picchu', 'C': 'Cristo Redentor', 'D': 'Torre Eiffel'},
          'correta': 'D'},
#13
          {'titulo': 'Que dia comemora a ressureição de Jesus Cristo?',
          'nivel': 'medio',
          'opcoes': {'A': 'Quarta-Feira de Cinzas', 'B': 'Natal', 'C': 'Reveillon', 'D': 'Sexta-Feira Santa'},
          'correta': 'D'},

         {'titulo': 'Qual destas pessoas conduziu importantes estudos sobre radioatividade, sendo ganhadora de dois prêmios Nobel?',
          'nivel': 'medio',
          'opcoes': {'A': 'Marie Curie', 'B': 'Paul Erdős', 'C': 'Clive W.J. Granger', 'D': 'Maria Ressa'},
          'correta': 'A'},

         {'titulo': 'Quem é considerada a primeira pessoa programadora do mundo?!',
          'nivel': 'medio',
          'opcoes': {'A': 'Marie Curie', 'B': 'Alan Turing', 'C': 'Ada Lovelace', 'D': 'Edsger Dijkstra'},
          'correta': 'C'},

#9
         {'titulo': 'Qual o ano da independência do Brasil?',
          'nivel': 'medio',
          'opcoes': {'A': '1820', 'B': '1823', 'C': '1822', 'D': '1819'},
          'correta': 'C'},
#14
          {'titulo': 'Quantos estados tem o Brasil?',
          'nivel': 'medio',
          'opcoes': {'A': '24', 'B': '27', 'C': '23', 'D': '26'},
          'correta': 'D'}, 

         {'titulo': 'Qual destes números é primo?',
          'nivel': 'medio',
          'opcoes': {'A': '259', 'B': '85', 'C': '49', 'D': '19'},
          'correta': 'D'},
#10
          {'titulo': 'O que significa a sigla PT?',
          'nivel': 'medio',
          'opcoes': {'A': 'Partdio Trabalhista', 'B': 'Partido dos Trabalhadores', 'C': 'Partido do Trabalho', 'D': 'Partido da Tribuna'},
          'correta': 'B'},


         {'titulo': 'Na Conjectura de _______, escolhendo-se um número natural inicial n, onde n > 0, os seguintes critérios serão obedecidos: Se n for par o seu sucessor será a metade e se n for ímpar o seu sucessor será o triplo mais um, gerando então um novo número. Qual o nome da conjectura?',
          'nivel': 'medio',
          'opcoes': {'A': 'Collatz', 'B': 'Goldbach', 'C': 'Poincaré', 'D': 'Hodge'},
          'correta': 'A'},

         {'titulo': 'Como faço para chamar o SAMU?',
          'nivel': 'medio',
          'opcoes': {'A': 'Ligue 101', 'B': 'Ligue 192', 'C': 'Ligue 109', 'D': 'Ligue 122'},
          'correta': 'B'},
#16
          {'titulo': 'Qual o ano do golpe militar no Brasil?',
          'nivel': 'medio',
          'opcoes': {'A': '1964', 'B': '1959', 'C': '1962', 'D': '1963'},
          'correta': 'A'},
#6
          {'titulo': 'Como faço para chamar a POLÍCIA?',
          'nivel': 'medio',
          'opcoes': {'A': 'Ligue 190', 'B': 'Ligue 192', 'C': 'Ligue 109', 'D': 'Ligue 122'},
          'correta': 'A'},

         {'titulo': 'Qual a segunda pessoa mais seguida no Instagram?',
          'nivel': 'medio',
          'opcoes': {'A': 'Cristiano Ronaldo', 'B': 'Dwayne Johnson', 'C': 'Kim Kardashian', 'D': 'Kylie Jenner'},
          'correta': 'D'},

         {'titulo': 'Qual a pessoa mais seguida no Instagram?',
          'nivel': 'medio',
          'opcoes': {'A': 'Cristiano Ronaldo', 'B': 'Dwayne Johnson', 'C': 'Kim Kardashian', 'D': 'Lionel Messi'},
          'correta': 'A'},

         {'titulo': 'A reprodução dos seres vivos é um processo biológico através do qual os organismos geram descendência. Qual desta não é uma forma de reprodução assexuada?',
          'nivel': 'dificil',
          'opcoes': {'A': 'Autogamia', 'B': 'Esporulação', 'C': 'Partenogênese', 'D': 'Divisão binária'},
          'correta': 'A'},

         {'titulo': 'Qual o resultado da operação 5 + 2 * 3 ^ 2, onde ^ representa potenciação?',
          'nivel': 'dificil',
          'opcoes': {'A': '441', 'B': '86', 'C': 'Nenhuma das outras respostas', 'D': '23'},
          'correta': 'D'},

         {'titulo': 'Quem é Oxóssi?!',
          'nivel': 'dificil',
          'opcoes': {'A': 'Rede de mercados', 'B': 'Tipo de poema Dissílabo', 'C': 'Divindade das religiões africanas', 'D': 'Trapper brasileiro'},
          'correta': 'C'},

         {'titulo': 'Qual a altura do Cristo Redentor?',
          'nivel': 'dificil',
          'opcoes': {'A': 'entre 0 e 20 metros', 'B': 'Entre 21 e 40 metros', 'C': 'Entre 41 e 60 metros', 'D': 'Mais que 60 metros'},
          'correta': 'B'},

         {'titulo': 'Em que ano faleceu Charles Babbage?',
          'nivel': 'dificil',
          'opcoes': {'A': '2022', 'B': '1791', 'C': '1935', 'D': '1871'},
          'correta': 'A'},
#15
          {'titulo': 'A derivada da velocidade representa o quê?',
          'nivel': 'dificil',
          'opcoes': {'A': 'Aceleração', 'B': 'Espaço', 'C': 'Tempo', 'D': 'Tamanho'},
          'correta': 'A'},

         {'titulo': 'Einstein foi Nobel de física em qual ano?',
          'nivel': 'dificil',
          'opcoes': {'A': '1906', 'B': '1905', 'C': '1920', 'D': '1921'},
          'correta': 'D'},

         {'titulo': 'Qual o número atômico do nitrogênio?',
          'nivel': 'dificil',
          'opcoes': {'A': '9', 'B': '7', 'C': '6', 'D': '8'},
          'correta': 'B'},
#20
          {'titulo': 'Qual o número atômico do carbono?',
          'nivel': 'dificil',
          'opcoes': {'A': '5', 'B': '4', 'C': '6', 'D': '8'},
          'correta': 'C'},

         {'titulo': 'Qual o ponto de fusão do nitrogênio?',
          'nivel': 'dificil',
          'opcoes': {'A': '120º C', 'B': '15º C', 'C': '-210º C', 'D': '-180º C'},
          'correta': 'C'},

          {'titulo': 'Quantos gols Pelé fez oficialmente?',
          'nivel': 'dificil',
          'opcoes': {'A': '815', 'B': '762', 'C': '1100', 'D': '1057'},
          'correta': 'B'},
#17        
         {'titulo': 'Em que ano iniciou-se o Plano Real?',
          'nivel': 'dificil',
          'opcoes': {'A': '1993', 'B': '1994', 'C': '1992', 'D': '2000'},
          'correta': 'B'},

         {'titulo': 'O que é Necrose?',
          'nivel': 'dificil',
          'opcoes': {'A': 'Uma banda de Rock', 'B': 'Uma marca de luxo', 'C': 'Cidade Francesa', 'D': 'Morte de tecido orgânico'},
          'correta': 'D'},
#3
          {'titulo': 'Em que ano o Titanic afundou no Oceano Atlântico em 15 de abril, em sua viagem inaugural de Southampton?',
          'nivel': 'dificil',
          'opcoes': {'A': '1912', 'B': '1916', 'C': '1930', 'D': '1908'},
          'correta': 'A'},
#4
          {'titulo': 'Qual cantor liderou o grupo pop dos anos 1970, Showaddywaddy?',
          'nivel': 'dificil',
          'opcoes': {'A': 'Dave Bartram', 'B': 'Michael Jackson', 'C': 'Oliver Bartram', 'D': 'Brian May'},
          'correta': 'A'},
#5
          {'titulo': 'Quantos corações tem um polvo?',
          'nivel': 'dificil',
          'opcoes': {'A': '1', 'B': '2', 'C': '4', 'D': '3'},
          'correta': 'D'},
#8
          {'titulo': 'Qual o maior avião comercial do mundo?',
          'nivel': 'dificil',
          'opcoes': {'A': 'Airbus A320', 'B': 'Airbus A380', 'C': 'Boeing 767', 'D': 'Boeing 737'},
          'correta': 'B'}]


class ANSI():   
    def color_text(code): 
        return "\33[{code}m".format(code=code)

def transforma_base(quest):




    dicio_f = {}
    l_facil = []
    l_medio = []
    l_dificil = []


    if len(quest) == 0:
        return dicio_f 

    for questao in quest:
        for item in questao:
            if item == 'nivel':
                if questao[item] == 'facil':
                    l_facil.append(questao)
                elif questao[item] == 'medio':
                    l_medio.append(questao)
                else:
                    l_dificil.append(questao)

    dicio_f['facil'] = l_facil
    dicio_f['medio'] = l_medio
    dicio_f['dificil'] = l_dificil

    return dicio_f

dicio_f = transforma_base(quest)

def valida_questao(dicio):
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

def valida_questoes(lista_questoes):
    lista_resp=[]
    for dicio in lista_questoes:
        x=valida_questao(dicio)
        lista_resp.append(x)
    return lista_resp    
        

valida_f = valida_questoes(dicio_f['facil'])


valida_m = valida_questoes(dicio_f['medio'])

valida_d = valida_questoes(dicio_f['dificil'])

soma_f = 0
soma_m = 0
soma_d = 0

for perg in valida_f:
    tam = len(perg)
    soma_f = soma_f + tam

for perg in valida_m:
    tam = len(perg)
    soma_m = soma_m + tam

for perg in valida_d:
    tam = len(perg)
    soma_d = soma_d + tam
    
continuar2=True    

if (soma_f + soma_m + soma_d) == 0:
    while continuar2:

        c = 0
        lista_q = []
        premio = 0
        valores = [1000,5000,10000,30000,50000,100000,300000,500000,1000000]
        continuar=True
        pulos = 3
        ajudas = 2
        nível='facil'
        rodada=0
        repete_quest=0
        nao_sortear=0
        
        print()

        print("\033[1m" + (ANSI.color_text(95) + 'Olá! Você está na Fortuna DesSoft e terá a oportunidade de enriquecer!') + "\033[0m")

        print()

        nome = input(ANSI.color_text(39) + 'Qual seu nome? ')
        nome = nome.upper()

        print()
    

        input("\033[1m" + ((ANSI.color_text(39) + "Ok {0}, você tem direito a pular 3 vezes e 2 ajudas!\n").format(nome) + (ANSI.color_text(96) + "As opções de resposta são 'A', 'B', 'C', 'D', 'ajuda', 'pula' e 'parar'!")) + "\033[0m" + 
        "\n" + "\n" + (ANSI.color_text(39) + "Aperte ENTER para continuar..."))


        print((ANSI.color_text(39) + "O jogo ja vai começar! Lá vem a primeira questão!") + "\n"  + "\n" + (ANSI.color_text(39) + "Vamos começar com questões do nível FACIL!") + "\n") 
        input(ANSI.color_text(39) + "Aperte ENTER para continuar...")


        while continuar:
            

            if c >= 0 and c <= 2:
                nível = 'facil'
            elif c > 2 and c <=5:
                nível = 'medio'
            else:
                nível = 'dificil'

            

            
            def sorteia_questao(dicionário,nível):
    
                for chaves in dicionário:
                    if chaves==nível:
                        x=len(dicionário[chaves])
                        coloque=x-1
                        i=random.randint(0,coloque)
                        z=dicionário[chaves]
                        return z[i]

            def sorteia_questao_inedita(dicionário,nível,lista):
                dicionário=dicionário
                nível=nível
                continuar=True
                while continuar:
                    questao=sorteia_questao(dicionário,nível)
                    if questao not in lista:
                        
                        lista.append(questao)
                        continuar=False
                        return questao
            if pulos>=-1 and rodada==0 and ajudas>=-1 and repete_quest==0 and nao_sortear==0:
                questao = sorteia_questao_inedita(dicio_f,nível,lista_q)
                c = c + 1

            def questao_para_texto(questao,c):

                item = 0
                respostas = 0
                num = str(c)
                A = 0
                B = 0
                C = 0
                D = 0

                for item in questao:
                    if item == "titulo":
                        titulo = questao[item]
                    if item == 'opcoes':
                        respostas = questao[item]

                for letra in respostas:
                    if letra == "A":
                        A = respostas[letra]
                    elif letra == "B":
                        B = respostas[letra]
                    elif letra == "C":
                        C = respostas[letra]
                    elif letra == "D":
                        D = respostas[letra]
                    
                final1 = ("\n\n----------------------------------------" + "\n" + "\033[1m" + (ANSI.color_text(34) + "QUESTÃO {0}:") + "\033[0m" + '\n' + '\n' + (ANSI.color_text(39) + "{1}") + '\n' + '\n' + (ANSI.color_text(39) + "RESPOSTAS:\nA: {2}\nB: {3}\nC: {4}\nD: {5}")).format(num,titulo,A,B,C,D)

                return final1

            perg = questao_para_texto(questao,c)

            print(perg)

            resp = input((ANSI.color_text(39) + "\n" + "Qual sua resposta?! "))
            

            for item in questao:
                if item == "correta":
                    resp_correta = questao[item]
            letras = ['A','B','C','D']
            letras2 = []

            for letra in letras:
                if letra != resp_correta:
                    letras2.append(letra)        

            

            if resp == resp_correta:
                premio = valores[c-1]
                if pulos<0:
                    pulos=-1
                if ajudas<0:
                    ajudas=-1    
                rodada=0
                repete_quest=0
                nao_sortear=0    
                print()
                if c!=9:
                    print("\033[1m" + (ANSI.color_text(92) + "Você acertou! Seu prêmio atual é de R$ {0:.2f}".format(premio)) + "\033[0m" + "\n")
            
                if c==3:
                    print("\033[1m" + (ANSI.color_text(39)+ 'HEY! Você passou para o nível MEDIO!') + "\033[0m")
                    
                elif c==6:
                    print("\033[1m" + (ANSI.color_text(39)+ 'HEY! Você passou para o nível DIFICIL!') + "\033[0m")    
                 
                elif c==9:
                    print("\033[1m" + (ANSI.color_text(92) + "PARABÉNS, você zerou o jogo e ganhou um milhão de reais!") + "\033[0m")
                    continuar=False
                    continuar2=False
                if c!=9:    
                    input((ANSI.color_text(39) + "Aperte ENTER para continuar..."))    


           

            elif resp in letras2:
                
                print()
                print("\033[1m" + (ANSI.color_text(93) + "Que pena, você errou e vai sair sem nada :(") + "\033[0m")
                print()
                jogar_dnv = input((ANSI.color_text(39) + "Gostaria de jogar novamente [S/N]? "))
                if jogar_dnv == "S":
                    continuar = False
                else:
                    continuar = False
                    continuar2= False

            elif resp == 'pula':
                pulos = pulos - 1
                if pulos==0:
                    print((ANSI.color_text(39)) + "OK, pulando! ATENÇÃO: Você não tem mais direito a pulos!")
                    input((ANSI.color_text(39) + "Aperte ENTER para continuar..."))
                    repete_quest=0
                    rodada=0
                    nao_sortear=0
                    
                    c = c - 1
                elif pulos<0:
                    pulos=-2
                    #colocar cor vermelha
                    print("\033[1m" + (ANSI.color_text(91) + "Não deu! Você não tem mais direito a pulos!") + "\033[0m")
                    input((ANSI.color_text(39) + "Aperte ENTER para continuar..."))
                else:

                    print((ANSI.color_text(39) + "OK, pulando! Você ainda tem {0} pulos!".format(pulos)) + "\n")
                    input((ANSI.color_text(39) + "Aperte ENTER para continuar..."))
                    repete_quest=0
                    rodada=0
                    nao_sortear=0
        
                    c = c - 1
            elif resp=='ajuda':
                def gera_ajuda(questao):
                    questões=['A','B','C','D']
                    certa=questao["correta"]
                    questões_para_sortear=[]
                    questões_ja_sorteadas=[]

                    for valores in questões:
                        if valores!=certa:
                            questões_para_sortear.append(valores)

                    numero_questoes_sorteadas=random.randint(1,2)
                    if numero_questoes_sorteadas==1:
                        numero=random.randint(0,2)
                        questao_sorteada=questões_para_sortear[numero]
                        Errada= questao['opcoes'][questao_sorteada]
                        resp="DICA:"+"\n"+'Opções certamente erradas: '+ Errada
                        return resp
                    else:
                        while len(questões_ja_sorteadas)<2:
                            numero=random.randint(0,2)
                            questao_sorteada=questões_para_sortear[numero]
                            if questao_sorteada not in questões_ja_sorteadas:
                                questões_ja_sorteadas.append(questao_sorteada)
                        Errada=questao['opcoes'][questões_ja_sorteadas[0]]
                        Errada1=questao['opcoes'][questões_ja_sorteadas[1]]        
                        resp="DICA:"+"\n"+'Opções certamente erradas: '+ Errada +' | '+ Errada1
                        return resp
                ajudas= ajudas - 1
                ajuda_quest=gera_ajuda(questao)
                
                if rodada==0 and ajudas>0:
                    print((ANSI.color_text(39) + 'Ok, lá vem ajuda! Você ainda tem {0} ajudas!'.format(ajudas)) + '\n')
                    input((ANSI.color_text(39) + "Aperte ENTER para continuar..."))
                    #colocar verde
                    print("\033[1m" + (ANSI.color_text(92) + ajuda_quest) + "\033[0m"+'\n')
                    input((ANSI.color_text(39) + "Aperte ENTER para continuar..."))
                    rodada=1
                elif rodada==1:
                    #colocar vermelho
                    print((ANSI.color_text(91) + 'Não deu! Você já pediu ajuda nessa questão!'))
                    input((ANSI.color_text(39) + "Aperte ENTER para continuar..."))
                    ajudas= ajudas + 1
                elif ajudas==0:
                    print((ANSI.color_text(39)+ 'Ok, lá vem ajuda! ATENÇÃO: Você não tem mais direito a ajudas!')+'\n')
                    input((ANSI.color_text(39) + "Aperte ENTER para continuar..."))
                    #colocar verde
                    print("\033[1m" + (ANSI.color_text(92) + ajuda_quest) + "\033[0m"+'\n')
                    input((ANSI.color_text(39) + "Aperte ENTER para continuar..."))
                    rodada=1
                elif ajudas<0:
                    ajudas=-2
                    #colocar vermelho
                    print((ANSI.color_text(91)+ 'Não deu! Você não tem mais direito a ajuda!'))
                    input((ANSI.color_text(39) + "Aperte ENTER para continuar..."))
            elif resp=='parar':
                pare=True
                while pare: 
                    print()
                    sim = "S"
                    parar = input((ANSI.color_text(39) + "Deseja mesmo parar [S/N]?? Caso responda {0}, sairá com R$ {1:.2f}! ").format(sim,premio))
                    if parar=='S':
                        print((ANSI.color_text(39)+ 'Ok!, Você parou e seu prêmio é de R$ {0:.2f} '.format(premio)))
                        print()
                        jogar_dnv = input((ANSI.color_text(39) + "Gostaria de jogar novamente [S/N]? "))
                        if jogar_dnv == "S":
                            continuar= False
                        else:
                            continuar= False
                            continuar2=False
                        pare=False
                    elif parar=='N':
                        repete_quest=1
                        pare=False
                    else:
                        #colocar em vermelho
                        print("\033[1m" + (ANSI.color_text(91)+ 'Opção inválida!') + "\033[0m")    
            elif resp!='A' or resp!='B' or resp!='C' or resp!='D' or resp!='ajuda' or resp!='pula' or resp!='parar':
                #colocar em vermelho
                print("\033[1m" + (ANSI.color_text(91)+ 'Opção inválida!') + "\033[0m")
                print("\033[1m" + (ANSI.color_text(96) + "As opções de resposta são 'A', 'B', 'C', 'D', 'ajuda', 'pula' e 'parar'!") + "\033[0m"+ '\n')
                input((ANSI.color_text(39) + "Aperte ENTER para continuar..."))
                nao_sortear=1
                
else:
    print(ANSI.color_text(91) + "A base de dados NÃO está consistente!")
                
