import streamlit as st

# Título da aplicação
st.title("🧮 Calculadora Simples")

# Inputs do usuário
num1 = st.number_input("Digite o primeiro número", value=0.0)
num2 = st.number_input("Digite o segundo número", value=0.0)

# Seleção da operação
operacao = st.selectbox(
    "Escolha a operação",
    ("Soma", "Subtração", "Multiplicação", "Divisão")
)

# Botão de calcular
if st.button("Calcular"):
    if operacao == "Soma":
        resultado = num1 + num2

    elif operacao == "Subtração":
        resultado = num1 - num2

    elif operacao == "Multiplicação":
        resultado = num1 * num2

    elif operacao == "Divisão":
        if num2 == 0:
            st.error("❌ Não é possível dividir por zero")
            resultado = None
        else:
            resultado = num1 / num2

    # Exibe o resultado
    if resultado is not None:
        st.success(f"✅ Resultado: {resultado}")
