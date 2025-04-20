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
def list_apps() -> str:
    """Get all digital ocean apps.
    """
    data = client.apps.list()

    return data

@mcp.tool()
def get_app(app_id: str, name: str) -> str:
    """Get a digital ocean app.

        Args:
            app_id: The id of the app to get.
            name: The name of the app to get.
    """
    data = client.apps.get(app_id=app_id, name=name)

    return data

@mcp.tool()
def list_app_deployments(app_id: str) -> str:
    """List an app's deployments.

        Args:
            app_id: The id of the app to list deployments for.
    """
    # There is a size limit on what Claude can digest, hence why we can't use
    # default per_page of 20.
    data = client.apps.list_deployments(app_id=app_id, per_page=5)

    return data

@mcp.tool()
def list_app_alerts(app_id: str) -> str:
    """List an app's alerts.

        Args:
            app_id: The id of the app to list alerts for.
    """
    data = client.apps.list_alerts(app_id=app_id)

    return data


if __name__ == "__main__":
    print("Starting digital ocean server...")

    mcp.run(transport='stdio')