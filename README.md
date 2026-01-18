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

# ⚖️ Calculadora de IMC 2.0 (Visual Edition)

![Badge Flet](http://img.shields.io/static/v1?label=INTERFACE&message=FLET&color=blue&style=for-the-badge) ![Badge Python](http://img.shields.io/static/v1?label=STATUS&message=CONCLUÍDO&color=GREEN&style=for-the-badge)

## 📝 Descrição

Esta é a evolução da calculadora de IMC clássica. Deixamos o terminal de lado para criar uma **Aplicação Desktop Moderna** utilizando a biblioteca **Flet**.

O diferencial deste projeto é o **Feedback Visual Dinâmico**: a interface reage ao resultado do cálculo. Não é apenas um número na tela; o usuário recebe um cartão informativo que muda de cor (Verde, Amarelo, Vermelho) dependendo da gravidade do IMC, simulando alertas de saúde reais.

## 📸 Screenshots

<img width="1366" height="768" alt="image" src="https://github.com/user-attachments/assets/a155c58b-892f-4bcc-80fd-4cb7a63e4b27" />

<img width="1366" height="768" alt="image" src="https://github.com/user-attachments/assets/16d0c1ae-766f-4a58-9ff8-5ebdc7a17da0" />

<img width="1366" height="768" alt="image" src="https://github.com/user-attachments/assets/ef88f0c1-5833-4565-a151-8449063eb407" />

Imagens da aplicação rodando, mostrando a diferença entre o cartão Verde e o Amarelo/Vermelho)

## 🚀 Funcionalidades

- **🎨 Interface Reativa:** O container de resultado muda de cor (`bgcolor`) automaticamente:
  - 🟢 **Verde:** Peso Normal.
  - 🟠 **Laranja/Amarelo:** Sobrepeso ou Abaixo do Peso.
  - 🔴 **Vermelho:** Obesidade.
- **📝 Markdown Render:** Uso de renderização Markdown para exibir textos com formatação rica (negrito e títulos) dentro da interface.
- **🛡️ Tratamento de Dados:**
  - Aceita tanto ponto (`.`) quanto vírgula (`,`) como separador decimal.
  - Previne erros se os campos estiverem vazios.

## 🧠 Aprendizados Técnicos

Neste projeto, apliquei conceitos de **UI/UX** e estruturas de dados mais elaboradas:

1.  **Tuplas no Retorno de Função:**
    A lógica de classificação não retorna apenas o texto, mas também a cor correspondente.
    ```python
    def classificar_imc(imc):
        if imc < 18.5:
             # Retorna (Texto, Cor)
            return ("Abaixo do peso...", "orange")
    ```

2.  **Hierarquia Visual:** Uso de `ft.Container` como elemento "pai" para controlar o fundo e as bordas, enquanto o `ft.Markdown` (elemento "filho") cuida do conteúdo.

## 🔧 Como Executar

1. Instale o Flet:
```bash
pip install flet

```

2. Execute o app:

```bash
python imc_visual.py

```

---
