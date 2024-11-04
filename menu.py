# from movimentacao import adicionar_transacao, remover_transacao
# from cp3 import encerrar, visualizar_relatorio, obter_insights, salvar_dados

def inicio():

    from cp3 import encerrar
    from movimentacao import adicionar_transacao

    opcao = input("\nBEM-VINDO! \nNotamos que seu histórico de transação está vázio, por favor comece adicionando uma transação!\n1 - Adicionar Transação\n2 - Encerrar Programa\nO que você deseja?: ")
    transacoes = []
    Valor_Inicial = 0

    while opcao.isnumeric() == False or (opcao != "1" and opcao != "2"):
        opcao = input("\nOpção inválida, por favor, escolha entre as seguintes opções\n1 - Adicionar Transação\n2 - Encerrar Programa\nO que você deseja?: ")

    if opcao == "1":
        adicionar_transacao(Valor_Inicial, transacoes)
        # resposta = adicionar_transacao(Valor_Inicial, transacoes)
        # if resposta == 'nao':
         # return
    elif opcao == "2":
        encerrar()  

    return Valor_Inicial, transacoes  


def menu_principal(Valor_Inicial, transacoes):

    from movimentacao import adicionar_transacao, remover_transacao
    from cp3 import visualizar_relatorio, obter_insights, salvar_dados, encerrar

    opcao = input("\nBEM-VINDO! \n1 - Adicionar Transação\n2 - Remover Transação\n3 - Visualizar Relatório\n4 - Obter Insights\n5 - Salvar Dados\n6 - Encerrar Programa\n\nO que você deseja?: ")

    while opcao.isnumeric() == False or (opcao != "1" and opcao != "2" and opcao != "3" and opcao != "4" and opcao != "5" and opcao != "6"):
        opcao = input("\nOpção inválida, por favor, escolha entre as seguintes opções\n1 - Adicionar Transação\n2 - Remover Transação\n3 - Visualizar Relatório\n4 - Obter Insights\n5 - Salvar Dados\n6 - Encerrar Programa\n\nO que você deseja?: ")

    if opcao == "1":
        adicionar_transacao(Valor_Inicial, transacoes)
    elif opcao == "2":
        remover_transacao(Valor_Inicial, transacoes)
    elif opcao == "3":
        visualizar_relatorio(Valor_Inicial, transacoes)
    elif opcao == "4":
        obter_insights(Valor_Inicial, transacoes)
    elif opcao == "5":
        salvar_dados(Valor_Inicial, transacoes, nome_arquivo="transacoes.csv")
    elif opcao == "6":
        encerrar()      