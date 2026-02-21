import streamlit as st
import pandas as pd
import pickle
from utils.config import set_page_config
from exercicios_lib import TREINOS


@st.cache_resource
def load_model():
    with open("../model/model.pkl", "rb") as f:
        return pickle.load(f)


model = load_model()

set_page_config(title="Gymselyk")
st.title("Gymselyk")
st.markdown("""
    #### Em busca do treino perfeito!
    Preencha o formulário com seus dados e obtenha seu Split ideal:
""")


with st.form("form_aluno"):
    nome = st.text_input("Nome")

    col1, col2 = st.columns(2)

    with col1:
        sexo = st.selectbox("Sexo", ["Selecione", "Masculino", "Feminino"], index=0)
        idade = st.number_input("Idade", min_value=14, max_value=100)
        peso = st.number_input("Peso (kg)", min_value=40.0, max_value=200.0)

    with col2:
        nivel = st.selectbox(
            "Nível", ["Selecione", "Iniciante", "Intermediário", "Avançado"], index=0
        )
        altura = st.number_input("Altura (cm)", min_value=100, max_value=250) / 100
        dias_disponiveis = st.selectbox("N° dias disponível", ["3", "4", "5", "6"])

    tempo = st.slider("Tempo mínimo disponível", min_value=45, max_value=90)

    enviar = st.form_submit_button("Enviar Dados")

if enviar:
    novo_aluno = pd.DataFrame(
        [
            {
                "sexo": sexo,
                "idade": idade,
                "peso": peso,
                "altura": altura,
                "nivel": nivel,
                "dias_disponiveis": dias_disponiveis,
                "tempo_disponivel": tempo,
            }
        ]
    )

    predict = model.predict(novo_aluno)
    split_id = predict[0]

    st.success(f"Split ideal é: **{split_id}**")
    st.divider()

    if split_id in TREINOS:
        planilha = TREINOS[split_id]
        st.subheader("Planilha de Treino")

        titulos_abas = st.tabs(list(planilha.keys()))

        for i, dia in enumerate(planilha.keys()):
            with titulos_abas[i]:
                df_planilha = pd.DataFrame(planilha[dia])

                if "Day Off" in df_planilha["ex"].values:
                    st.info("Dia de descanso! Recupere suas energias.")
                else:
                    df_exibir = df_planilha[["ex", "sets"]].copy()
                    df_exibir.columns = ["Exercício", "Séries/Reps"]

                    st.dataframe(df_exibir, use_container_width=True, hide_index=True)

                    st.markdown("#### Vídeos de Execução")

                    for i, row in df_planilha.iterrows():
                        video_url = row.get("video")

                        with st.expander(f"{row['ex']}"):
                            if str(video_url).lower().endswith(
                                ".gif"
                            ) or "giphy" in str(video_url):
                                st.image(video_url, use_container_width=True)
                            else:
                                st.video(video_url)
    else:
        st.warning(
            "Split recomendado, mas exercícios ainda não cadastrados na biblioteca."
        )
