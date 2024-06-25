from textwrap import dedent
from crewai import Agent
from langchain_openai import ChatOpenAI
import os
from langchain_openai import AzureChatOpenAI
from dotenv import load_dotenv
load_dotenv()
class GameAgents():
    def __init__(self):
        self.llm = AzureChatOpenAI(
            openai_api_version = "2024-05-01-preview",
            azure_deployment=os.getenv("AZURE_OPENAI_DEPLOYMENT"),
            azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
            api_key = os.getenv("AZURE_OPENAI_API_KEY")
            
        )

    def senior_engineer_agent(self):
        return Agent(
            model=os.getenv('MODEL'),
            role='Senior Software Engineer',
            goal='Create software as needed',
            backstory=dedent("""\
				You are a Senior Software Engineer at a leading tech think tank.
				Your expertise in programming in python. and do your best to
				produce perfect code"""),
            allow_delegation=False,
            verbose=True,
            llm=self.llm
        )

    def qa_engineer_agent(self):
        return Agent(
             model=os.getenv('MODEL'),
            role='Software Quality Control Engineer',
            goal='create prefect code, by analizing the code that is given for errors',
            backstory=dedent("""\
				You are a software engineer that specializes in checking code
  			for errors. You have an eye for detail and a knack for finding
				hidden bugs.
  			You check for missing imports, variable declarations, mismatched
				brackets and syntax errors.
  			You also check for security vulnerabilities, and logic errors"""),
            allow_delegation=False,
            verbose=True,
            llm=self.llm
        )

    def chief_qa_engineer_agent(self):
        return Agent(
            model=os.getenv('MODEL'),
            role='Chief Software Quality Control Engineer',
            goal='Ensure that the code does the job that it is supposed to do',
            backstory=dedent("""\
				You feel that programmers always do only half the job, so you are
				super dedicate to make high quality code."""),
            allow_delegation=True,
            verbose=True,
            llm=self.llm
        )
