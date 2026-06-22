from fastmcp import FastMCP

# initialize MCP server
mcp = FastMCP(
    name="pixelle-mcp-server",
    on_duplicate="replace",
)
