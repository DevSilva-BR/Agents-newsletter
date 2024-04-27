import os
from langchain_community.document_loaders import UnstructuredFileLoader
import logging
import datetime

class FormatDocs:
    """
    Método para formatar o conteúdo em markdown e salvar em arquivo.
    """
    def __init__(self, persist_directory: str ="../../src/data"):
        """
        Initialize with the directory where articles will be saved.
        """
        self.persist_directory = os.path.join(persist_directory)
        self.ensure_directory_exists()
        self.logger = logging.getLogger(__name__)

    def ensure_directory_exists(self) -> None:
        """Ensures the persistent directory exists."""
        # Ensure the directory exists
        # This is the primary public method of this class, so check for all potential issues
        if self.persist_directory is None:
            raise ValueError("Directory cannot be None.")
        # Check for unhandled exception
        try:
            os.makedirs(self.persist_directory, exist_ok=True)
        except FileNotFoundError as e:
            raise RuntimeError(f"Failed to create directory {self.persist_directory}: {e}")


    def format_to_markdown(self, articles: list[dict]) -> str:
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

    def save_articles(self, articles: list[dict]) -> str:
        """
        Saves the given articles in markdown format to a file.
        Args:
            articles (list[dict]): A list of dictionaries representing articles.

        Returns:
            str: A message indicating success or failure of saving the data.
        """
        date_atual = datetime.datetime.now()
        date = date_atual.strftime("%d-%m-%Y")
        markdown_content = self.format_to_markdown(articles)
        file_path = os.path.join(self.persist_directory, date + ".md")
        
        try:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(markdown_content)
            return f"Data successfully saved to {file_path}"
        except Exception as e:
            self.logger.error(f"An error occurred while saving articles: {e}")
            return "Failed to save articles."

    def load_context(self) -> str:
        """
        Loads and concatenates the content of the data file (src/data).
        """
        context = []
        try:
            loader = UnstructuredFileLoader(os.path.join(self.persist_directory, "data.md"))
            documents = loader.load()
            for doc in documents:
                context.append(doc.page_content)
            all_context = '\n'.join(context)
            self.logger.info(f"Contexto carregado com sucesso de '{self.persist_directory}'.")
            return all_context
        except FileNotFoundError as e:
            self.logger.error(f"Error: File not found: {e}")
            return None
        except Exception as e:
            self.logger.error(f"An unexpected error occurred: {e}")
            return None