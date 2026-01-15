# --- 1. Configurações e Dados ---

altura_input = 0
peso_input = 0

def classificar_imc(imc):
    # --- 2. Classificação do IMC ---
    if (imc < 18.5):
        print("Classificação: Abaixo do peso")
        print("Aviso: Seu peso está abaixo do recomendado.")
    elif (18.5 <= imc < 24.9):
        print("Classificação: Peso normal")
        print("Parabéns! Você está dentro do peso adequado.")
    elif (25 <= imc < 29.9):
        print("Classificação: Sobrepeso")
        print("Aviso: Atenção! Seu peso está acima do recomendado.")
    elif (30 <= imc < 34.9):
        print("Classificação: Obesidade Grau I")
        print("Aviso: Cuidado! Procure acompanhamento médico e nutricional.")
    elif (35 <= imc < 39.9):
        print("Classificação: Obesidade Grau II")
        print("Aviso: Cuidado! Procure acompanhamento médico e nutricional.")
    else:  
        print("Classificação: Obesidade Grau III")
        print("Aviso: Cuidado! Procure acompanhamento médico e nutricional.")

def definir_dados(altura_input, peso_input):

    altura_input = float(input("Digite sua altura em metros (ex: 1.75): "))
    peso_input = float(input("Digite seu peso em kg (ex: 70.5): "))

    # --- 3. Cálculo do IMC ---
    imc = peso_input / (altura_input ** 2)

    print(f"Seu IMC é: {imc:.2f}")
    classificar_imc(imc)
    return altura_input, peso_input

# --- 4. Execução do Programa ---

while True:
    print("\nCalculadora de IMC")
    escolha = int(input("Você deseja 1. Calcular IMC ou 2. Sair? "))

    if (escolha == 2):
        print("Encerrando o programa. Obrigada!")
        break   
    else:
        definir_dados(altura_input, peso_input)