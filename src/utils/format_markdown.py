import os
from langchain_community.document_loaders import UnstructuredFileLoader

class FormatDocs:
    """
    Método para formatar o conteúdo em markdown e salvar em arquivo.
    """
    def __init__(self, persist_directory="../data"):
        """
        Initialize with the directory where articles will be saved.
        """
        self.persist_directory =  persist_directory
        self.ensure_directory_exists()

    def ensure_directory_exists(self):
        """Ensures the persistent directory exists."""
        os.makedirs(self.persist_directory, exist_ok=True)

    def format_to_markdown(self, articles):
        """
        Formats a list of article dictionaries into markdown text.
        """
        markdown_content = []
        for article in articles:
            markdown_content.append(f"## {article.get('title', 'No Title Provided')}\n")
            markdown_content.append(f"**Author:** {article.get('author', 'Unknown')}\n")
            markdown_content.append(f"**Published At:** {article.get('publishedAt', 'No Date Provided')}\n")
            markdown_content.append(f"**Source:** {article.get('source', {}).get('name', 'Unknown')}\n")
            markdown_content.append(f"**URL:** [Link]({article.get('url', '#')})\n")
            markdown_content.append(f"**Content:**\n{article.get('content', 'No content available')}\n")
            markdown_content.append("---\n")
        return '\n'.join(markdown_content)

    def save_data(self, articles):
        """
        Saves the given articles data in markdown format to a file.
        """
        markdown_content = self.format_to_markdown(articles)
        
      
        # Especifica o caminho completo para o arquivo data.md
        file_path = os.path.join(self.persist_directory, "data.md")
        
        try:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(markdown_content)
            return f"Data successfully saved to {file_path}"
        except Exception as e:
            return f"An error occurred while saving  {e}"

    def load_context(self):
        """
        Carrega e concatena o conteúdo de todos os documentos na pasta persistente usando UnstructuredFileLoader.
        """
        context = []
        try:
            # Garante que o diretório existe
            if not os.path.exists(self.persist_directory):
                print(f"O diretório '{self.persist_directory}' não foi encontrado.")
                return ""

            # Cria uma instância do loader e carrega os documentos
            loader = UnstructuredFileLoader(self.persist_directory)
            documents = loader.load()

            # Concatena o conteúdo de todos os documentos em uma única string
            for doc in documents:
                context.append(doc.page_content)

            all_context = '\n'.join(context)
            print(f"Contexto carregado com sucesso de '{self.persist_directory}'.")
            return all_context
        except Exception as e:
            print(f"Ocorreu um erro ao carregar o contexto de '{self.persist_directory}': {e}")
            return ""
        

result = FormatDocs()
rr = result.load_context()
print(rr)