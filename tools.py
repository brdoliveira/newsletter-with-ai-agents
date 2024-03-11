from langchain.agents import Tool
from langchain.agents import load_tools
from langchain.utilities import GoogleSerperAPIWrapper

class ToolsNewsletter:
    def __init__(self):
        self.search = GoogleSerperAPIWrapper()
        self.search_tool = Tool(
            name="Scrape google searches",
            func=self.search.run,
            description="Useful for when you need to ask the agent to search the internet"
        )
        self.human_tools = load_tools(["human"])
        
    @property
    def search(self):
        return self._search

    @property
    def search_tool(self):
        return self._search_tool

    @property
    def human_tools(self):
        return self._human_tools