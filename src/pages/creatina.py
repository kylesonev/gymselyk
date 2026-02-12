import streamlit as st
import plotly.graph_objects as go

st.set_page_config(page_title="Calculadora de Creatina", page_icon="🧮")
st.header("Calculadora de Creatina")

with st.form("creatina_calc"):
    peso = st.slider("Peso (kg)", min_value=0.0, max_value=300.0, step=0.1)
    quantidade = peso * 0.06
    enviar = st.form_submit_button("Calcular")

    if enviar:
        st.metric(
            "Dose Diária",
            f"{quantidade:.2f}g",
            help="Baseado em 0.06g por kg de peso corporal",
        )

        fig = go.Figure(
            data=go.Bar(
                x=["Creatina"],
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

        fig.add_hline(
            y=3,
            line_dash="dot",
            line_color="yellow",
            annotation_text="Dose mínima (3g)",
            annotation_position="top right",
        )

        fig.update_layout(
            height=450,
            paper_bgcolor="#0E1117",
            plot_bgcolor="#0E1117",
            yaxis=dict(
                title=dict(text="Quantidade (gramas)", font=dict(size=18)),
                gridcolor="rgba(255,255,255,0.1)",
                range=[0, max(quantidade * 1.3, 6)],
            ),
            xaxis=dict(tickfont=dict(size=16, color="white")),
            showlegend=False,
            margin=dict(t=50, b=50, l=60, r=60),
        )

        st.plotly_chart(fig, use_container_width=True)
