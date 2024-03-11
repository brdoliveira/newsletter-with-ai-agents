from crewai import Process, Crew
from tasks import TasksNewsletter
from agents import AgentsNewsletter

tasks_newsletter = TasksNewsletter()
agent_newsletter = AgentsNewsletter()

# Agents
explorer_agent = agent_newsletter.get_explorer()
writer_agent = agent_newsletter.get_writer()
critic_agent = agent_newsletter.get_critic()

# Tasks
task_reddit_report = tasks_newsletter.get_task_reddit_report()
task_google_report = tasks_newsletter.get_task_google_report()
task_blog = tasks_newsletter.get_task_blog()
task_critique = tasks_newsletter.get_task_critique()

# Crew
reddit_crew = Crew(
    agents=[explorer_agent, writer_agent, critic_agent],
    tasks=[task_reddit_report, task_blog, task_critique],
    verbose=2,
    process=Process.sequential
)

google_crew = Crew(
    agents=[explorer_agent, writer_agent, critic_agent],
    tasks=[task_google_report, task_blog, task_critique],
    verbose=2,
    process=Process.sequential
)

# Result
reddit_result = reddit_crew.kickoff()
print(reddit_result)

google_result = reddit_crew.kickoff()
print(google_result)