from mcp.server.fastmcp import FastMCP
from agents import run_research
import os

# Initialize the MCP Server
# "dependencies" tells the client (VS Code) what python libraries to install if it manages the environment
mcp = FastMCP("Deep Researcher", dependencies=["crewai", "linkup-sdk", "python-dotenv"])

@mcp.tool()
def research_topic(topic: str) -> str:
    """
    Performs deep internet research on a specific topic using AI agents.
    
    Args:
        topic: The subject to research (e.g., "Latest trends in AI 2025")
    """
    try:
        # Ensure the key is loaded
        if not os.getenv("LINKUP_API_KEY"):
            return "Error: LINKUP_API_KEY not found in environment variables."
            
        return run_research(topic)
    except Exception as e:
        return f"Research failed: {str(e)}"

# Run the server using stdio (Standard Input/Output)
if __name__ == "__main__":
    mcp.run(transport="stdio")