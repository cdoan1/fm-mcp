from fastmcp import FastMCP

mcp = FastMCP("Demo 🚀")

@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

def main():
    print("Hello from fm-mcp!")
    # mcp.run()
    mcp.run(transport="streamable-http", host="0.0.0.0", port=8000, path="/mcp")

if __name__ == "__main__":
    main()
