from crewai import Crew, Process
from src.agents.agents import Agents
from src.tasks.tasks import Tasks
from src.tools.tools_get_news import Tools
from src.utils.format_markdown import FormatDocs


def main():
    # Ferramentas

    tools = Tools()

    # Agentes
    agents = Agents()
    writer_agent = agents.writer()
    ir_expert_agent = agents.international_relations_expert()
    economist_agent = agents.economic_analyst()
    tech_advocate_agent = agents.technology_advocate()
    crypto_expert_agent = agents.cryptocurrency_expert()
    
    # Tarefas
    tasks = Tasks()
    ir_research_task = tasks.international_relations_task(ir_expert_agent)
    initial_evaluation_task = tasks.economics_task(economist_agent)
    tech_research_task = tasks.technology_task(tech_advocate_agent)
    crypto_research_task = tasks.crypto_task(crypto_expert_agent)
    writing_task = tasks.create_content_task(writer_agent)
    revision_task = tasks.review_content_task(writer_agent)
    final_evaluation_task = tasks.rewrite_content_task(writer_agent)
    public_task = tasks.publish_content_task(writer_agent)

    # Criar e iniciar a equipe
    crew = Crew(
        agents=[
            writer_agent,
            ir_expert_agent,
            economist_agent,
            tech_advocate_agent,
            crypto_expert_agent
        ],
        tasks=[
            ir_research_task,
            initial_evaluation_task,
            tech_research_task,
            crypto_research_task,
            writing_task,
            final_evaluation_task,
            revision_task
        ],
        verbose=False,
        process=Process.sequential  # Considere ajustar para Process.parallel onde aplicável
    )
    result = crew.kickoff()
    print(result)

main()