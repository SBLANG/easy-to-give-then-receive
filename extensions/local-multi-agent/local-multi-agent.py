from crewai import Agent, Task, Crew, LLM
from langchain_community.chat_models.ollama import ChatOllama
import os

# Create model running on local host per README.md install instructions
llm = LLM(model="ollama_chat/llama3.1", base_url="http://localhost:11434")

# Create prompt
prompt = """what is the status quo of international efforts towards increasing equality and improving 
            access to opportunities, and what evidence is recorded in academic and scientific literature, 
            including geospatial studies."""

# Create a writing agent
general_agent = Agent(
    role="Writer",
    backstory="""You are a writer who is a master in business writing about topical
                subjects in current affairs and human development in great breadth and depth.
              """,
    goal="Articulate a comprehensive article to an audience who might not be familiar with your content.",
    llm=llm,
    verbose=True,
    allow_delegation=False,
)

# Create a researching agent
researcher = Agent(
    role="Researcher",
    backstory="""You are a highly-skilled researcher using quantitative research and spatial data analysis
                to review academic and scientific articles. You are excellent at aggregating historical facts 
                and important debates, including recent advancements in a subject area.
              """,
    goal="list historical facts, important debates and recent advancements in a subject area.",
    llm=llm,
    verbose=True,
    allow_delegation=False,
)

# Define the task for the researching agent to create lists of facts, debates, and advancements
researching_task = Task(
    description=f"""list facts, important debates, and recent advancements 
                    in the selected topic: {prompt}.
                    """,
    agent=researcher,
    expected_output="Facts, Important Debates and Recent Advancements.",
)

# Define the task for the writing agent to author an article based on the research inputs
writing_task = Task(
    description=f"""Based on the input from the research conducted, 
                    write an article about {prompt}.
                    """,
    agent=general_agent,
    expected_output="an article that is more than 100 words and less than 300 words",
)

# Create a crew with agents and tasks, and kick off the crew
crew = Crew(agents=[general_agent, researcher], tasks=[researching_task, writing_task], verbose=True)

# Initiate the workflow and receive the output
result = crew.kickoff()

# Print the output
print(result)