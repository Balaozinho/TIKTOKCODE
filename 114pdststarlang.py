#IMPORTAR BIBLIOTECAS
import pandas as pd
import streamlit as st

#CARREGAR O DATAFRAME / ARQUIVO
df = pd.read_csv("github_trending_repos.csv")

#CALCULAR MEDIA POR LINGUAGEM
media_estrelas = (df.groupby("language")["stars"].mean().sort_values(ascending=False))

#CONFIGURAR STREAMLIT
st.header("MEDIA POR LINGUAGEM")
st.line_chart(media_estrelas)