from src.main import main
from src.tools.tools_get_news import Tools
from src.api.test_api import Test_API

api_test = Test_API()
tools = Tools()
print(10*"---")
print("""
    [1] Newsletter
    [2] Scraper News
    [3] Test API
    [3] Sair
    ----------->
                by Jemison
""")
print(10*"---")
def main():
    while True:
        select = input("Digite sua opção: \n1 - News\n2 - Scraper\n3 - Test\n")

        if select == "1" or select == "News":
            # Add code for the News option here
            pass
        elif select == "2" or select == "Scraper":
            tools
        elif select == "3" or select == "Test":
            api = input("Digite a api para testa: \nApi:")
            test_api_connection(api)
        else:
            print("Opção inválida, tente novamente.")
            continue

if __main__ == "__main__":
    main()