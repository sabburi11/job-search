from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from crewai_tools import SerperDevTool
from crewai.knowledge.source.pdf_knowledge_source import PDFKnowledgeSource
from pydantic import BaseModel, Field
# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

#pdf_source = PDFKnowledgeSource(file_paths=["resume.pdf"])
class Jobs(BaseModel):
    title: str = Field(description="Title of job")
    location: str = Field(description="Where is this job")
    job_type: str = Field(description="Type of job. For example: Entry level, Internship, etc")
    link: str = Field(description="URL for job posting")
    skills: str = Field(description="List of skills needed for job seperated by commas and space")
    salary: str = Field(description="The amount of money you get from working in the job")
class JobsList(BaseModel):
    list_of_jobs: list[Jobs] = Field(description="List of jobs that might suit user")
class Review(BaseModel):
    title: str = Field(description="Title of job. PLEASE MAKE SURE THE title OF THE REVIEW MATCHES THE title OF THE JOB EXACTLY")
    reason: str = Field(description="Reason for whether this job is a good fit or not")
    score: int = Field(description="Number between 1 and 100 representing how much the job fits the user. 100 is the best(meaning the job is a perfect fit) and 1 is the worst(the user should not do this job)")
    reccomendation: str = Field(description="Reccomendation for what to improve so user can be more suited for this job next time")
class ReviewList(BaseModel):
    reviews: list[Review] = Field(description="List of reviews for each job")


@CrewBase
class JobSearch():
    """JobSearch crew"""

    agents: list[BaseAgent]
    tasks: list[Task]
    # Learn more about YAML configuration files here:
    # Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
    # Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
    
    # If you would like to add tools to your agents, you can learn more about it here:
    # https://docs.crewai.com/concepts/agents#agent-tools
    @agent
    def job_search(self) -> Agent:
        return Agent(config=self.agents_config['job_search'], tools=[SerperDevTool()])
    
    @agent
    def match_analysis(self) -> Agent:
        return Agent(config=self.agents_config['match_analysis'], tools=[SerperDevTool()])

    @agent
    def report_writer(self) -> Agent:
        return Agent(config=self.agents_config['report_writer'])

    # To learn more about structured task outputs,
    # task dependencies, and task callbacks, check out the documentation:
    # https://docs.crewai.com/concepts/tasks#overview-of-a-task
    @task
    def search_for_job(self) -> Task:
        return Task(config=self.tasks_config['search_for_job'], output_pydantic=JobsList)
    @task
    def match_job(self) -> Task:
        return Task(config=self.tasks_config['match_job'], output_pydantic=ReviewList)
    @task
    def write_report(self) -> Task:
        return Task(config=self.tasks_config['write_report'])

    @crew
    def crew(self) -> Crew:
        """Creates the JobSearch crew"""
        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
