#importar bibliotecas
import pandas as pd
import streamlit as st

#carregar csv e criar dataframe
df = pd.read_csv("github_trending_repos.csv")

#numero de estrelas
stars = df[['repo_name', 'owner', 'stars']].sort_values(by='stars', ascending=False).head(10)

#configurar streamlit
st.header("REPOS x STARS")
st.dataframe(stars)