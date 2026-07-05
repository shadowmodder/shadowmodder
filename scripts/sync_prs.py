#!/usr/bin/env python3
"""
Fetch PR statuses and update the profile README.
Only MERGED PRs appear in the README table.
Open PRs are tracked in PORTFOLIO.md (blog repo) — not touched here.
"""
import json, re, urllib.request, urllib.error, os

PRs = [
    ("EleutherAI/lm-evaluation-harness", 3913, "ECE + RMS calibration metrics"),
    ("vibrantlabsai/ragas", 2816, "NDCG, MRR, Precision@K, Recall@K retrieval metrics"),
    ("BerriAI/litellm", 32198, "`stream_chunk_builder` KeyError on missing `choices`"),
    ("BerriAI/litellm", 32199, "`reasoning_tokens` forced to `0` in Responses API proxy"),
    ("BerriAI/litellm", 32200, "Async cache streaming drops `reasoning_content`"),
    ("BerriAI/litellm", 32205, "`previous_response_id` double-encoded in MCP tool loops"),
    ("langchain-ai/langchain", 38680, "Streaming tool call fires prematurely with empty args"),
    ("huggingface/peft", 3391, "`update_and_allocate` unreachable after `inject_adapter_in_model`"),
    ("huggingface/trl", 6297, "NaN logprobs crash in GRPO trainer with vLLM importance sampling"),
    ("567-labs/instructor", 2412, "`Optional[NestedModel]` fields stored as raw dicts in streaming partials"),
]

HEADERS = {"Accept": "application/vnd.github+json", "X-GitHub-Api-Version": "2022-11-28"}
token = os.environ.get("GH_TOKEN") or os.environ.get("GITHUB_TOKEN")
if token:
    HEADERS["Authorization"] = f"Bearer {token}"


def get_pr_info(repo, number):
    url = f"https://api.github.com/repos/{repo}/pulls/{number}"
    req = urllib.request.Request(url, headers=HEADERS)
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            return json.loads(resp.read())
    except Exception:
        return None


merged_rows = []
open_count = 0

for repo, num, desc in PRs:
    data = get_pr_info(repo, num)
    if not data:
        print(f"  ⚠️  Could not fetch {repo}#{num}")
        continue

    repo_name = repo.split("/")[1]
    url = f"https://github.com/{repo}/pull/{num}"

    if data.get("merged_at"):
        merged_at = data["merged_at"][:10]  # YYYY-MM-DD
        merged_rows.append(
            f"| [#{num}]({url}) | [{repo_name}](https://github.com/{repo}) | {desc} | ✅ {merged_at} |"
        )
        print(f"  ✅ Merged  {repo}#{num}")
    elif data.get("state") == "open":
        open_count += 1
        print(f"  🟢 Open    {repo}#{num}")
    else:
        print(f"  ❌ Closed  {repo}#{num}")

# Build table content
if merged_rows:
    header = "| PR | Repository | Description | Merged |\n|---|---|---|---|"
    table = header + "\n" + "\n".join(merged_rows)
else:
    table = f"| *(none merged yet — {open_count} open PRs in review)* | | | |"

full_table = f"| PR | Repository | Description | Merged |\n|---|---|---|---|\n{chr(10).join(merged_rows)}" if merged_rows else f"| PR | Repository | Description | Merged |\n|---|---|---|---|\n| *(none merged yet — {open_count} open PRs in review)* | | | |"

with open("README.md") as f:
    content = f.read()

new_content = re.sub(
    r"<!-- PR-STATUS-START -->.*?<!-- PR-STATUS-END -->",
    f"<!-- PR-STATUS-START -->\n{full_table}\n<!-- PR-STATUS-END -->",
    content,
    flags=re.DOTALL,
)

with open("README.md", "w") as f:
    f.write(new_content)

print(f"\nDone: {len(merged_rows)} merged, {open_count} open.")
