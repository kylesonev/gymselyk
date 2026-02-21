import streamlit as st
import plotly.graph_objects as go
from utils.config import set_page_config


set_page_config(title="Calculadora de IMC")

with st.form("imc_calc"):
    peso = st.slider("Peso (kg)", min_value=0.0, max_value=200.0, step=0.1)
    altura = st.slider("Altura (cm)", min_value=100, max_value=250) / 100

    enviar = st.form_submit_button("Calcular")

    def calcular_imc(peso: float, altura: float):
        return peso / (altura**2)

    def gerar_categoria(imc: float) -> str | None:
        if imc <= 18.5:
            return "Abaixo do Peso"
        elif imc > 18.5 and imc <= 24.99:
            return "Peso Normal"
        elif imc > 25 and imc <= 29.99:
            return "Sobrepeso"
        elif imc > 30 and imc <= 34.99:
            return "Obesidade Grau I"
        elif imc > 35 and imc <= 39.99:
            return "Obesidade Grau II"
        elif imc >= 40:
            return "Obesidade Grau III"
        else:
            return None

    if enviar:
        if peso and altura:
            imc = calcular_imc(peso, altura)
            categoria = gerar_categoria(imc)
            fig = go.Figure(
                go.Indicator(
                    mode="gauge+number+delta",
                    value=imc,
                    domain={"x": [0, 1], "y": [0, 1]},
                    title={"text": categoria, "font": {"size": 24}},
                    delta={
                        "reference": 22,
                        "increasing": {"color": "red"},
                        "decreasing": {"color": "green"},
                    },
                    gauge={
                        "axis": {
                            "range": [10, 50],
                            "tickwidth": 1,
                            "tickcolor": "darkblue",
                        },
                        "bar": {"color": "black"},
                        "steps": [
                            {"range": [10, 18.5], "color": "#87CEFA"},
                            {"range": [18.5, 24.9], "color": "#90EE90"},
                            {"range": [24.9, 29.9], "color": "#FFD700"},
                            {"range": [29.9, 34.9], "color": "#FF6347"},
                            {"range": [34.9, 39.9], "color": "blue"},
                            {"range": [39.9, 50], "color": "yellow"},
                        ],
                        "threshold": {
                            "line": {"color": "red", "width": 4},
                            "thickness": 0.75,
                            "value": imc,
                        },
                    },
                )
            )

            fig.update_layout(height=400)
            st.plotly_chart(fig, use_container_width=True)
