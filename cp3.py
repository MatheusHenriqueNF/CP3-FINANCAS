#Funcionalidades: - Adicionar transações (receitas e despesas) - Visualizar o saldo atual - Gerar um relatório de transações - Categorizar transações

#Estruturas de Dados: Utilize listas para armazenar as transações, onde cada transação é
#um dicionário contendo tipo (receita ou despesa), valor, categoria, e data.
#Dicionários podem ser usados para categorizar as transações e calcular totais por categoria.

from datetime import datetime
import csv

# Obtendo a data e hora atuais
agora = datetime.now()
data = agora.strftime("%d/%m/%Y %H:%M:%S")
transacoes = []
Valor_Inicial = 0

def inicio():
    opcao = input("\nBEM-VINDO! \nNotamos que seu histórico de transação está vázio, por favor comece adicionando uma transação!\n1 - Adicionar Transação\n2 - Encerrar Programa\nO que você deseja?: ")

    while opcao.isnumeric() == False or (opcao != "1" and opcao != "2"):
        opcao = input("\nOpção inválida, por favor, escolha entre as seguintes opções\n1 - Adicionar Transação\n2 - Encerrar Programa\nO que você deseja?: ")
       

    if opcao == "1":
        adicionar_transacao(transacoes)
    elif opcao == "2":
        encerrar()    


def menu_principal(transacoes):
    opcao = input("\nBEM-VINDO! \n1 - Adicionar Transação\n2 - Remover Transação\n3 - Visualizar Relatório\n4 - Obter Insights\n5 - Salvar Dados\n6 - Encerrar Programa\n\nO que você deseja?: ")

    while opcao.isnumeric() == False or (opcao != "1" and opcao != "2" and opcao != "3" and opcao != "4" and opcao != "5" and opcao != "6"):
        opcao = input("\nOpção inválida, por favor, escolha entre as seguintes opções\n1 - Adicionar Transação\n2 - Remover Transação\n3 - Visualizar Relatório\n4 - Obter Insights\n5 - Salvar Dados\n6 - Encerrar Programa\n\nO que você deseja?: ")

    if opcao == "1":
        adicionar_transacao(transacoes)
    elif opcao == "2":
        remover_transacao(transacoes)
    elif opcao == "3":
        visualizar_relatorio(transacoes)
    elif opcao == "4":
        obter_insights(transacoes)
    elif opcao == "5":
        salvar_dados(transacoes)
    elif opcao == "6":
        encerrar()                            


def adicionar_transacao(transacoes):
    global Valor_Inicial
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
            menu_principal(transacoes)

        return transacoes, menu_principal(transacoes)
    

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
    return transacoes, menu_principal(transacoes)


def visualizar_relatorio(transacoes):
    global Valor_Inicial
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
    return transacoes, menu_principal(transacoes)


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

    print("Média de receitas: R$", media_receitas)
    print("Média de despesas: R$", media_despesas)
    print("Maior receita: R$", maior_receita)
    print("Maior despesa: R$", maior_despesa)
    menu_principal(transacoes)


def salvar_dados(valores, nome_arquivo="transacoes.csv"):
    """Salva os registros em um arquivo CSV."""
    try:
        with open(nome_arquivo, 'w', newline='') as arquivo:
            escritor = csv.writer(arquivo)
            # Escreve o cabeçalho
            escritor.writerow(["Tipo", "Valor na conta", "Movimentacao" ,"Descricao", "Data"])
            # Escreve cada registro
            for registro in valores:
                escritor.writerow(registro)
        print(f"Registros salvos com sucesso em '{nome_arquivo}'.")
    except Exception as e:
        print(f"Ocorreu um erro ao salvar os registros: {e}")


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