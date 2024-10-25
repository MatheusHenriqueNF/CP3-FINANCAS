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
                transacoes.append(valorInicial)
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
        


# def removerTransacao(valor):

#     if not valor:
#         print("Nenhuma transação para remover.")
#         return

#     print("Transações atuais: ")
#     for i, transacao in range(valor):
#         print(f"{i+1}. {transacao}")

#     indice = int(input("Informe o número da transação que deseja remover: "))
#     if indice <= 0 < len(valor):
#         transacao_removida = valor.pop(indice)
#         print(f"Transação removida: {transacao_removida}")
#     else:
#         print("Número errado")


def main():
    valorTransacao = adicionar_transacao()
    # remover = removerTransacao(valorTransacao)

if __name__ == "__main__":
    main()
