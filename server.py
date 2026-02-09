import ipaddress
import subprocess
from typing import List
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("ping")


def _parse_ip(ip_address: str) -> str:
    if not ip_address:
        raise ValueError("Missing ip_address.")
    try:
        return str(ipaddress.ip_address(ip_address))
    except ValueError as exc:
        raise ValueError(f"Invalid IP address: {ip_address}") from exc


def _clamp(value: int, low: int, high: int) -> int:
    return max(low, min(high, value))


@mcp.tool()
def ping_ip(ip_address: str, count: int = 4, timeout_sec: int = 4) -> str:
    """Run ping against an IP address and return the output."""
    try:
        target = _parse_ip(ip_address)
    except ValueError as exc:
        return str(exc)

    count = _clamp(count, 1, 10)
    timeout_sec = _clamp(timeout_sec, 1, 10)

    args: List[str] = [
        "ping",
        "-n",
        "-c",
        str(count),
        "-W",
        str(timeout_sec * 1000),
        target,
    ]

    try:
        result = subprocess.run(
            args,
            capture_output=True,
            text=True,
            timeout=timeout_sec * count + 2,
            check=False,
        )
    except FileNotFoundError:
        return "ping command not found on PATH."
    except subprocess.TimeoutExpired:
        return "Ping timed out."

    output = (result.stdout or "") + (result.stderr or "")
    output = output.strip()
    if not output:
        return "Ping produced no output."

    return output


if __name__ == "__main__":
    mcp.run()
