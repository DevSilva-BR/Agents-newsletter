
# Agentes News

Uma breve descrição sobre o que esse projeto faz e para quem ele é


## Funcionalidades
- [ ] cria Diagrama de agentes para pequisa 
- [x]  Pesquisa
- [x]  Formata Pesquisa
- [x] Salva Pesquisa
- [x] Recupera Pesquisa
- [ ] Realiza Embbedings
- [ ] Cria Agentes para interagia com os dados da pesquisa
- [x] Salva pesquisa e recupera dados
- [ ] cria blacklist
- [ ] sistema de proxy
- [ ] cria um chatbot no telegram para recebe os articlos pontos




## Sites de Lista de classes, IDs e seletores a serem ignorados na raspagem das noticias
      Website onde estão sendo ignorando os elementos.
        - www.metropoles.com
        - g1.globo.com
        - dinheirama.com
        - valor.globo.com
        - www.terra.com.br
        - www.viomundo.com.br
        - sputniknewsbr.com.br
        - www.bbc.com
        - www.infomoney.com.br

## Melhorias

Utiliza de forma assicrona os agentes para cria de forma automatica os articlos


## Screenshots



## Stack utilizada

**Back-end:** 
crewai 
requests 
langchain_google_genai 
langchain_community
requests
python-dotenv
langchain-chroma
pyTelegramBotAPI
"unstructured[md]"


## Variáveis de Ambiente

Para rodar esse projeto, você vai precisar adicionar as seguintes variáveis de ambiente no seu .env

`NEWS_API_KEY`

`GOOGLE_API_KEY`


sites para pega os token
- [Gemini Pro](https://ai.google.dev/)
- [text](https://newsapi.org/)

## Rodando localmente

Clone o projeto

```bash
  git clone https://link-para-o-projeto
```

Entre no diretório do projeto

```bash
  cd my-project
```
Ative o ambiente
```bash
  ./Scripts/activate
```

Instale as dependências

```bash
  pip install -r requeriments.txt
```

Inicie o servidor

```bash
  python main.py
```
