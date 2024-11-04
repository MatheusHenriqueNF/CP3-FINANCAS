from datetime import datetime

agora = datetime.now()
data = agora.strftime("%d/%m/%Y %H:%M:%S")   

def adicionar_transacao(Valor_Inicial, transacoes):

    from menu import menu_principal

    while not transacoes:
        
        Perg_Valor_Inicial = input("\nDeseja começar com um valor inicial na sua conta?\n1 - Sim\n2 - Não\nO que deseja?: ")
        
        while Perg_Valor_Inicial.isnumeric() == False or (Perg_Valor_Inicial != "1" and Perg_Valor_Inicial != "2"):
            Perg_Valor_Inicial = input("Opção inválida, por favor, escolha entre as seguintes opções\n1 - Sim\n2 - Não\nO que você deseja?: ")

        if Perg_Valor_Inicial == "1":
            Valor_Inicial = float(input("\nQual seria o valor inicial?: "))

            while Valor_Inicial < 0:
                Valor_Inicial = float(input("\nValor inválido!\nPor favor insira um valor válido: "))

            print(f"O valor inicial da sua conta é: R${Valor_Inicial}")
            transacoes.append(["VALOR INICIAL", Valor_Inicial, data])

            break    

        elif Perg_Valor_Inicial == "2":
            return 'nao'


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

                print(f"Receita adicionada. Novo saldo: R${Valor_Inicial} \nReceita inserida foi de: R${Receita_Valor_Novo} {Desc_Receita_Valor_Novo} na data {data}")
                
                transacoes.append(["RECEITA",Valor_Inicial, Receita_Valor_Novo, Desc_Receita_Valor_Novo, data])
                
                #print(transacoes) remover essa linha depois

            # DESPESA
            elif Tipo_Valor_Novo == "2":

                Despesa_Valor_Novo = float(input("\nValor da nova despesa: "))

                while Despesa_Valor_Novo < 0 or Despesa_Valor_Novo > Valor_Inicial:
                    Despesa_Valor_Novo = float(input("\nValor Inválido \nInsira o valor da nova despesa: "))

                

                Desc_Despesa_Valor_Novo = input("Descrição da nova despesa: ")

                Valor_Inicial -= Despesa_Valor_Novo

                print(f"Despesa adicionada. Novo saldo: R${Valor_Inicial} \nDespesa inserida foi de: R${Despesa_Valor_Novo} {Desc_Despesa_Valor_Novo} na data {data}")
                
                transacoes.append(["DESPESA", Valor_Inicial, Despesa_Valor_Novo, Desc_Despesa_Valor_Novo, data])

                #print(transacoes) remover essa linha depois  

        elif Perg_Valor_Novo == "2":
            menu_principal(Valor_Inicial, transacoes)

    return Valor_Inicial, transacoes, menu_principal
    

def remover_transacao(Valor_Inicial, transacoes):

    from menu import menu_principal

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
    return transacoes, menu_principal(Valor_Inicial, transacoes)

