class ANSI():   
    def color_text(code): 
        return "\33[{code}m".format(code=code) 
  
print()

print((ANSI.color_text(95) + 'Olá! Você está na Fortuna DesSoft e terá a oportunidade de enriquecer!'))

print()

nome = input(ANSI.color_text(39) + 'Qual seu nome? ')

print()

print(input(ANSI.color_text(39) + "Ok {0}, você tem direito a pular 3 vezes e 2 ajudas!\n".format(nome) + (ANSI.color_text(96) + "As opções de resposta são 'A', 'B', 'C', 'D', 'ajuda', 'pula' e 'parar'!") + 
"\n" + "\n" + (ANSI.color_text(39) + "Aperte ENTER para continuar...")))


print((ANSI.color_text(39) + "O jogo ja vai começar! Lá vem a primeira questão!") + "\n"  + "\n" + (ANSI.color_text(39) + "Vamos começar com questões do nível FÁCIL!") + "\n" + 
(ANSI.color_text(39) + "Aperte ENTER para continuar..."))

print()
print()

print((ANSI.color_text(39) + "-----------------------"))

n_questao = 1

print()

print((ANSI.color_text(34) + "QUESTÃO" + ' ' + "{0}".format(n_questao)))

print()

resp = input((ANSI.color_text(39) + "Qual sua resposta?! "))

print((ANSI.color_text(91) + "Opção inválida!") + "\n" +
(ANSI.color_text(96) + "As opções de resposta são 'A', 'B', 'C', 'D', 'ajuda', 'pula' e 'parar'!"))

print()

resp = input((ANSI.color_text(39) + "Qual sua resposta?! "))

ajudas = 0

print((ANSI.color_text(39) + "OK, lá vem ajuda! Você ainda tem {0} ajudas!".format(ajudas)) + "\n" + (ANSI.color_text(39) + "Aperte ENTER para continuar..."))

ops_erradas = 0

print((ANSI.color_text(92) + "DICA:") + "\n" + (ANSI.color_text(92) + "Opções certamente erradas: {0}".format(ops_erradas)) + 
"\n" + (ANSI.color_text(39) + "Aperte ENTER para continuar..."))

print((ANSI.color_text(91) + "Não deu! Você já pediu ajuda nesta questão!") + 
"\n" + (ANSI.color_text(39) + "Aperte ENTER para continuar..."))

print((ANSI.color_text(39) + "OK, lá vem ajuda! ATENÇÃO: Você não tem mais direito a ajudas!") + "\n" + "\n" +  (ANSI.color_text(39) + "Aperte ENTER para continuar..."))

pulos = 0

print((ANSI.color_text(39) + "OK, pulando! Você ainda tem {0} pulos!".format(pulos)) + "\n" + (ANSI.color_text(39) + "Aperte ENTER para continuar..."))

print()

print((ANSI.color_text(39) + "OK, pulando! ATENÇÃO: Você não tem mais direito a pulos!") + "\n" + (ANSI.color_text(39) + "Aperte ENTER para continuar..."))

print()

print((ANSI.color_text(91) + "Não deu! Você não tem mais direito a pulos!") + "\n" + (ANSI.color_text(39) + "Aperte ENTER para continuar..."))

print()

premio = 0

sim = "S"

parar = input((ANSI.color_text(39) + "Deseja mesmo parar [S/N]?? Caso responda {0}, sairá com R$ {1}").format(sim,premio))

print((ANSI.color_text(91) + "Opção inválida!"))


print(ANSI.color_text(39) + "Ok! Você parou e seu prêmio é de R$ {0}".format(premio))

print()

print((ANSI.color_text(92) + "Você acertou! Seu prêmio atual é de R$ {0}".format(premio)) + "\n" + (ANSI.color_text(39) + "Aperte ENTER para continuar..."))

print()

nivel = 'MÉDIO'

print((ANSI.color_text(92) + "Você acertou! Seu prêmio atual é de R$ {0}".format(premio)) + "\n" + "\n" + (ANSI.color_text(93) + "HEY! Você passou para o nível {0}".format(nivel)) + "\n" + (ANSI.color_text(39) + "Aperte ENTER para continuar..."))

print()

print((ANSI.color_text(93) + "Que pena, você errou e vai sair sem nada :("))

print()

print((ANSI.color_text(92) + "PARABÉNS, você zerou o jogo e ganhou um milhão de reais!"))









