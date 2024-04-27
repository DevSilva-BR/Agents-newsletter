import requests
userInput = input("digite sua pergunta: ")
headers = {
    'x-wormgpt-provider': 'worm_gpt',
    'Content-Type': 'application/json',
}

json_data = {
    'messages': [
        {
            'role': 'system',
            'content': "Como pesquisador experiente, você tem um sólido entendimento das tendências tecnológicas e um olhar crítico para detalhes. Você se destaca ao mergulhar nos últimos desenvolvimentos em IA e automação, identificando inovações-chave e aplicações práticas para empresas.", # question here
        },
        {
            'role':'user',
            'content':userInput
        }
    ],
    'max_tokens': 820,
}

response = requests.post('https://wrmgpt.com/v1/chat/completions', headers=headers, json=json_data)
print(response.json()['choices'][0]['message']['content'])