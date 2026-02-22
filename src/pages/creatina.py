import streamlit as st
import plotly.graph_objects as go
from utils.config import set_page_config


set_page_config(title="Calculadora de Creatina")
st.header("Calculadora de Creatina")

st.markdown("""

A creatina é um composto de aminoácidos (glicina, arginina, metionina) produzido naturalmente pelo corpo e obtido na dieta, essencial para fornecer energia rápida aos músculos. 

É um dos suplementos mais eficazes para aumentar força, potência, hipertrofia muscular e melhorar a recuperação.

O cálculo é realizado da seguinte maneira:

Quantidade Diária = (peso corporal * 0,06)
___

""")

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

st.markdown("""

___ 

#### Principais Benefícios e Detalhes

* **Performance**: Melhora o desempenho em exercícios de alta intensidade e curta duração.

* **Ganho Muscular**: Auxilia no aumento de massa magra e força.

* **Efeito Cognitivo**: Estudos sugerem benefícios na função cerebral e redução de fadiga.

* **Segurança**: Considerada segura para a maioria das pessoas, não causa danos renais em indivíduos saudáveis.

* **Uso**: O efeito é por acúmulo, logo, deve ser consumida diariamente, inclusive em dias de descanso. Pode ser tomada antes ou após o treino.

* **Ganho de Peso**: Pode ocorrer um aumento de peso inicial devido à retenção de água intramuscular.




#### Dicas de Consumo

* **Como tomar**: Pode ser ingerida com água ou misturada a outras bebidas/suplementos.

* **Melhor Tipo**: A creatina monohidratada é a forma com melhor custo-benefício e mais estudada.


* **Marcas Populares**: Integralmedica, Max Titanium, Soldiers Nutrition e Dark Lab são algumas das marcas citadas.

""")
