# News Agents

The idea behind this project is to create a newsletter team that researches, creates, formats, and reviews content based on automated document scraping and formatting.

## Features

- [x] Create Agent Diagram for research
- [x] Research
- [x] Format Research
- [x] Save Research
- [x] Retrieve Research
- [ ] Perform Embeddings
- [ ] Create Agents to interact with research data
- [x] Save research and retrieve data
- [ ] Create blacklist
- [ ] Proxy system
- [ ] Create a Telegram chatbot to receive selected articles

## Exclusion List Websites

Some websites are ignored during news scraping due to the nature of their elements. They are:

- www.metropoles.com
- g1.globo.com
- dinheirama.com
- valor.globo.com
- www.terra.com.br
- www.viomundo.com.br
- sputniknewsbr.com.br
- www.bbc.com
- www.infomoney.com.br

## Future Improvements

Using agents asynchronously to automate the collection of articles.

## Used Stack

**Back-end:**
- crewai
- requests
- langchain_google_genai
- langchain_community
- python-dotenv
- langchain-chroma
- pyTelegramBotAPI
- "unstructured[md]"

## Environment Variables

To run this project, you need to set the following environment variables in your `.env` file:

- `NEWS_API_KEY`
- `GOOGLE_API_KEY`

Sites to get the API keys:
- [Gemini Pro](https://ai.google.dev/)
- [text](https://newsapi.org/)

## Running Locally

Clone the repository:

```bash
git clone https://link-to-the-project
```

Navigate to the project directory:

```bash
cd my-project
```

Activate the virtual environment:

```bash
./Scripts/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Start the server:

```bash
python main.py
```
