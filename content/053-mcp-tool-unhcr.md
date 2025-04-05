Title: Vibing with mcp_tool Deployment
Slug: mcp-tool-deployment-vibe
Date: 2025-04-04 18:00
Modified: 2025-04-05 15:00
Category: Blog
Tags: mcp, mcp_tool, coding, unhcr, ai, manus, python
Author: Vibek Raj Maurya
Summary: I built mcp_tool to experiment with MCP—Model Context Protocol using UNHCR’s Refugee Population Statistics, got it running with a little help from Manus.

Lately I’ve been hearing a lot of buzz around <a href="https://modelcontextprotocol.io/docs/concepts/tools" target="_blank"><strong>MCP—Model Context Protocol</strong></a> — and, I had to check it out. A few videos, some docs later, I was in deep.

That’s when I ended up building my first `mcp_tool` that interacts with <a href="https://api.unhcr.org/docs/refugee-statistics.html#api-Default-population" target="_blank">UNHCR’s Refugee Population Statistics</a>. The code lives in my GitHub repo: <a href="https://github.com/rvibek/mcp_unhcr" target="_blank">rvibek/mcp_unhcr</a>, and I even spun up a live server version here: <a href="https://smithery.ai/server/@rvibek/mcp_unhcr" target="_blank">smithery.ai server</a>. I built it with some help from <a href="https://manus.ai" target="_blank">Manus</a> — yep, that pretty wild AI sidekick everyone’s talking about.

The idea behind `mcp_tool` was just to experiment and get a feel for how MCP works, so I picked up the UNHCR RDF as a real-world dataset to try it out with.

The code itself is pretty simple — just some scripts, a bit of config magic, and that MCP layer tying it all together. Manus handled most of the heavy lifting. I had to jump in for some refactoring and troubleshooting — ran into a few errors, of course. After five failed deployments 😅, I finally got it running.

Now I’ve got it plugged into Cline in VSCode, and it’s starting to feel like a real little dev assistant setup. Still early days, but it’s been a fun ride so far.

## How to test MCP project locally

The easy way to get started - install [uv](https://docs.astral.sh/uv/), modern python package manager.

```bash

uv init mcp-server
cd mcp-server
source .venv/bin/activate

## add dependencies
uv add "mcp[cli]" requests

## run app.py
mcp dev /path/to/app.py

```
The server should start on the port 6274

<img src="https://res.cloudinary.com/rvibek-com-np/image/upload/v1743862085/mcp_test_gfb6kw.png" style="width: 100%; max-width: 800px; height: auto; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);" alt="Responsive image with shadow"/>

