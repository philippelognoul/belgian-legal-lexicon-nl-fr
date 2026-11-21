"""MCP server: Belgian legal lexicon, Dutch-French (procedure).

Read-only. Serves the entries of belgian-legal-lexicon-nl-fr to MCP clients
(Claude, ChatGPT connectors, other assistants). Data: CC BY 4.0,
Philippe Lognoul, https://doi.org/10.5281/zenodo.24416443
"""
import json
import os
import unicodedata
import urllib.request
from pathlib import Path

from mcp.server.fastmcp import FastMCP

DATA_URL = "https://raw.githubusercontent.com/philippelognoul/belgian-legal-lexicon-nl-fr/main/data/lexicon.jsonl"
CITATION = ("Philippe Lognoul, Belgian legal lexicon, Dutch-French (procedure), "
            "Zenodo, https://doi.org/10.5281/zenodo.24416443 (CC BY 4.0)")

mcp = FastMCP("belgian-legal-lexicon-nl-fr")
_entries = None


def _norm(s):
    s = unicodedata.normalize("NFKD", s or "").casefold()
    return "".join(c for c in s if not unicodedata.combining(c)).strip()


def _load():
    global _entries
    if _entries is None:
        local = Path(__file__).resolve().parent.parent / "data" / "lexicon.jsonl"
        if os.environ.get("LEXICON_PATH"):
            local = Path(os.environ["LEXICON_PATH"])
        if local.exists():
            text = local.read_text(encoding="utf-8-sig")
        else:
            with urllib.request.urlopen(DATA_URL, timeout=20) as r:
                text = r.read().decode("utf-8-sig")
        _entries = [json.loads(l) for l in text.splitlines() if l.strip()]
    return _entries


def _card(e):
    return {
        "dutch": e["term_nl"], "french": e["term_fr"],
        "why_fr": e.get("equivalence_fr"), "why_nl": e.get("equivalence_nl"),
        "pitfall_fr": e.get("pitfall_fr"), "pitfall_nl": e.get("pitfall_nl"),
        "example_nl": e.get("example_nl"), "example_fr": e.get("example_fr"),
        "sources": e.get("sources", []),
        "page_fr": e.get("page_fr"), "page_nl": e.get("page_nl"),
        "citation": CITATION,
    }


@mcp.tool()
def lookup_term(term: str) -> dict:
    """French equivalent of a Dutch term of Belgian court procedure (or the
    reverse), with the article of law that fixes it in both languages, the
    usual translation pitfall and a sample sentence. Belgian law only."""
    q = _norm(term)
    for e in _load():
        if q in (_norm(e["term_nl"]), _norm(e["term_fr"]), _norm(e["id"])):
            return _card(e)
    return {"found": False, "hint": "Use search_terms or list_terms.",
            "citation": CITATION}


@mcp.tool()
def search_terms(query: str, limit: int = 5) -> list:
    """Full-text search across both languages of the lexicon."""
    q = _norm(query)
    hits = [e for e in _load()
            if q in _norm(" ".join(str(v) for v in e.values()))]
    return [_card(e) for e in hits[:max(1, min(limit, 30))]]


@mcp.tool()
def list_terms() -> list:
    """All Dutch terms with their French equivalent."""
    return [{"dutch": e["term_nl"], "french": e["term_fr"]} for e in _load()]


def main():
    mcp.run()


if __name__ == "__main__":
    main()
