import streamlit as st
from utils.config import set_page_config


set_page_config(title="Calculadora de Calorias")

st.header("Calculadora de Calorias")

st.markdown("""


A Taxa Metabólica Basal (TMB) é a quantidade mínima de calorias que o corpo necessita para manter funções vitais em repouso absoluto, como respiração, circulação e atividade cerebral. 

Representando cerca de 60% a 75% do gasto energético diário, a TMB é influenciada por idade, sexo, genética e composição corporal (mais músculos aumentam o gasto).

""")

st.markdown("""
##### Homens
$$
TMB = (10 * peso (kg)) + (6.25 * altura (cm)) - (5 * idade (anos)) + 5
$$

##### Mulheres
$$
TMB = (10 * peso (kg)) + (6.25 * altura (cm)) - (5 * idade (anos)) - 161
$$
""")

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
    st.markdown("""
    #### Cálculo Realizado
    """)
    if peso and altura and idade and sexo and atividade:
        taxa_metabolica_basal = calcular_taxa_basal(peso, altura, sexo)
        gasto_calorico = calcular_gasto_calorico(taxa_metabolica_basal, atividade)

        st.info(f"Taxa Metabólica Basal: {taxa_metabolica_basal:.2f}")
        st.info(f"Gasto Calórico Total Diário: {gasto_calorico:.2f}")

    st.markdown("""
    O gasto calórico diário é a quantidade total de energia que o corpo utiliza ao 
    longo de um dia para manter suas funções vitais e realizar atividades. 
    Essa energia é medida em calorias (kcal) e varia de pessoa para pessoa.


    Fator de Atividade:

    * **Sedentário** (pouco ou nenhum exercício): TMB * 1,2

    * **Levemente ativo** (exercício leve 1-3 dias/semana): TMB * 1,375

    * **Moderadamente ativo** (exercício moderado 3-5 dias/semana): TMB * 1,55

    * **Muito ativo** (exercício intenso 6-7 dias/semana): TMB * 1,99

    """)
