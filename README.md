## Estrutura do Projeto

-   `controllers/`: Controladores FastAPI para diferentes serviços.
    -   `api/`: Controladores de API.
-   `services/`: Contém os serviços de backend para integração.
    -   `azureai/`: Serviços específicos para AzureAI.
    -   `openai/`: Serviços específicos para OpenAI.
-   `venv/`: Contém o ambiente virtual.
-   `.env`: Arquivo de variáveis de ambiente.
-   `main.py`: Arquivo principal de inicialização do Python
-   `requirements.txt`: Lista de dependências do Python.

## Configuração do Ambiente

1. Clone o repositório:

```powershell
git clone https://github.com/Alanbacha/ai-api
cd ai-api
```

2. Crie e ative um ambiente virtual:

```powershell
python -m venv env
env\Scripts\activate
```

3. Crie o arquivo .env na raiz do projeto e configure as variáveis de ambiente:

```env
OPENAI_API_KEY=your_openai_api_key
OPENAI_ASSISTANTS_API_KEY=your_openai_api_key
```

## Execução do Projeto

1. Construa os arquivos necessários:

```powershell
pip install -r requirements.txt
```

2. Inicie o servidor:

```powershell
python main.py
```

3. Acesse a aplicação em http://127.0.0.1:8001.
