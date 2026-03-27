
import os
from google.adk.agents import LlmAgent
from google.adk.tools.mcp_tool import McpToolset
from google.adk.tools.mcp_tool.mcp_session_manager import StdioConnectionParams
from mcp import StdioServerParameters

"""
File Reader Assistant Agent
Demonstrates MCP tools integration with ADK using the filesystem MCP server.

Reference: https://google.github.io/adk-docs/tools-custom/mcp-tools/
"""

# Get the absolute path of the folder containing agent.py
script_dir = os.path.dirname(os.path.abspath(__file__))


#. Point to the my_files folder inside that specific directory
ALLOWED_PATH = os.path.join(script_dir, "my_files")

# Create the folder if it doesn't exist
os.makedirs(ALLOWED_PATH, exist_ok=True)

# Create the agent with MCP filesystem tools
root_agent = LlmAgent(
    model='gemini-2.5-flash',
    name='file_reader_assistant',
    description='Helps users read and explore files using MCP tools.',
    instruction="""
You are a file reader assistant that helps users explore files.

Your capabilities:
 - List files in directories using list_directory
 - Read file contents using read_file

When helping users:
1. Use list_directory to show available files
2. Use read_file to display file contents when asked
3. Describe what you find in a helpful way

Always be clear about which folder you're working with.
""",
    tools=[
        McpToolset(
            connection_params=StdioConnectionParams(
                server_params=StdioServerParameters(
                    command='npx',
                    args=[
                        '-y',
                        '@modelcontextprotocol/server-filesystem',
                        ALLOWED_PATH,
                    ],
                ),
            ),
            # Filter to only expose safe, read-only tools
            tool_filter=['list_directory', 'read_file'],
        )
    ],
)
