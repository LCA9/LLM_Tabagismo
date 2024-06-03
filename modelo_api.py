from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
import os
from openai import OpenAI
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import OpenAIEmbeddings
#uvicorn modelo_api:app --reload


app = FastAPI()
load_dotenv()
client = OpenAI(api_key=os.getenv('API_KEY'))
openai = OpenAIEmbeddings(openai_api_key=os.getenv('API_KEY'))

#realiza validação se o valor recebido pela função assincrona responde_tabaco é do tipo str
class reponde_tabaco_Request(BaseModel):
  text: str


def faiss_load(query):
  vector_db = FAISS.load_local("store_path", openai)
  docs = vector_db.similarity_search(query)
  return docs


@app.post("/resposta/")
async def responde_tabaco(resposta: reponde_tabaco_Request):

  text = resposta.text
  context = faiss_load(resposta.text)

  completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "Sua funcao e responder a PERGUNTA DO MEDICO sobre o protocolo de tratamento dotabagismo, com base no documento disponibilizado pelo INCA (Instituto Nacional de Câncer).As respostas devem ser concisas, resumidas. Nao invente resposta, responda a pergunta de acordo com o CONTEXTO fornecido. \n\nCONTEXTO:" + context[0].page_content},
    {"role": "user", "content": "\n\nPERGUNTA DO MEDICO:"+text}
  ])

  vr = completion.choices[0].message.content
  return {"text": vr}




"""if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)"""