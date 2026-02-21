import plotly.graph_objects as go
import streamlit as st
from utils.config import set_page_config


set_page_config(title="Calculadora de Proteína")

st.header("Meta de Proteína Diária")

with st.form("proteina_calc"):
    peso = st.slider("Peso (kg)", min_value=0.0, max_value=300.0, step=0.1)
    quantidade = peso * 2
    enviar = st.form_submit_button("Calcular")

    if enviar:
        st.metric(
            "Dose Diária",
            f"{quantidade:.2f}g",
            help="Baseado em 2g por kg de peso corporal",
        )

        fig = go.Figure(
            data=go.Bar(
                x=["Proteína"],
                y=[quantidade],
                text=[f"{quantidade:.2f}g"],
                textposition="outside",
                textfont=dict(size=28, color="white"),
                marker=dict(
                    color="red", line=dict(color="white", width=4), opacity=0.9
                ),
                width=0.2,
                hovertemplate="<b>Dose:</b> %{y:.2f}g<extra></extra>",
            )
        )

        fig.update_layout(
            height=450,
            paper_bgcolor="#0E1117",
            plot_bgcolor="#0E1117",
            yaxis=dict(
                title=dict(text="Quantidade (gramas)", font=dict(size=18)),
                gridcolor="rgba(255,255,255,0.1)",
                range=[0, 400],
            ),
            xaxis=dict(tickfont=dict(size=16, color="white")),
            showlegend=False,
            margin=dict(t=50, b=50, l=60, r=60),
        )

        st.plotly_chart(fig, use_container_width=True)
