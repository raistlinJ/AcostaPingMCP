# MCP Ping Server

Simple MCP server in Python that runs ping against IP addresses.

## Requirements

- Python 3.10+
- ping available on PATH

## Windows compatibility

The current implementation uses Unix-style ping flags (`-c` and `-W`) and will not work on Windows as-is. Windows uses different flags (for example, `-n` for count and `-w` for timeout in milliseconds). If you need Windows support, the server code should select the appropriate flags based on the OS.

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Run

```bash
python server.py
```

## Claude Desktop config

Add a server entry to your Claude Desktop config (typically in your user config location):

```json
{
  "mcpServers": {
    "ping": {
      "command": "/absolute/path/to/python",
      "args": ["/absolute/path/to/AcostaPingMCP/server.py"]
    }
  }
}
```

## Tool

- `ping_ip(ip_address, count=4, timeout_sec=4)`: runs ping against the IP address and returns output.
