import streamlit as st

st.set_page_config(page_title="Calculadora de Calorias", page_icon="🧮")

st.header("Calculadora de Calorias")

with st.form("calorias"):
    peso = st.slider("Peso (kg)", min_value=0.0, max_value=300.0, step=0.1)
    altura = st.slider("Altura (cm)", min_value=100, max_value=250) / 100
    idade = st.number_input("Idade", min_value=14, max_value=100)
    sexo = st.selectbox("Sexo", ["Selecione", "Masculino", "Feminino"], index=0)
    atividade = st.selectbox(
        "Nível de Atividade Física",
        [
            "Sedentário",
            "Levemente Ativo",
            "Moderadamente Ativo",
            "Muito Ativo",
            "Extremamente Ativo",
        ],
    )
    enviar = st.form_submit_button("Calcular")

    def calcular_taxa_basal(peso: float, altura: float, sexo: str) -> float | None:
        altura *= 100

        # Mifflin-St Jeor Fórmula
        if sexo == "Masculino":
            taxa_metabolica_basal = ((10 * peso) + (6.25 * altura)) - (5 * idade) + 5
            return taxa_metabolica_basal
        if sexo == "Feminino":
            taxa_metabolica_basal = ((10 * peso) + (6.25 * altura) - (5 * idade)) - 161
            return taxa_metabolica_basal
        return None

    def calcular_gasto_calorico(taxa_metabolica_basal, atividade: str) -> float | None:
        if atividade == "Sedentário":
            return taxa_metabolica_basal * 1.2
        elif atividade == "Levemente Ativo":
            return taxa_metabolica_basal * 1.375
        elif atividade == "Moderadamente Ativo":
            return taxa_metabolica_basal * 1.55
        elif atividade == "Muito Ativo":
            return taxa_metabolica_basal * 1.725
        elif atividade == "Extremamente Ativo":
            return taxa_metabolica_basal * 1.9

        return None

    if enviar:
        if peso and altura and idade and sexo and atividade:
            taxa_metabolica_basal = calcular_taxa_basal(peso, altura, sexo)
            gasto_calorico = calcular_gasto_calorico(taxa_metabolica_basal, atividade)

            st.info(f"Taxa Metabólica Basal: {taxa_metabolica_basal:.2f}")
            st.info(f"Gasto Calórico Total Diário: {gasto_calorico:.2f}")
