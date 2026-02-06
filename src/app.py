import streamlit as st
import time
import pandas as pd
import pickle

@st.cache_resource
def load_model():
    with open("../model/model.pkl", "rb") as f:
        return pickle.load(f)

model = load_model()


st.title("Gymselyk")
st.markdown("""
    #### Em busca do treino perfeito
            
    Preencha o formulário com seus dados:
""")


with st.form("form_aluno"):
    nome = st.text_input("Nome")

    col1, col2 = st.columns(2)

    with col1:
        sexo = st.selectbox("Sexo", ["Selecione", "M", "F"], index=0)
        idade = st.number_input("Idade", min_value=14, max_value=100)
        peso = st.number_input("Peso (kg)", min_value=40.0, max_value=200.0)

    with col2:
        nivel = st.selectbox(
            "Nível",
            ["Selecione", "Iniciante", "Intermediário", "Avançado"],
            index=0
        )
        altura = st.number_input("Altura (cm)", min_value=100, max_value=250) / 100
        dias_disponiveis = st.selectbox("N° dias disponível", ["3", "4", "5", "6"])

    tempo = st.slider("Tempo mínimo disponível", min_value=45, max_value=90)

    enviar = st.form_submit_button("Enviar Dados")

if enviar:
    novo_aluno = pd.DataFrame([{
        "sexo": sexo,
        "idade": idade,
        "peso": peso,
        "altura": altura,
        "nivel": nivel,
        "dias_disponiveis": dias_disponiveis,
        "tempo_disponivel": tempo
        }])
    
    predict = model.predict(novo_aluno)

    st.success(f"Seu split ideal é: {predict[0]}")
    
    
