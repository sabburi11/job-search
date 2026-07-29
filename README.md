# JobSearch Crew

Welcome to the JobSearch Crew project, powered by [crewAI](https://crewai.com). This agent will be able to generate a list of jobs that will suit your skills according to your resume and the job you want.

## How To Use

1. Type in the job title you are looking for
2. Upload a PDF of your resume
3. The agent should generate a report on what jobs are available to apply to

## Frameworks

 - CrewAI
 - Gradio
 - OpenAI api

## Installation

Ensure you have Python >=3.10 <3.14 installed on your system. This project uses [UV](https://docs.astral.sh/uv/) for dependency management and package handling, offering a seamless setup and execution experience.

First, if you haven't already, install uv:

```bash
pip install uv
```

Next, navigate to your project directory and install the dependencies:

(Optional) Lock the dependencies and install them by using the CLI command:
```bash
crewai install
```
### Customizing

**Add your `OPENAI_API_KEY` into the `.env` file**

- Modify `src/job_search/config/agents.yaml` to define your agents
- Modify `src/job_search/config/tasks.yaml` to define your tasks
- Modify `src/job_search/crew.py` to add your own logic, tools and specific args
- Modify `src/job_search/main.py` to add custom inputs for your agents and tasks

## Running the Project

To run the project, run app.py. This will open a gradio server for the project. Additionally, job_report.md will be made containing the report in markdown. 


