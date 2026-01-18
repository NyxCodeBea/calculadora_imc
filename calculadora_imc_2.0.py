# --- 1. Configurações e Dados ---

import flet as ft

def main(page: ft.Page):
    # 1. Configurações da Janela
    page.title = "Calculadora IMC 2.0"
    # Centralizando o conteúdo da página
    page.vertical_alignment = "center" 
    page.horizontal_alignment = "center"
    # Adicionei rolagem caso a tela seja pequena
    page.scroll = "adaptive"

    # 2. Elementos da Interface
    titulo = ft.Text("Calculadora IMC 2.0", size=30, weight=ft.FontWeight.BOLD) # Título

    # Campos de entrada
    altura_input = ft.TextField(label="Altura (cm) - Ex: 175:", width=350, keyboard_type="number")
    peso_input = ft.TextField(label="Peso (kg) - Ex: 70.50:", width=350, keyboard_type="number")
    
    resultado_text = ft.Markdown("", extension_set="gitHubWeb")  # Texto para mostrar o resultado

    # 3. Container para o resultado com padding e borda arredondada
    container_resultado = ft.Container(
        content=resultado_text,
        padding=20,
        border_radius=10,
        bgcolor="transparent" # Começa transparente
    )

    def classificar_imc(imc):
        # --- 2. Classificação do IMC ---
        if (imc < 18.5):
            return (f"### Classificação: Abaixo do peso\n\nSeu IMC é **{imc:.2f}**.\nAviso: Seu peso está abaixo do recomendado.", "orange")
        elif (18.5 <= imc < 25):
            return (f"### Classificação: Peso normal\n\nSeu IMC é **{imc:.2f}**.\nParabéns! Você está dentro do peso adequado.", "green")
        elif (25 <= imc < 30):
            return (f"### Classificação: Sobrepeso\n\nSeu IMC é **{imc:.2f}**.\nAtenção! Seu peso está acima do recomendado.", "amber")
        elif (30 <= imc < 35):
            return (f"### Classificação: Obesidade Grau I\n\nSeu IMC é **{imc:.2f}**.\nCuidado! Procure acompanhamento médico.", "red")
        elif (35 <= imc < 40):
            return (f"### Classificação: Obesidade Grau II\n\nSeu IMC é **{imc:.2f}**.\nCuidado! Procure acompanhamento médico.", "red")
        else:  
            return (f"### Classificação: Obesidade Grau III\n\nSeu IMC é **{imc:.2f}**.\nCuidado! Procure acompanhamento médico.", "red")
    
    def calcular_imc(e):
        try:
            # --- 3. Cálculo do IMC ---
            altura_str = altura_input.value # Pegando o valor do campo de altura
            peso_str = peso_input.value.replace(",", ".") # Pegando o valor do campo de peso e substituindo vírgula por ponto

            if not altura_str or not peso_str:
                return # Não faz nada se estiver vazio
            
            altura = int(altura_str)
            peso = float(peso_str)

            imc = peso / ((altura / 100) ** 2) # Cálculo do IMC

            mensagem, cor_do_fundo = classificar_imc(imc) # Classificação do IMC
            
            resultado_text.value = mensagem # Atualizando o texto do resultado
            container_resultado.bgcolor = cor_do_fundo # Mudando a cor de fundo conforme a classificação

            page.update() # Atualizando a página para mostrar o resultado

        except ValueError:
            resultado_text.value = "Por favor, insira valores válidos."
            container_resultado.bgcolor = "grey"
            page.update()

    # Botão para calcular o IMC
    # características visuais do botão
    botão = ft.ElevatedButton(
        content=ft.Text("Calcular IMC"),
        color="white",
        bgcolor="blue",
        on_click=calcular_imc)
    
    # Container para o botão com margem superior
    calcular_button = ft.Container(
        content=botão,
        margin=ft.margin.only(top=20),
    )

    # Adicionando elementos à página
    page.add(
        titulo, 
        ft.Row([altura_input, peso_input], alignment="center"), 
        calcular_button,
        ft.Divider(), 
        ft.Container(
            content=container_resultado,
            width=400,
            padding=20,
            border_radius=10,
            bgcolor="lightgrey"
        )
    )
# --- 4. Execução do Programa ---
ft.app(target=main)
