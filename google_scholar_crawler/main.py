"""Refresh citation data without replacing the last good value on fetch failure."""
import json
import os
from datetime import datetime, timezone
from pathlib import Path

SCHOLAR_ID = os.environ.get("GOOGLE_SCHOLAR_ID") or "ZTuS-yUAAAAJ"
OUT = Path(__file__).resolve().parent / "results" / "gs_data.json"


def citation_record(author, scholar_id=SCHOLAR_ID):
    """Reject incomplete results; a genuine zero is a valid citation count."""
    count = author.get("citedby")
    if isinstance(count, bool) or not isinstance(count, int) or count < 0:
        raise ValueError("Scholar did not return a valid citation count")
    return {
        "citations": count,
        "scholar_id": scholar_id,
        "updated": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
        "source": "Google Scholar",
    }


def refresh(fetch_author, output=OUT):
    try:
        new = citation_record(fetch_author())
        if output.exists():
            old = json.loads(output.read_text(encoding="utf-8"))
            previous = old.get("citations", old.get("citedby"))
            if (old.get("scholar_id", SCHOLAR_ID) == SCHOLAR_ID
                    and isinstance(previous, int) and previous > 0
                    and new["citations"] < previous * .8):
                raise ValueError("Citation count dropped by more than 20%; review before replacing")
        output.parent.mkdir(parents=True, exist_ok=True)
        temporary = output.with_suffix(".tmp")
        temporary.write_text(json.dumps(new, indent=2) + "\n", encoding="utf-8")
        temporary.replace(output)
        print(f"Saved {new['citations']} citations, updated {new['updated']}")
        return True
    except Exception as error:
        print(f"::warning::Citation refresh failed; retaining saved data. {error}")
        return False


def fetch_author():
    from scholarly import scholarly
    scholarly.set_timeout(20)
    scholarly.set_retries(1)
    author = scholarly.search_author_id(SCHOLAR_ID)
    return scholarly.fill(author, sections=["indices"])


if __name__ == "__main__":
    raise SystemExit(0 if refresh(fetch_author) else 1)
