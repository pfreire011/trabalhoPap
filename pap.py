import numpy_financial as npf

#Questão 1)
custoRef = 45600  # Custo de referência ($)
capacidadeNecessária = 4  
capacidadeReferência = 4.5  
n = 0.6  # Exponente de extrapolação
CEPCI_ano = 500  
CEPCI_atual = 574  
fatorNacionalizacao = 1.74  
fatorInstalacao = 1.74 

C1 = custoRef * (capacidadeNecessária / capacidadeReferência)**n
C2 = C1 * (CEPCI_atual / CEPCI_ano)
C3 = C2 * fatorNacionalizacao
C_final = C3 * fatorInstalacao

print("questão 1")
print("letra a)", C1) 
print("letra b)", C2) 
print("letra c)", C3) 
print("letra d)", C_final) 


#Questão 2)
#letra a)
valorFinanciado = 7400000  
i = 0.14  # Taxa de juros anual
n = 10  # Número de prestações

A = valorFinanciado * (i * (1 + i)**n) / ((1 + i)**n - 1)
montoTotal = A * n
jurosTotais = montoTotal - valorFinanciado
print("questão 2")
print("letra a)", jurosTotais)

#letra b)
print("letra b)",montoTotal)

#letra c)
A_amort = valorFinanciado / n

saldoDevedor = valorFinanciado
juros_totais_amort = 0
prestacoes_amort = []

for ano in range(1, n + 1):
    jurosAno = saldoDevedor * i
    prestacao_ano = A_amort + jurosAno
    juros_totais_amort += jurosAno
    saldoDevedor -= A_amort
    prestacoes_amort.append(prestacao_ano)

montante_total_amort = sum(prestacoes_amort)

print("letra c)", juros_totais_amort)
#5698000.000000001
print("letra d)", montante_total_amort)
#13098000.0
print("letra e)", jurosTotais-juros_totais_amort)
#1088802.0224172408

#questão 3
investimento_inicial = 388374 
cap_max = 574
preco_venda_unitario = 1274
custos_variaveis = 874
custos_fixos_desembolsaveis = 95374
depreciacao_anual = 0.1 * investimento_inicial
taxa_imposto_renda = 0.34

def estimativa_producao_anual(cap_max, ano):
    return cap_max * (1 - 1 / (2 ** ano))

def receita_anual(prod, preco_venda_unitario):
    return prod * preco_venda_unitario

def custos_variaveis_anuais(prod, custos_variaveis):
    return prod * custos_variaveis

def lucro_bruto(receita, custos_variaveis, custos_fixos):
    return receita - custos_variaveis - custos_fixos

def lucro_antes_impostos(lucro_bruto, depreciacao):
    return lucro_bruto - depreciacao

def lucro_depois_impostos(lucro_antes_impostos, taxa_imposto_renda):
    return lucro_antes_impostos * (1 - taxa_imposto_renda)

def ponto_de_nivelamento(custos_fixos, preco_venda_unitario, custos_variaveis):
    return custos_fixos / (preco_venda_unitario - custos_variaveis)

ano = 10
prod_ano_10 = estimativa_producao_anual(cap_max, ano)
receita_ano_10 = receita_anual(prod_ano_10, preco_venda_unitario)
custos_variaveis_ano_10 = custos_variaveis_anuais(prod_ano_10, custos_variaveis)
lucro_bruto_ano_10 = lucro_bruto(receita_ano_10, custos_variaveis_ano_10, custos_fixos_desembolsaveis)
lucro_antes_impostos_ano_10 = lucro_antes_impostos(lucro_bruto_ano_10, depreciacao_anual)
lucro_depois_impostos_ano_10 = lucro_depois_impostos(lucro_antes_impostos_ano_10, taxa_imposto_renda)
ponto_nivelamento = ponto_de_nivelamento(custos_fixos_desembolsaveis, preco_venda_unitario, custos_variaveis)

print("questão 3")
print(f"letra a): ${receita_ano_10:.2f}")
print(f"Letra b): ${lucro_bruto_ano_10:.2f}")
print(f"Letra c): ${lucro_antes_impostos_ano_10:.2f}")
print(f"Letra d): ${lucro_depois_impostos_ano_10:.2f}")
print(f"letra e): {ponto_nivelamento:.2f} ton")

#questão 4
ultimos_4_digitos = 8374
investimento_inicial = 1008374
taxa_imposto_renda = 0.30
taxa_minima_atratividade = 0.10
horizonte_projecao = 15


def receita_anual(ano):
    return 800000 * (1 - 1 / (2 ** ano))

def custos_variaveis_anuais(ano):
    return 400000 * (1 - 1 / (2 ** ano))

def depreciacao_anual(investimento):
    return 0.1 * investimento

def fluxo_de_caixa_anual(ano, investimento):
    receita = receita_anual(ano)
    custos_variaveis = custos_variaveis_anuais(ano)
    custos_fixos = 50000
    depreciacao = depreciacao_anual(investimento) if ano <= 10 else 0
    lucro_bruto = receita - custos_variaveis - custos_fixos
    lucro_antes_impostos = lucro_bruto - depreciacao
    impostos = lucro_antes_impostos * taxa_imposto_renda
    lucro_liquido = lucro_antes_impostos - impostos
    fluxo_de_caixa = lucro_liquido + depreciacao
    return fluxo_de_caixa

fluxos_de_caixa = [-investimento_inicial] + [fluxo_de_caixa_anual(ano, investimento_inicial) for ano in range(1, horizonte_projecao + 1)]

def calcular_vpl(fluxos, taxa):
    return npf.npv(taxa, fluxos)

def calcular_tir(fluxos):
    return npf.irr(fluxos)

def calcular_tempo_retorno(fluxos):
    acumulado = 0
    for ano, fluxo in enumerate(fluxos):
        acumulado += fluxo
        if acumulado >= 0:
            return ano
    return None

def calcular_indice_lucratividade(fluxos, investimento):
    vpl = calcular_vpl(fluxos, taxa_minima_atratividade)
    return (vpl + investimento) / investimento

vpl = calcular_vpl(fluxos_de_caixa, taxa_minima_atratividade)
tir = calcular_tir(fluxos_de_caixa)
tempo_retorno = calcular_tempo_retorno(fluxos_de_caixa)
indice_lucratividade = calcular_indice_lucratividade(fluxos_de_caixa, investimento_inicial)

print("questão 4)")
print(f"Letra a): ${vpl:.2f}")
print(f"Letra b): {tir:.2%}")
print(f"Letra c): {tempo_retorno} anos")
print(f"Letra d): {indice_lucratividade:.2f}")