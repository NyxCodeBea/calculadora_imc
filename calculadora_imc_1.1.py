# --- 1. Configurações e Dados ---
# Removemos as variáveis globais daqui (altura_input = 0...), pois elas nascem dentro da função agora.

def classificar_imc(imc):
    # --- 2. Classificação do IMC ---
    if (imc < 18.5):
        print("Classificação: Abaixo do peso")
        print("Aviso: Seu peso está abaixo do recomendado.")
    elif (18.5 <= imc < 25):
        print("Classificação: Peso normal")
        print("Parabéns! Você está dentro do peso adequado.")
    elif (25 <= imc < 30):
        print("Classificação: Sobrepeso")
        print("Aviso: Atenção! Seu peso está acima do recomendado.")
    elif (30 <= imc < 35):
        print("Classificação: Obesidade Grau I")
        print("Aviso: Cuidado! Procure acompanhamento médico e nutricional.")
    elif (35 <= imc < 40):
        print("Classificação: Obesidade Grau II")
        print("Aviso: Cuidado! Procure acompanhamento médico e nutricional.")
    else:  
        print("Classificação: Obesidade Grau III")
        print("Aviso: Cuidado! Procure acompanhamento médico e nutricional.")

def definir_dados():
    # PARÊNTESES VAZIOS: A função começa "zerada" e coleta os dados aqui dentro
    altura_input = int(input("Digite sua altura em centímetros (ex: 175): "))
    peso_string = input("Digite seu peso em kg (ex: 70.5): ").replace(",", ".")

    peso_input = float(peso_string)

    # --- 3. Cálculo do IMC ---
    imc = peso_input / ((altura_input / 100) ** 2)

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
        altura_input, peso_input = definir_dados()