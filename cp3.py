#Funcionalidades: - Adicionar transações (receitas e despesas) - Visualizar o saldo atual - Gerar um relatório de transações - Categorizar transações

#Estruturas de Dados: Utilize listas para armazenar as transações, onde cada transação é um dicionário contendo tipo (receita ou despesa), valor, categoria, e data. Dicionários podem ser usados para categorizar as transações e calcular totais por categoria.


def transacaoEntrada():
    
    transacaoLista = {
        "RECEITA": [],
        "DESPESA": []
    }
    
    while True:
        resposta = input("Deseja adicionar uma nova transacção? (SIM/NÃO): ")

        if resposta.upper() == "SIM":
            
            entrada = float(input("Digite o valor da transacção: "))
            tipo = int(input("Digite o tipo da transacção 1 [RECEITA] ou 2 [DESPESA]): "))
            
            if tipo == 1:
                transacaoLista["RECEITA"].append(entrada)

            print("O valor de R$" + str(entrada) + " foi adicionado a sua conta!")
        
        else:
           break

    return transacaoLista
    

def transacaoSaida():
    pass

def saldoAtual():
    pass

def relatorioTransacoes():
    pass

def categorizarTransacoes():
    pass

def main():
    valorEntrada = transacaoEntrada()

if __name__ == "__main__":
    main()