#IMPORTAR BIBLIOTECAS
import pandas as pd
import streamlit as st

#CRIAR O DATAFRAME CARREGANDO O ARQUIVO CSV
df = pd.read_csv("github_trending_repos.csv")

#FAZER CONTAGEM DE OCORRÊNCIAS
lang_counts = df['language'].value_counts()

#CONFIGURAR COMPONENTES DA STREAMLIT
st.title("MOST POPULAR LANGUAGES (2025)")
st.bar_chart(lang_counts)