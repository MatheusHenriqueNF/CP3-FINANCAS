#Funcionalidades: - Adicionar transações (receitas e despesas) - Visualizar o saldo atual - Gerar um relatório de transações - Categorizar transações

#Estruturas de Dados: Utilize listas para armazenar as transações, onde cada transação é
#um dicionário contendo tipo (receita ou despesa), valor, categoria, e data.
#Dicionários podem ser usados para categorizar as transações e calcular totais por categoria.

from datetime import datetime

# Obtendo a data e hora atuais
agora = datetime.now()
data = agora.strftime("%d/%m/%Y %H:%M:%S")

def adicionar_transacao():
    respostaInicial = input("Deseja começar com um valor inicial na sua conta? (sim/não) ")
    transacoes = []

    if respostaInicial.lower() == 'sim':
        while True:
            try:
                valorInicial = float(input("Qual o valor inicial da sua conta? "))
                if valorInicial < 0:
                    print("Valor inicial inválido. Informe um valor positivo.")
                else:
                    print(f"O valor inicial da sua conta é: {valorInicial}")
                    break
            except ValueError:
                print("Erro: Você não digitou um número válido.")
    elif respostaInicial.lower() == 'não':
        valorInicial = 0
        print(f"Seu saldo atual é de: {valorInicial}")
    else:
        print("Resposta inválida. O programa será encerrado.")
        return

    while True:
        try:
            inserirValor = int(input("Deseja inserir um novo valor: 1 [SIM] ou 2 [NÃO]? "))

            if inserirValor == 1:
                respostaUsuario = int(input("Você deseja inserir uma: 1 [RECEITA] ou 2 [DESPESA]? "))
                

                if respostaUsuario == 1:
                    valor = float(input("Qual o valor da receita? "))
                    descricao = input("Digite a sua descrição para o valor: ")
                   

                    if valor < 0:
                        print("Valor inválido. Informe um valor positivo.")
                    else:
                        valorInicial += valor
                        print(f"Receita adicionada. Novo saldo: {valorInicial}\nReceita inserida foi de: {valor} {descricao} na data {data}")
                        transacoes.append(["RECEITA",valorInicial, valor, descricao, data])
                        print(transacoes) #remover essa linha depois

                elif respostaUsuario == 2:
                    valor = float(input("Qual o valor da despesa? "))
                    descricao = input("Digite a sua descrição para o valor: ")
                    if valor < 0:
                        print("Valor inválido. Informe um valor positivo.")
                    elif valorInicial >= valor:
                        valorInicial -= valor
                        print(f"Despesa adicionada. Novo saldo: {valorInicial}\nDespesa inserida foi de: {valor} {descricao} na data {data}")
                        transacoes.append(["DESPESA",valorInicial, valor, descricao, data])
                        print(transacoes) #remover essa linha depois
                    
                    else:
                        print("Saldo insuficiente. Transação recusada!")

                else:
                    print("Opção inválida. Informe 1 [RECEITA] ou 2 [DESPESA].")

            elif inserirValor == 2:
                print("Encerrando o programa.")
                break
            else:
                print("Opção inválida. Informe 1 [SIM] ou 2 [NÃO].")

        except ValueError:
            print("Erro: Você não digitou um número válido.")
    return transacoes

def remover_transacao(transacoes):
    while True:
        if not transacoes:
            print("Nenhuma transação para remover.")
            return

        print("Transações atuais: ")
        
        i = 1  
        for transacao in transacoes:
            print(f"{i}: {transacao}")
            i += 1  

        try:
            indice = int(input("Informe o número da transação que deseja remover: ")) - 1
            if 0 <= indice < len(transacoes):
                transacao_removida = transacoes.pop(indice)
                print(f"Transação removida: {transacao_removida}")
                print("Transações restantes:", transacoes)
            else:
                print("Número inválido.")
        except ValueError:
            print("Erro: Você não digitou um número válido.")

        continuar = input("Deseja remover outra transação? (sim/não): ").strip().lower()
        if continuar.lower() == 'não':
            print("Encerrando a remoção de transações.")
            break
    return transacoes


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
    return transacoes

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

def main():
    valorTransacao = adicionar_transacao()
    remover = remover_transacao(valorTransacao)
    relatorio = visualizar_relatorio(remover)
    insight = obter_insights(relatorio)

if __name__ == "__main__":
    main()
