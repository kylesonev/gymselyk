import streamlit as st

pg_home = st.Page("pages/home.py", title="Treino Perfeito", default=True)
pg_creatina = st.Page("pages/creatina.py", title="Calculadora de Creatina")
pg_imc = st.Page("pages/imc.py", title="Cálculo de IMC")
pg_proteina = st.Page("pages/proteina.py", title="Meta de Proteína")
pg_tmb = st.Page("pages/calorias.py", title="Calorias")

pg = st.navigation(
    {
        "Principal": [pg_home],
        "Calculadoras Fitness": [pg_creatina, pg_imc, pg_proteina, pg_tmb],
    }
)

pg.run()
