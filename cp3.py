#Funcionalidades: - Adicionar transações (receitas e despesas) - Visualizar o saldo atual - Gerar um relatório de transações - Categorizar transações

#Estruturas de Dados: Utilize listas para armazenar as transações, onde cada transação é
#um dicionário contendo tipo (receita ou despesa), valor, categoria, e data.
#Dicionários podem ser usados para categorizar as transações e calcular totais por categoria.

from datetime import datetime

# Obtendo a data e hora atuais
agora = datetime.now()
data = agora.strftime("%d/%m/%Y %H:%M:%S")
transacoes = []

def inicio():
    opcao = input("\nBEM-VINDO! \n1 - Adicionar Transação\n2 - Carregar Dados\nO que você deseja?: ")

    while opcao.isnumeric() == False or (opcao != "1" and opcao != "2"):
        opcao = input("\nOpção inválida, por favor, escolha entre as seguintes opções\n1 - Adicionar Transação\n2 - Carregar Dados\n3 - Encerrar Programa\nO que você deseja?: ")
       

    if opcao == "1":
        adicionar_transacao(transacoes)
    elif opcao == "2":
        carregar_dados()
    elif opcao == "3":
        encerrar()    


def menu_principal():
    opcao = input("\nBEM-VINDO! \n1 - Adicionar Transação\n2 - Remover Transação\n3 - Visualizar Relatório\n4 - Obter Insights\n5 - Salvar Dados\n6 - Carregar Dados\n7 - Encerrar Programa\n\nO que você deseja?: ")

    while opcao.isnumeric() == False or (opcao != "1" and opcao != "2" and opcao != "3" and opcao != "4" and opcao != "5" and opcao != "6" and opcao != "7"):
        opcao = input("\nOpção inválida, por favor, escolha entre as seguintes opções\n1 - Adicionar Transação\n2 - Remover Transação\n3 - Visualizar Relatório\n4 - Obter Insights\n5 - Salvar Dados\n6 - Carregar Dados\n7 - Encerrar Programa\n\nO que você deseja?: ")

    if opcao == "1":
        adicionar_transacao(transacoes)
    elif opcao == "2":
        remover_transacao(transacoes)
    elif opcao == "3":
        visualizar_relatorio(transacoes)
    elif opcao == "4":
        obter_insights(transacoes)
    elif opcao == "5":
        salvar_dados()
    elif opcao == "6":
        carregar_dados()
    elif opcao == "7":
        encerrar()                            


def adicionar_transacao(transacoes):
    while not transacoes:
        
        Perg_Valor_Inicial = input("\nDeseja começar com um valor inicial na sua conta?\n1 - Sim\n2 - Não\nO que deseja?: ")
        
        while Perg_Valor_Inicial.isnumeric() == False or (Perg_Valor_Inicial != "1" and Perg_Valor_Inicial != "2"):
            Perg_Valor_Inicial = input("Opção inválida, por favor, escolha entre as seguintes opções\n1 - Sim\n2 - Não\nO que você deseja?: ")

        if Perg_Valor_Inicial == "1":
            Valor_Inicial = float(input("\nQual seria o valor inicial?: "))

            while Valor_Inicial < 0:
                Valor_Inicial = float(input("\nValor inválido!\nPor favor insira um valor válido: "))

            print(f"O valor inicial da sua conta é: {Valor_Inicial}")
            transacoes.append(["VALOR INICIAL", Valor_Inicial, data])

            break    

        elif Perg_Valor_Inicial == "2":
            inicio()


    while True:
        Perg_Valor_Novo = input("\nDeseja inserir um valor novo?\n1 - Sim\n2 - Não\nO que você deseja?: ")
        
        while Perg_Valor_Novo.isnumeric() == False or (Perg_Valor_Novo != "1" and Perg_Valor_Novo != "2"):
            Perg_Valor_Novo = input("\nOpção inválida, por favor, escolha entre as seguintes opções\n1 - Sim\n2 - Não\nO que você deseja?: ")


        # PERGUNTA SOBRE VALOR NOVO
        if Perg_Valor_Novo == "1":
            
            Tipo_Valor_Novo = input("\nO que seria o valor?\n1 - Receita\n2 - Despesa\nR: ")
            
            while Tipo_Valor_Novo.isnumeric() == False or (Tipo_Valor_Novo != "1" and Tipo_Valor_Novo != "2"):
                Perg_Valor_Novo = input("\nOpção inválida, por favor, escolha entre as seguintes opções\n1 - Receita\n2 - Despesa\nO que você deseja?: ")

            # RECEITA
            if Tipo_Valor_Novo == "1":
                
                Receita_Valor_Novo = float(input("\nValor da nova receita: "))
                
                while Receita_Valor_Novo < 0:
                    Receita_Valor_Novo = float(input("\nValor Inválido \nInsira o valor da nova receita: "))
                
                Desc_Receita_Valor_Novo = input("Descrição da nova receita: ")

                Valor_Inicial += Receita_Valor_Novo

                print(f"Receita adicionada. Novo saldo: {Valor_Inicial} \nReceita inserida foi de: {Receita_Valor_Novo} {Desc_Receita_Valor_Novo} na data {data}")
                
                transacoes.append(["RECEITA",Valor_Inicial, Receita_Valor_Novo, Desc_Receita_Valor_Novo, data])
                
                print(transacoes) #remover essa linha depois

            # DESPESA
            elif Tipo_Valor_Novo == "2":

                Despesa_Valor_Novo = float(input("\nValor da nova despesa: "))

                while Despesa_Valor_Novo < 0 or Despesa_Valor_Novo > Valor_Inicial:
                    Despesa_Valor_Novo = float(input("\nValor Inválido \nInsira o valor da nova despesa: "))

                

                Desc_Despesa_Valor_Novo = input("Descrição da nova despesa: ")

                Valor_Inicial -= Despesa_Valor_Novo

                print(f"Despesa adicionada. Novo saldo: {Valor_Inicial} \nDespesa inserida foi de: {Despesa_Valor_Novo} {Desc_Despesa_Valor_Novo} na data {data}")
                
                transacoes.append(["RECEITA", Valor_Inicial, Despesa_Valor_Novo, Desc_Despesa_Valor_Novo, data])

                print(transacoes) #remover essa linha depois  

        elif Perg_Valor_Novo == "2":
            menu_principal()

    return transacoes, menu_principal()
    

def remover_transacao(transacoes):
    while True:
        if not transacoes:
            print("\nNenhuma transação para remover.")
            return

        print("\nTRANSAÇÕES ATUAIS: ")
        
        i = 1  
        for transacao in transacoes:
            print(f"\n{i}: {transacao}")
            i += 1  

        try:
            indice = int(input("\nInforme o número da transação que deseja remover: ")) - 1
            if 0 <= indice < len(transacoes):
                transacao_removida = transacoes.pop(indice)
                print(f"\nTransação removida: {transacao_removida}")
                print("\nTransações restantes:", transacoes)
            else:
                print("Número inválido.")
        except ValueError:
            print("Erro: Você não digitou um número válido.")

        continuar = input("Deseja remover outra transação? (sim/não): ").strip().lower()
        if continuar.lower() == 'não':
            print("Encerrando a remoção de transações.")
            break
    return transacoes, menu_principal()


def visualizar_relatorio(transacoes):
    print("Relatório de transações:")
    print("Saldo final: ", transacoes[-1][-4])    
    print("Receitas:")
    for transacao in transacoes:
        if transacao[0] == "RECEITA":
            print(f"{transacao[4]} - {transacao[2]} {transacao[3]}")
    print("Despesas:")
    for transacao in transacoes:
        if transacao[0] == "DESPESA":
            print(f"{transacao[4]} - {transacao[2]} {transacao[3]}")
    return transacoes, menu_principal()


def obter_insights(transacoes):
    if not transacoes:
        print("Nenhuma tranação disnível para analise.")
        return

    total_receitas = 0
    total_despesas = 0
    maior_receita = 0
    maior_despesa = 0
    num_receitas = 0
    num_despesas = 0

    for transacao in transacoes:
        tipo = transacao[0]
        valor = transacao[2]

        if tipo == "RECEITA" :
            total_receitas += valor
            num_receitas += 1
            if valor > maior_receita :
                maior_receita = valor
    
        elif tipo == "DESPESA" :
            total_despesas += valor
            num_despesas += 1
            if valor > maior_despesa :
                maior_despesa = valor

    media_receitas = total_receitas / num_receitas if num_receitas > 0 else 0
    media_despesas = total_despesas / num_despesas if num_despesas > 0 else 0

    print("Média de receitas:", media_receitas)
    print("Média de despesas:", media_despesas)
    print("Maior receita:", maior_receita)
    print("Maior despesa:", maior_despesa)
    menu_principal()


def salvar_dados():
    exit()


def carregar_dados():
    exit()


def encerrar():
    exit()


def main():
    inicio()
    # valorTransacao = adicionar_transacao(transacoes)
    # remover = remover_transacao(valorTransacao)
    # relatorio = visualizar_relatorio(remover)
    # insight = obter_insights(relatorio)


if __name__ == "__main__":
    main()



###### ADICIONAR TRANSACAO ORIGINAL:

# if not transacoes:
#         respostaInicial = input("\nDeseja começar com um valor inicial na sua conta? (sim/não): ") 
#         if respostaInicial.lower() == 'sim':
#             while True:
#                 try:
#                     valorInicial = float(input("Qual o valor inicial da sua conta?: "))
#                     if valorInicial < 0:
#                         print("Valor inicial inválido. Informe um valor positivo.")
#                     else:
#                         print(f"O valor inicial da sua conta é: {valorInicial}")
#                         break
#                 except ValueError:
#                     print("Erro: Você não digitou um número válido.")
#         elif respostaInicial.lower() == 'não':
#             valorInicial = 0
#             print(f"Seu saldo atual é de: {valorInicial}")
#         else:
#             print("Resposta inválida. O programa será encerrado.")
#             return
    
#         while True:
#             try:
#                 inserirValor = int(input("Deseja inserir um novo valor: 1 [SIM] ou 2 [NÃO]? "))

#                 if inserirValor == 1:
#                     respostaUsuario = int(input("Você deseja inserir uma: 1 [RECEITA] ou 2 [DESPESA]? "))
                    

#                     if respostaUsuario == 1:
#                         valor = float(input("Qual o valor da receita? "))
#                         descricao = input("Digite a sua descrição para o valor: ")
                    
#                         ### LOOPAR ERRO NO VALOR
#                         if valor < 0:
#                             print("Valor inválido. Informe um valor positivo.")
#                         else:
#                             valorInicial += valor
#                             print(f"Receita adicionada. Novo saldo: {valorInicial}\nReceita inserida foi de: {valor} {descricao} na data {data}")
#                             transacoes.append(["RECEITA",valorInicial, valor, descricao, data])
#                             print(transacoes) #remover essa linha depois

#                     elif respostaUsuario == 2:
#                         valor = float(input("Qual o valor da despesa? "))
#                         descricao = input("Digite a sua descrição para o valor: ")
#                         if valor < 0:
#                             print("Valor inválido. Informe um valor positivo.")
#                         elif valorInicial >= valor:
#                             valorInicial -= valor
#                             print(f"Despesa adicionada. Novo saldo: {valorInicial}\nDespesa inserida foi de: {valor} {descricao} na data {data}")
#                             transacoes.append(["DESPESA",valorInicial, valor, descricao, data])
#                             print(transacoes) #remover essa linha depois
                        
#                         else:
#                             print("Saldo insuficiente. Transação recusada!")

#                     else:
#                         print("Opção inválida. Informe 1 [RECEITA] ou 2 [DESPESA].")
#                 # ARRUMAR AQUI
#                 elif inserirValor == 2:
#                     print("Encerrando o programa.")
#                     break
#                 else:
#                     print("Opção inválida. Informe 1 [SIM] ou 2 [NÃO].")

#             except ValueError:
#                 print("Erro: Você não digitou um número válido.")
#         return transacoes, menu_principal()