#!/usr/bin/env python3
"""Fetch PR statuses from GitHub API and update the README between marker comments."""
import json, re, urllib.request, urllib.error

PRs = [
    ("EleutherAI/lm-evaluation-harness", 3913, "ECE + RMS calibration metrics"),
    ("vibrantlabsai/ragas", 2816, "NDCG, MRR, Precision@K, Recall@K retrieval metrics"),
    ("BerriAI/litellm", 32198, "`stream_chunk_builder` KeyError on missing `choices`"),
    ("BerriAI/litellm", 32199, "`reasoning_tokens` forced to `0` in Responses API proxy"),
    ("BerriAI/litellm", 32200, "Async cache streaming drops `reasoning_content`"),
    ("BerriAI/litellm", 32205, "`previous_response_id` double-encoded in MCP tool loops"),
    ("langchain-ai/langchain", 38678, "Streaming tool call fires prematurely with empty args"),
    ("huggingface/peft", 3391, "`update_and_allocate` unreachable after `inject_adapter_in_model`"),
    ("huggingface/trl", 6296, "NaN logprobs crash in GRPO trainer with vLLM importance sampling"),
]

HEADERS = {"Accept": "application/vnd.github+json", "X-GitHub-Api-Version": "2022-11-28"}

import os
token = os.environ.get("GH_TOKEN") or os.environ.get("GITHUB_TOKEN")
if token:
    HEADERS["Authorization"] = f"Bearer {token}"


def get_pr_status(repo, number):
    url = f"https://api.github.com/repos/{repo}/pulls/{number}"
    req = urllib.request.Request(url, headers=HEADERS)
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read())
        if data.get("merged_at"):
            return "✅ Merged"
        elif data.get("state") == "open":
            return "🟢 Open"
        else:
            return "❌ Closed"
    except urllib.error.HTTPError as e:
        return f"⚠️ {e.code}"
    except Exception:
        return "⚠️ Unknown"


rows = []
for repo, num, desc in PRs:
    repo_name = repo.split("/")[1]
    status = get_pr_status(repo, num)
    url = f"https://github.com/{repo}/pull/{num}"
    rows.append(f"| [#{num}]({url}) | [{repo_name}](https://github.com/{repo}) | {desc} | {status} |")

header = "| PR | Repository | Description | Status |\n|---|---|---|---|"
table = header + "\n" + "\n".join(rows)

with open("README.md") as f:
    content = f.read()

new_content = re.sub(
    r"<!-- PR-STATUS-START -->.*?<!-- PR-STATUS-END -->",
    f"<!-- PR-STATUS-START -->\n{table}\n<!-- PR-STATUS-END -->",
    content,
    flags=re.DOTALL,
)

with open("README.md", "w") as f:
    f.write(new_content)

print("Updated PR statuses:")
for row in rows:
    print(" ", row.split("|")[-2].strip())
