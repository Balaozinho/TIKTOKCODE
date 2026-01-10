#IMPORTAR BIBLIOTECAS
from langchain_openai import ChatOpenAI
from dotenv import find_dotenv, load_dotenv

load_dotenv()

#CARREGAR MODELO
llm = ChatOpenAI(model="gpt-4o-mini")

#INTERAGIR COM MODELO
resposta = llm.invoke("Explique o que é empreendedorismo para uma criança de 12 anos")

#IMPRIMIR RESPOSTA
print(resposta.content)
