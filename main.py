from typing import Any
import os
from mcp.server.fastmcp import FastMCP
from pydo import Client
from dotenv import load_dotenv

load_dotenv()

access_token = os.getenv("DIGITALOCEAN_ACCESS_TOKEN")

client = Client(token=access_token)

get_resp = client.apps.list()

mcp = FastMCP("digitalocean")

@mcp.tool()
def get_apps(state: str) -> str:
    """Get all digital ocean apps.
    """
    data = client.apps.list()

    return data


if __name__ == "__main__":
    print("Starting digital ocean server...")

    mcp.run(transport='stdio')