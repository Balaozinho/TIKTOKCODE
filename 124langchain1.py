#IMPORTANTO AS BIBLIOTECAS
from dotenv import find_dotenv, load_dotenv
from langchain.agents import initialize_agent, Tool
from langchain_openai import ChatOpenAI

load_dotenv()

#CRIANDO FUNCAO DA FERRAMENTA
def calculadora(texto):
    return str(eval(texto))

#CONFIGURANDO AS TOOLS
tools = [
    Tool(
        name="Calculadora",
        func=calculadora,
        description="Resolve contas matemáticas"
    )
]

#INICIANDO O MODELO
llm = ChatOpenAI(model="gpt-4o-mini")

#INICIANDO O AGENT
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent="zero-shot-react-description",
    verbose=True
)

#INVOCAR O AGENT
agent.invoke("Quanto é (200 * 3) + 150?")