# MCP Ping Server

Simple MCP server in Python that runs ping against IP addresses.

## Requirements

- Python 3.10+
- Conda (install Miniforge: https://github.com/conda-forge/miniforge)
- ping available on PATH

## Windows compatibility

The current implementation uses Unix-style ping flags (`-c` and `-W`) and will not work on Windows as-is. Windows uses different flags (for example, `-n` for count and `-w` for timeout in milliseconds). If you need Windows support, the server code should select the appropriate flags based on the OS.

## Setup

```bash
conda create -n AcostaMCP python=3.10
conda activate AcostaMCP
pip install -r requirements.txt
```

## Conda env location

By default, conda environments are created under your conda base directory:

- macOS: `~/miniforge3/envs/AcostaMCP` or `~/anaconda3/envs/AcostaMCP`
- Windows: `C:\Users\<you>\miniforge3\envs\AcostaMCP` or `C:\Users\<you>\anaconda3\envs\AcostaMCP`

If you are unsure, run `conda info --base` and look under the `envs` folder.

## Claude Desktop config

Add a server entry to your Claude Desktop config (typically in your user config location):

```json
{
  "mcpServers": {
    "ping": {
      "command": "/absolute/path/to/miniforge3/envs/AcostaMCP/bin/python",
      "args": ["/absolute/path/to/AcostaPingMCP/server.py"]
    }
  }
}
```

## Tool

- `ping_ip(ip_address, count=4, timeout_sec=4)`: runs ping against the IP address and returns output.
