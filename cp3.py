#Funcionalidades: - Adicionar transações (receitas e despesas) - Visualizar o saldo atual - Gerar um relatório de transações - Categorizar transações

#Estruturas de Dados: Utilize listas para armazenar as transações, onde cada transação é
#um dicionário contendo tipo (receita ou despesa), valor, categoria, e data.
#Dicionários podem ser usados para categorizar as transações e calcular totais por categoria.

# from menu import inicio, menu_principal
# from movimentacao import adicionar_transacao, remover_transacao

import csv 
                      
def visualizar_relatorio(Valor_Inicial, transacoes):

    from menu import menu_principal

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
    return transacoes, menu_principal(Valor_Inicial, transacoes)


def obter_insights(Valor_Inicial, transacoes):

    from menu import menu_principal

    if not transacoes:
        print("Nenhuma transação disponível para análise.")
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
    menu_principal(Valor_Inicial, transacoes)


def salvar_dados(Valor_Inicial, transacoes, nome_arquivo="transacoes.csv"):

    from menu import menu_principal

    """Salva os registros em um arquivo CSV."""
    try:
        with open(nome_arquivo, 'w', newline='') as arquivo:
            escritor = csv.writer(arquivo)
            # Escreve o cabeçalho
            escritor.writerow(["Tipo", "Valor na conta", "Movimentacao" ,"Descricao", "Data"])
            # Escreve cada registro
            for registro in transacoes:
                escritor.writerow(registro)
        print(f"Registros salvos com sucesso em '{nome_arquivo}'.")
    except Exception as e:
        print(f"Ocorreu um erro ao salvar os registros: {e}")
    menu_principal(Valor_Inicial, transacoes)    


def encerrar():
    exit()


def main():

    from menu import inicio

    inicio()
    # valorTransacao = adicionar_transacao(transacoes)
    # remover = remover_transacao(valorTransacao)
    # relatorio = visualizar_relatorio(remover)
    # insight = obter_insights(relatorio)


if __name__ == "__main__":
    main()