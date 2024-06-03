pip install -r requirements.txt

### Diretório fasapienv
Guarda os arquivos necessários para a criação do ambiente, contendo as bibliotecas e dependências necessárias para o projeto.

### Diretório store_path
Guarda os embeddings. Foi criado a partir do arquivo de ingestão.

### ingestao.ipynb
Faz a preparação (tratamentos) e ingestão dos dados na VectorStore (Faiss).

### modelo_api.py
Constrói a API com FastAPI e utiliza o modelo LLM da OpenAI GPT-3.5 e a vector store FAISS para retornar as respostas das perguntas.

### streamlit_app.py
Front-end da aplicação, utilizando Streamlit. Possui layout de chat conversacional, que tem o objetivo de responder perguntas médicas, usando o contexto e os documentos indexados. Durante a execução, recupera informações relevantes utilizando a VectorStore.

### Arquivo .env
Armazena variáveis de ambiente.

### Diretório Video
Possui um video de demostração do app, mostrando a interação entre o front-end(streamlit) com o back-end(Api).

### Configurações iniciais
Configure o diretório fastapi como o raiz (comando: "cd fastapi"), posteriormente inicie o ambiente da fastapi (comando: "fastapienv\Scripts\activate.bat"). Não é necessária a instalação do uvicorn, pois esta já foi realizada.

### Comando para funcinamento da aplicação
Comando para iniciar o funcionamento da API: uvicorn modelo_api.py:app --reload
Comando para iniciar o funcionamento do streamlit: streamlit run streamlit_app.py

posteriormente copie e cole no url do browser:http://localhost:8501/

Donwload arquivo fastenv, .env, e video: https://drive.google.com/file/d/1HduVakl0p-HdPWQnpYlQvZCDNdJbIjbW/view?usp=sharing

