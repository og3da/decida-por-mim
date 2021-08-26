import random
stop=1

#lista de respostas aleatórias
respostas = [
        "acho que deveria",
        "nao faz isso",
        "agora ferrou",
        "é o caminho certo",
        "isso seria burro...",
        "vai com tudo",
        "em nenhuma hipótese",
        "com certeza",
        "sijoga",
        "faz nem"
        #'cara,pensa nisso'
    ]

#executar programa=1 ou adicionar resposta para a lista=2
executar=int(input("Digite 1 para adicionar uma resposta para a lista de respostas ou 2 para executar o programa: "))
if executar==1:
    adicionarResposta=str(input("Digite a resposta: "))
    respostas.append(adicionarResposta)

elif executar==2:
    while (stop==1):
        input("Faça uma pergunta qualquer: ")
        print(random.choice(respostas))
        stop=int(input("Digite 1 para continuar ou 2 para encerrar: "))

else:
    print("Digite apenas a opção 1 ou 2!")