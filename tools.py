import praw
import time

from langchain.agents import Tool
from langchain.agents import load_tools
from langchain.utilities import GoogleSerperAPIWrapper
from langchain.tools import tool

class ToolsNewsletter:
    def __init__(self):
        self.search = GoogleSerperAPIWrapper()
        self.human_tools = load_tools(["human"])
        
    @property
    def search(self):
        return self._search

    @property
    def search_tool(self):
        return self._search_tool

    def human_tools(self):
        return Tool(
            name="Scrape google searches",
            func=self.search.run,
            description="Useful for when you need to ask the agent to search the internet"
        )
    
    @tool("Scrape reddit content")
    def scrape_reddit(max_comments_per_post=7):
        """Useful to scrape a reddit content"""
        reddit = praw.Reddit(
            client_id="client-id",
            client_secret="client-secret",
            user_agent="user-agent",
        )
        subreddit = reddit.subreddit("LocalLLaMA")
        scraped_data = []

        for post in subreddit.hot(limit=12):
            post_data = {"title": post.title, "url": post.url, "comments": []}

            try:
                post.comments.replace_more(limit=0)  # Load top-level comments only
                comments = post.comments.list()
                if max_comments_per_post is not None:
                    comments = comments[:7]

                for comment in comments:
                    post_data["comments"].append(comment.body)

                scraped_data.append(post_data)

            except praw.exceptions.APIException as e:
                print(f"API Exception: {e}")
                time.sleep(60)  # Sleep for 1 minute before retrying

        return scraped_data