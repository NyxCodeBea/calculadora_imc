# ⚖️ Calculadora de IMC (Índice de Massa Corporal)

![Badge Concluído](http://img.shields.io/static/v1?label=STATUS&message=CONCLUÍDO&color=GREEN&style=for-the-badge) ![Badge Python](http://img.shields.io/static/v1?label=LINGUAGEM&message=PYTHON&color=blue&style=for-the-badge)

Projeto desenvolvido em Python para cálculo e classificação de IMC, com foco em estrutura de dados, funções e experiência do usuário (UX).

## 📝 Histórico de Versões

### Versão 1.0: Estrutura Base
O lançamento inicial do projeto.
* **Modularização:** Separação da lógica em funções (`def`) para cálculo e classificação.
* **Loop de Execução:** Uso de `while True` para manter o programa rodando até o usuário decidir sair.
* **Cálculo Base:** Fórmula padrão do IMC aplicada corretamente.

### Versão 1.1: Refinamento de UX e Lógica (Atual)
Foco na robustez do código e facilidade de uso.
* **Entrada de Dados Flexível:** Implementação do método `.replace(",", ".")`, permitindo que o usuário digite o peso com ponto ou vírgula sem causar erros.
* **Melhoria na UX (Altura):** O usuário agora pode digitar a altura em centímetros (inteiro), e o sistema converte automaticamente para metros na fórmula (`/ 100`).
* **Lógica de Classificação:** Ajuste nos intervalos condicionais (`elif`) para cobrir todas as faixas decimais (ex: `< 25` em vez de `< 24.9`), evitando "buracos" na classificação.
* **Estrutura Limpa:** Remoção de variáveis globais desnecessárias; as funções `definir_dados` e `classificar_imc` são autossuficientes.

