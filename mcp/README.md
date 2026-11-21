# Belgian legal lexicon — MCP server

Read-only server that lets an assistant (Claude, ChatGPT and any MCP client) look up the Dutch terms of Belgian court procedure in this lexicon, with their French equivalent, the article of law that fixes it in both languages, the usual pitfall and a sample sentence.

Tools: `lookup_term`, `search_terms`, `list_terms`. No account, no write access, no personal data.

## Install (Claude Desktop and other MCP clients)

```json
{
  "mcpServers": {
    "belgian-legal-lexicon": {
      "command": "uvx",
      "args": ["--from", "git+https://github.com/philippelognoul/belgian-legal-lexicon-nl-fr#subdirectory=mcp", "belgian-legal-lexicon-mcp"]
    }
  }
}
```

Installed this way, the server fetches `data/lexicon.jsonl` from this repository; run from a clone, it reads the local file.

Author: Philippe Lognoul, translator since 1992 (ORCID 0009-0000-3951-5667). Data: CC BY 4.0. Cite: https://doi.org/10.5281/zenodo.24416443. Belgian law only; a translation aid, not legal advice.
