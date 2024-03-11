from crewai import Task
from textwrap import dedent

class TasksNewsletter:
    def get_task_reddit_report(self,agent):
        return Task(
            description= dedent("""\
                Use and summarize scraped data from subreddit LocalLLama to make a detailed report on the latest
                rising projects in AI. Use ONLY scraped data from LocalLLama to generate the report. Your final answer
                MUST be a full analysis report, text only, ignore any code or anything that isn't text. The report has to
                have bullet points and with 5-10 exciting new AI projects and tools. Write names of every tool and project. 
                Each bullet point MUST contain 3 sentences that refer to one specific ai company, product, model or anything
                you found on subreddit LocalLLama.  
            """),
            agent=agent,
        )
    
    def get_task_google_report(self, agent):
        return Task(
            description=dedent("""\
                Use and summarize scraped data from the internet to make a detailed report on the latest rising
                projects in AI.Use ONLY scraped data to generate the report. Your final answer MUST be a full analysis
                report, text only, ignore any code or anything that isn't text. The report has to have bullet points and
                with 5-10 exciting new AI projects and tools. Write names of every tool and project. Each bullet point MUST
                contain 3 sentences that refer to one specific AI company, product, model or anything you found on the
                internet.
            """),
            agent=agent,
        )

    def get_task_blog(self,agent):
        return Task(
            description=dedent("""\
                Write a blog article with text only and with a short but impactful headline and at least 10 paragraphs.
                Blog should summarize the report on latest AI tools found on localLLama subreddit. Style and tone should be
                compelling and concise, fun, technical but also use layman words for the general public. Name specific new,
                exciting projects, apps and companies in AI world. Don't write "**Paragraph [number of the paragraph]:**",
                instead start the new paragraph in a new line. Write names of projects and tools in BOLD. ALWAYS include links
                to projects/tools/research papers. ONLY include information from LocalLLAma.
                For your Outputs use the following markdown format:
                    ## [Title of post](link to project)
                    - Interesting facts
                    - Own thoughts on how it connects to the overall theme of the newsletter
                    ## [Title of second post](link to project)
                    - Interesting facts
                    - Own thoughts on how it connects to the overall theme of the newsletter
            """),
            agent=agent,
        )
        
    def get_task_critique(self,agent):
        return Task(
            description= dedent("""\
                The Output MUST have the following markdown format:
                    ## [Title of post](link to project)
                    - Interesting facts
                    - Own thoughts on how it connects to the overall theme of the newsletter
                    ## [Title of second post](link to project)
                    - Interesting facts
                    - Own thoughts on how it connects to the overall theme of the newsletter
                Make sure that it does and if it doesn't, rewrite it accordingly.
            """),
            agent=agent,
        )
