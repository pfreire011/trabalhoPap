# Planejamento e Avaliação de Projetos - Solução de Exercícios

## Descrição

Este projeto contém um script em Python (`pap.py`) que resolve uma série de exercícios de planejamento e avaliação de projetos, com base em um arquivo PDF (`Segunda Lista de exercícios PAP.pdf`). Os exercícios abordam temas como estimativa de custos de equipamentos, análise de financiamentos, fluxo de caixa e indicadores econômicos de projetos de investimento.

## Como Usar

Para utilizar este projeto, siga os passos abaixo:

1.  **Clone o repositório:**
    ```bash
    git clone <URL do repositório>
    ```

2.  **Instale as dependências:**
    O projeto utiliza a biblioteca `numpy-financial`. Para instalá-la, execute o seguinte comando no seu terminal:
    ```bash
    pip install numpy-financial
    ```

3.  **Execute o script:**
    Para ver as soluções dos exercícios, basta executar o script `pap.py`:
    ```bash
    python pap.py
    ```
    O script irá imprimir no console as respostas para cada uma das questões propostas no PDF.

## Exercícios

O script `pap.py` está organizado em seções, cada uma correspondendo a uma questão da lista de exercícios.

### Questão 1: Estimativa de Custo de Equipamento

Esta seção do código calcula o custo de um reator para um projeto, ajustando valores de referência de acordo com a capacidade, data e localidade. Os cálculos são feitos em etapas, estimando:
* a) Custo ajustado para a capacidade do projeto.
* b) Custo ajustado para a capacidade e a data do projeto.
* c) Custo ajustado para a capacidade, a data e a localidade.
* d) Custo final do equipamento instalado.

### Questão 2: Análise de Financiamento

Aqui, o script analisa um financiamento para a ampliação de uma unidade produtiva. Ele calcula:
* a) O total de juros a serem pagos em um sistema de prestações constantes.
* b) O montante total a ser pago no sistema de prestações constantes.
* c) O total de juros a serem pagos em um sistema de amortizações constantes.
* d) O montante total a ser pago no sistema de amortizações constantes.
* e) A diferença de juros entre os dois sistemas.

### Questão 3: Fluxo de Caixa

Esta parte do script desenvolve o fluxo de caixa para um projeto de investimento ao longo de 10 anos. Com base nos dados fornecidos, o script calcula para o ano 10:
* a) A receita.
* b) O lucro bruto.
* c) O lucro antes dos impostos.
* d) O lucro depois dos impostos.
* e) O ponto de nivelamento em toneladas.

### Questão 4: Indicadores Econômicos

Por fim, o script calcula os principais indicadores econômicos para avaliar um projeto de investimento com horizonte de 15 anos. Os indicadores calculados são:
* a) Valor Presente Líquido (VPL).
* b) Taxa Interna de Retorno (TIR).
* c) Tempo de Retorno do Investimento (Payback).
* d) Índice de Lucratividade (IL).

## Dependências

Este projeto requer a seguinte biblioteca Python:

* [`numpy-financial`](https://numpy.org/numpy-financial/): Para cálculos financeiros como VPL e TIR.
