from crewai import Task 
from src.utils.format_markdown import FormatDocs

file = FormatDocs()
r = file.load_context()
print(r)
class Tasks:
    # def __init__(self):
        # self.ferramentas = FormatDocs().load_context()

    def international_relations_task(self, agent):
        return Task(
            description="""
                Realize pesquisas aprofundadas sobre os principais eventos e desenvolvimentos relacionados a relações internacionais, política externa e conflitos globais na última semana. Colete notícias, análises e dados relevantes que possam informar os leitores sobre esses tópicos.
            """,
            expected_output='Um relatório detalhado com os principais insights e informações sobre relações internacionais, política externa e conflitos globais.',
            agent=agent
        )

    def economics_task(self, agent):
        return Task(
            description="""
                Investigue os desenvolvimentos econômicos mais significativos no Brasil na última semana, incluindo atualizações sobre o governo, reformas, mercado financeiro, inflação, taxas de juros e exportações. Colete dados, notícias e análises para informar uma visão abrangente da situação econômica atual.
            """,
            expected_output='Um relatório abrangente sobre os principais eventos e tendências econômicas no Brasil, com foco em tópicos como governo, reformas, mercados financeiros e comércio exterior.',
            agent=agent
        )

    def technology_task(self, agent):
        return Task(
            description="""
                Pesquise os avanços e notícias mais recentes relacionados à inovação tecnológica, inteligência artificial e startups brasileiras. Identifique desenvolvimentos importantes, novos produtos ou serviços, e tendências emergentes que possam interessar aos leitores.
            """,
            expected_output='Um relatório destacando os principais avanços e tendências em tecnologia, IA e startups brasileiras na última semana.',
            agent=agent
        )
        
    def crypto_task(self, agent):
        return Task(
            description="""
                Realize uma análise aprofundada do mercado de criptomoedas, com foco especial no Bitcoin. Colete dados sobre preços, volatilidade, adoção, regulamentação e outras notícias relevantes que possam impactar os investidores e entusiastas de criptomoedas.
            """,
            expected_output='Um relatório detalhado sobre as últimas tendências e desenvolvimentos no mercado de criptomoedas, especialmente relacionados ao Bitcoin.',
            agent=agent
        )
        
    def create_content_task(self, agent):
        return Task(
            description=f"""
                Pesquise e colete informaçõe {r}, como relações internacionais, economia, tecnologia ou criptomoedas. Utilize fontes confiáveis para extrair dados, notícias e análises recentes.
            """,
            expected_output='Um rascunho inicial do conteúdo que inclui pontos principais, dados relevantes e uma breve descrição de cada seção do artigo.',
            agent=agent
        )
    
    def review_content_task(self, agent):
        return Task(
            description="""
                Revise o rascunho inicial , verificando a acurácia das informações, a relevância do conteúdo e a clareza da exposição. Ajuste o texto para melhorar sua fluência e impacto no leitor.
            """,
            expected_output='Um rascunho revisado que endereça os feedbacks iniciais e melhora aspectos como clareza, coesão e profundidade da análise.',
            agent=agent
        )
    
    def rewrite_content_task(self, agent):
        return Task(
            description="""
                Refine o texto , incorporando feedback adicional e ajustando o estilo de escrita para alinhar com o tom e a voz da publicação. Foque em enriquecer o conteúdo com insights valiosos e citações relevantes.
            """,
            expected_output='Um texto final, revisado e polido, pronto para publicação. Deve refletir um entendimento profundo do tópico e apresentar uma narrativa coesa e engajante.',
            agent=agent
        ) 

    def publish_content_task(self, agent):
        return Task(
            description="""
                Prepare o texto final para publicação, incluindo a finalização do título, autor, data e fontes. Certifique-se de que o conteúdo está formatado corretamente para os diferentes canais de distribuição.
            """,
            expected_output='Um artigo pronto para publicação, com todas as informações necessárias, como título, autor, data e fontes claramente identificados. Inclui um resumo que captura a essência do artigo em poucas palavras.',
            agent=agent
        )