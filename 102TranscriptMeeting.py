import openai
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())
client = openai.OpenAI()

#TRANSCRIÇÃO DE AUDIO
print("=== INICIANDO TRANSCRIÇÃO DO ÁUDIO ===")
audio = open('Audio Exemplo.m4a', 'rb')
transcricao = client.audio.transcriptions.create(
    model='whisper-1',
    file=audio,
    prompt="""Você é um assistente que me ajudará a desenvolver resumos de reuniões da empresa Galileu Escola de Negócios.

O fluxo de trabalho funcionará da seguinte forma: 

1. Você receberá um arquivo em formato mp3
2. Logo em seguida, irá transcrever o audio utilizando o Whisper
3. Além disso, irá compreender e organizar o conteúdo, retornando um texto estruturado""",
    response_format='text'  # Usando 'text' para pegar apenas o texto transcrito
)

#ARMAZENAR ESSE AUDIO
texto_transcrito = transcricao
print("=== TEXTO TRANSCRITO ===")
print(texto_transcrito)
print("\n" + "="*50 + "\n")

#CRIAREMOS UM AGENT PARA ORGANIZAR AS INFOS TRANSCRITAS
print("=== INICIANDO ORGANIZAÇÃO DO CONTEÚDO ===")
response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "Você é um especialista em organização de informações. Sua função é pegar textos transcritos de áudio e transformá-los em resumos organizados para empresas."},
        
        {"role": "user", "content": f"Pegue o texto abaixo, compreenda e organize o conteúdo, retornando um texto estruturado como se fosse um resumo para a empresa Grupo Gali:\n\n{texto_transcrito}"}
    ],
    temperature=1,
    max_tokens=1000
)

#MOSTRAR A RESPOSTA DO AGENT
resumo_estruturado = response.choices[0].message.content
print("=== RESUMO ===")
print(resumo_estruturado)