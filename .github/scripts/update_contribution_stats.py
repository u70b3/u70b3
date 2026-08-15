#!/usr/bin/env python3
"""Update the generated contribution summary in the profile README."""

from __future__ import annotations

import json
import os
from pathlib import Path
import subprocess
import sys


START_MARKER = "<!-- contribution-stats:start -->"
END_MARKER = "<!-- contribution-stats:end -->"
PAGE_SIZE = 100
SEARCH_RESULT_LIMIT = 1_000


def search_page(username: str, page: int) -> dict:
    result = subprocess.run(
        [
            "gh",
            "api",
            "--method",
            "GET",
            "search/issues",
            "-f",
            f"q=is:pr is:merged author:{username}",
            "-F",
            f"per_page={PAGE_SIZE}",
            "-F",
            f"page={page}",
        ],
        check=True,
        stdout=subprocess.PIPE,
        text=True,
    )
    return json.loads(result.stdout)


def set_output(name: str, value: str) -> None:
    output_path = os.environ.get("GITHUB_OUTPUT")
    if output_path:
        with Path(output_path).open("a", encoding="utf-8") as output:
            output.write(f"{name}={value}\n")


def main() -> None:
    if len(sys.argv) not in (2, 3):
        raise SystemExit(f"Usage: {sys.argv[0]} USERNAME [README]")

    username = sys.argv[1]
    readme_path = Path(sys.argv[2] if len(sys.argv) == 3 else "README.md")
    selected_owners = {
        owner.strip().casefold()
        for owner in os.environ.get("CONTRIBUTION_ORGANIZATIONS", "").split(",")
        if owner.strip()
    }
    if not selected_owners:
        raise RuntimeError("CONTRIBUTION_ORGANIZATIONS must list at least one owner")

    repositories: set[str] = set()
    total_results = 0
    merged_pull_requests = 0
    fetched = 0
    page = 1

    while True:
        payload = search_page(username, page)
        if page == 1:
            total_results = int(payload["total_count"])

        items = payload["items"]
        for item in items:
            repository_url = item["repository_url"]
            owner = repository_url.rsplit("/", 2)[-2].casefold()
            if owner in selected_owners:
                merged_pull_requests += 1
                repositories.add(repository_url)
        fetched += len(items)

        if len(items) < PAGE_SIZE or fetched >= min(total_results, SEARCH_RESULT_LIMIT):
            break
        page += 1

    if total_results > SEARCH_RESULT_LIMIT:
        raise RuntimeError(
            "GitHub Search returned more than 1,000 results; "
            "the selected contribution count would not be exact"
        )

    pull_request_label = (
        "pull request" if merged_pull_requests == 1 else "pull requests"
    )
    repository_label = "repository" if len(repositories) == 1 else "repositories"
    summary = (
        f"Selected upstream contributions: {merged_pull_requests} merged "
        f"{pull_request_label} across "
        f"{len(repositories)} {repository_label}."
    )

    original = readme_path.read_text(encoding="utf-8")
    if original.count(START_MARKER) != 1 or original.count(END_MARKER) != 1:
        raise RuntimeError("README must contain exactly one contribution-stats block")

    before, marked = original.split(START_MARKER)
    _, after = marked.split(END_MARKER)
    updated = f"{before}{START_MARKER}\n{summary}\n{END_MARKER}{after}"
    changed = updated != original

    if changed:
        readme_path.write_text(updated, encoding="utf-8")

    set_output("changed", str(changed).lower())
    set_output("pull_requests", str(merged_pull_requests))
    set_output("repositories", str(len(repositories)))
    print(f"{summary} ({'updated' if changed else 'unchanged'})")


if __name__ == "__main__":
    main()
