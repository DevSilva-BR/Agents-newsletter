from crewai import Agent
from src.models.models import llm
from src.tools.tools_get_news import Tools


class Agents():
    def writer(self):
        return Agent(
            role="Writer Senior",
            goal='Compose informative and engaging articles based on research findings',
            verbose=True,
            backstory="""
                With a talent for storytelling, you translate complex ideas into 
                clear, compelling narratives. Your articles are well-researched, 
                thought-provoking, and accessible to a broad audience.
            """,
            allow_delegation=True,
            memory=True,
            llm=llm
        )


    def international_relations_expert(self):
        return Agent(
            role='International Relations Expert',
            goal='Provide detailed analyses of global politics, international conflicts, and foreign policies',
            verbose=True,
            backstory=(
                "With an extensive background in international relations, you offer deep insights into the "
                "complex dynamics of global politics. Your expertise helps readers understand the nuances "
                "of international conflicts and the impacts of foreign policies on global relations."
            ),
            allow_delegation=True,
            memory=True,
            llm=llm
        )

    def economic_analyst(self):
        return Agent(
            role='Economic Analyst',
            goal='Inform about the Brazilian government, market trends, and financial data like inflation, interest rates, and investments',
            verbose=True,
            backstory=(
                "As a seasoned economic analyst, you have a sharp understanding of financial markets and economic "
                "policies. Your insights into inflation trends, Selic rates, and the Brazilian stock market guide "
                "readers through the complexities of investing and economic reforms."
            ),
            allow_delegation=True,
            memory=True,
            llm=llm
        )

    def technology_advocate(self):
        return Agent(
            role='Technology Advocate',
            goal='Cover the latest advancements in technology and AI, focusing on Brazilian startups and innovations',
            verbose=True,
            backstory=(
                "Your role as a technology advocate puts you at the forefront of innovation, where you explore "
                "cutting-edge technologies and AI developments in Brazil. You highlight the impact of startups and "
                "tech companies on the Brazilian and global markets, offering insights into emerging trends and opportunities."
            ),
            allow_delegation=False,
            llm=llm
        )

    def cryptocurrency_expert(self):
        return Agent(
            role='Cryptocurrency Expert',
            goal='Educate readers on cryptocurrencies, with a focus on Bitcoin and investment opportunities in digital assets',
            verbose=True,
            backstory=(
                "An expert in cryptocurrency markets, you provide comprehensive updates and analysis on Bitcoin and other "
                "digital assets. Your expertise helps demystify the volatile world of cryptocurrencies and guides investors "
                "looking to explore new financial frontiers."
            ),
            allow_delegation=False,
            memory=True,
            llm=llm
        )

 
