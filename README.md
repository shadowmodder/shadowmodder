# Sudhir Vissa

**AI/ML leader. Founder & CEO, [SAGE7 AI](https://sage7.ai).** I build agents you can trust to act — with money, data and memory — and the teams and platforms behind them.

20+ years leading applied ML: Sr. Director of Data Science at SpotHero, ML platform at Apple, real-time services at Amazon Alexa, biometrics at Motorola/Lenovo. 48 granted patents, 22 papers. Current research: *The Autonomous Agentic Store* (SSRN) and lineage-aware agent memory (IEEE Access).

The longer goal: be the person teams call on the hard AI/ML questions — technical *and* organizational. Which eval to trust, where an agent is allowed to act, what "good" looks like when the model is a moving target. The work below is the proof, not the pitch.

**How I work:** agents draft, a human approves, a narrow actor executes, and the audit line is written before the action. Everything here is a working piece of that argument — the libraries my teams ship with, not demos.

[sage7.ai/blog](https://sage7.ai/blog) · [LinkedIn](https://linkedin.com/in/sudhirvissa) · [Technical notes](https://shadowmodder.github.io) · sudhir.vissa@sage7.ai

---

### Right now

- **Upstream contributions** — hands-on bug fixes in the LLM/ML libraries production systems actually run on: litellm, vLLM, lancedb, mem0, qdrant-client, weaviate-python-client. Twelve open PRs, two approved — the table below tracks merges as they land.
- **memharness** — a neutral eval for agent memory, built because vendors grade their own homework. Verified run: 1,986 questions, mean F1 0.416, every question retrieved.
- **Papers** — lineage-aware memory governance (IEEE Access) and the autonomous agentic store (SSRN). Selected papers below.
- **Sage7 AI** — founder & CEO. Building the agent trust boundary: approval loops, audit lines, and memory governance for teams shipping agents in production.

---

### Upstream contributions

Bug fixes shipped to production ML/LLM libraries. Open PRs tracked at [PORTFOLIO.md](https://github.com/shadowmodder/shadowmodder.github.io/blob/master/PORTFOLIO.md). Table below updates automatically each day — merged PRs appear here once landed.

<!-- PR-STATUS-START -->
| PR | Repository | Description | Merged |
|---|---|---|---|
| *(12 open PRs in review, 2 approved)* | | | |
<!-- PR-STATUS-END -->

---

### Merged upstream work (commit record)

The table above only tracks the PRs in the sync script. The commit record shows two more merged upstream contributions:

| Contribution | Repository | Date |
|---|---|---|
| [fix(providers): retry empty completion choices across handlers](https://github.com/567-labs/instructor/commit/8da7a13f1babc7c8c6c2896b3734f1f1ae5e65b2) — co-authored by shadowmodder; my PR #2864, landed via the maintainer's #2902 | [567-labs/instructor](https://github.com/567-labs/instructor) | 2026-11-05 |
| [Add Dockerfile](https://github.com/staart/ui/commit/95e2d6dba73aabb0f37f3a236791726cb726b96a) — merged as PR #1131 | [staart/ui](https://github.com/staart/ui) | 2021-05-09 |

---

### Kernel & devices (Motorola era)

Before the ML work, I shipped in the Android kernel trees at Motorola — Moto X 2013 (Ghost), Moto X 2015 (Clark, MSM8992), Moto G (MSM8226) and Nexus 6 (Shamu). Authored as `shadowmodder` from my Motorola address (`sid@motorola.com`), under the name strings `Sudhir Vissa`, `Sudhir C Vissa` and `fjdw67`. Each row is one unique change; the last column counts the community trees (forks and branches) still carrying it.

| Patch | Date | Role | Devices / branches |
|---|---|---|---|
| [WIFi LFR roaming events from QC](https://github.com/MoKee/android_kernel_motorola_ghost/commit/42905835902165f44bb171524234003cafa8d213) | 2013-04-25 | Authored | 33 |
| [DTIM 5 Beacon interval](https://github.com/emceethemouth/kernel_ghost/commit/4801399f3c2ecae77d3bdd5f66214fad1e8e9f98) | 2013-10-15 | Authored | 12 |
| [SBA from QC for SAP Country code](https://github.com/emceethemouth/kernel_ghost/commit/332b038371e8a646759c9df2f888cd4803178f6e) | 2013-10-23 | Authored | 12 |
| [PNO Sched_scan fix from SR 01332508](https://github.com/DC07/spirit_ghost/commit/ea14913146cd116b55bb56b247ec3e4459b99aa6) | 2013-10-23 | Authored | 13 |
| [shamu_defconfig: Add BCMDHD configuration](https://github.com/CPA-Poke/android_kernel_moto_shamu/commit/d90bb83164d0ed088430b60c9d020595132e5f7c) | 2014-05-22 | Authored | 237 |
| [arm: msm: bcm: remove msm_pcie_status_notify](https://github.com/SaberMod/android_kernel_moto_shamu/commit/3cc91bc41a65f01c5daaaadc32e37e4460513429) | 2014-06-03 | Authored | 237 |
| [8994-bringup-hack: net: cnss: Reset](https://github.com/CyanogenMod/android_kernel_motorola_msm8992/commit/73349158029916d2093a30436bfd817c79ce516c) | 2014-10-23 | Authored | 64 |
| [8994-bringup-hack arm/dt: 8994: Add gpio 112 to cnss node](https://github.com/CyanogenMod/android_kernel_motorola_msm8992/commit/dcb3858728a2f67b6e9b33cee9fbc7a4657bcb8b) | 2014-10-23 | Authored | 64 |
| [arm/dt: 8992: Add gpio 112 to cnss node](https://github.com/CyanogenMod/android_kernel_motorola_msm8992/commit/d2976fcd7e97) | 2015-01-08 | Authored | 32 |
| [additional logging for Clark driver on data stall](https://github.com/HashBang173/qcacld-2.0/commit/12d92b29542b2b20a15cb08c4f9982d67610c2a7) | 2015-04-27 | Authored | 1 |
| [enable packetlogs from ini for data stall](https://github.com/HashBang173/qcacld-2.0/commit/83a479aaca22c8fb00ce57243b7a6acdb14c68e3) | 2015-04-28 | Authored | 1 |
| [Add set Roam trigger support](https://github.com/TeamMoskvich/android_kernel_motorola_msm8226/commit/0222a70c39c7933176e4b52fe20fea14bc5e24eb) | 2013-09-11 | Reviewed-by | 61 |
| [Reading of MAC from UTAG (Clark)](https://github.com/LineageOS/android_kernel_motorola_msm8992/commit/d748b77e92) | 2015-02-13 | Reviewed-by | 35 |

Full list of the upstream commits carrying my name: [GitHub commit search](https://github.com/search?q=%22Sudhir+Vissa%22&type=commits).

---

### Selected papers

| Paper | Venue |
|---|---|
| [Lineage-Aware Memory Governance](https://arxiv.org/abs/2610.07258) | IEEE Access, Oct 2026 ([DOI](https://doi.org/10.1109/ACCESS.2026.3730363)) |
| [The Autonomous Agentic Store](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6600538) | SSRN, Apr 2026 |
| [After Attention](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7516238) | SSRN, Sep 2026 |
| [IT-IFC](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6955238) | SSRN, Jun 2026 |

---

### Patents

48 granted patents — mostly from the Motorola/Google era (biometrics, sensing, mobile devices), plus one from SpotHero (2024). Example: [Peer-to-peer group re-formation](https://patents.google.com/patent/US9560129B2/en) (US9560129B2, granted 2017). Full list on [Google Patents](https://patents.google.com/?inventor=Sudhir+Vissa).

---

### Writing

Essays at [sage7.ai/blog](https://sage7.ai/blog); technical notes at [shadowmodder.github.io](https://shadowmodder.github.io).

| Post | Tags |
|---|---|
| [My agents draft. I approve. Nothing acts without a tag.](https://sage7.ai/blog/agents-draft-i-approve) | agent trust boundary · approval loop · audit |
| [Your Fraud Model's Scores Are Not Probabilities](https://shadowmodder.github.io/posts/calibration-in-production.html) | calibration · production ML · fraud |
| [RAG Retrieval Isn't a Similarity Problem](https://shadowmodder.github.io/posts/rag-retrieval-isnt-similarity.html) | RAG · IR metrics · NDCG · MRR |
| [Running an LLM Gateway in Production](https://shadowmodder.github.io/posts/llm-gateway-production.html) | LLM · rate limiting · cost · caching |
| [Streaming LLMs in Production: The Edge Cases That Break Your App](https://shadowmodder.github.io/posts/streaming-llms-production.html) | streaming · SSE · LangChain · production |
| [Fine-Tuning vs. Prompting: A Decision Framework That Doesn't Lie to You](https://shadowmodder.github.io/posts/finetuning-vs-prompting.html) | fine-tuning · LoRA · RAG · prompting |
| [Claude Code Has No Memory. Here's How to Fix That.](https://shadowmodder.github.io/posts/claude-code-memory-persistence.html) | Claude Code · agent memory · persistence |
| [CLAUDE.md: Everything You Can Put in Claude Code's Memory File](https://shadowmodder.github.io/posts/claude-md-guide.html) | Claude Code · CLAUDE.md · agent memory |

Also on [LinkedIn](https://linkedin.com/in/sudhirvissa).

---

### Open source

Small, dependency-light libraries. Each one is the piece of an agentic or ML system where the decision actually gets made — the eval, the threshold, the memory, the tool loop.

#### Agentic & LLM infrastructure

| Repo | What it does |
|------|--------------|
| [tool-loop](https://github.com/shadowmodder/tool-loop) | Correct agentic tool-use loop: parallel dispatch, error isolation, auto-schema from Python functions |
| [mcp-quickserver](https://github.com/shadowmodder/mcp-quickserver) | MCP server template: tools, resources, and prompts with stdio and SSE transports |
| [stream-parse](https://github.com/shadowmodder/stream-parse) | Parse streaming LLM output: incremental JSON, markdown blocks, tool-call deltas, SSE events |
| [agent-scratchpad](https://github.com/shadowmodder/agent-scratchpad) | Persistent vector memory for agents: embed, store, retrieve by cosine similarity |
| [prompt-cache-bench](https://github.com/shadowmodder/prompt-cache-bench) | Benchmark prompt caching: cache hit rate, latency delta, cost savings with real measurements |
| [llm-eval-lite](https://github.com/shadowmodder/llm-eval-lite) | Assertion-based eval harness for LLM/agent outputs; composite checks (AllOf, AnyOf) |
| [rag-eval](https://github.com/shadowmodder/rag-eval) | RAG pipeline evaluation: chunking strategies, retrieval quality, answer faithfulness |
| [llm-gateway](https://github.com/shadowmodder/llm-gateway) | Production Anthropic API proxy: token-bucket rate limiting, retry with backoff, cost tracking |
| [rag-demo](https://github.com/shadowmodder/rag-demo) | End-to-end RAG demo: BM25 + tool-loop agent + faithfulness eval + persistent memory |

#### ML evaluation & calibration

| Repo | What it does |
|------|--------------|
| [ml-eval-report](https://github.com/shadowmodder/ml-eval-report) | Binary-classifier eval: metrics, ROC/PR + AUC, threshold sweep, Brier score, ECE |
| [calibrate-ml](https://github.com/shadowmodder/calibrate-ml) | Probability calibration: Platt scaling, isotonic regression, ECE, reliability diagram |
| [thresholdkit](https://github.com/shadowmodder/thresholdkit) | Pick operating thresholds under precision / FPR / cost / expected-value constraints |
| [rankeval](https://github.com/shadowmodder/rankeval) | NDCG, MRR, AP@K, P@K, R@K — ranking metrics for search, recommendation, RAG |

#### Production ML & data

| Repo | What it does |
|------|--------------|
| [featurecheck](https://github.com/shadowmodder/featurecheck) | Feature drift (PSI/KS/chi-squared) + schema/null/dtype validation |
| [idgraph](https://github.com/shadowmodder/idgraph) | Identity/entity graphs from shared signals; surface synthetic-identity rings + risk scoring |
| [pii-redactor](https://github.com/shadowmodder/pii-redactor) | Detect & redact PII (email, phone, SSN, IP, Luhn-validated cards); custom patterns |
| [capture-qa](https://github.com/shadowmodder/capture-qa) | Image capture-quality gates (sharpness, exposure, resolution) |
| [modelcard-gen](https://github.com/shadowmodder/modelcard-gen) | Generate Model Card markdown from a JSON config |
| [semantic_search](https://github.com/shadowmodder/semantic_search) | Semantic search over documents: SentenceTransformers embeddings, Flask API, Parquet store; Milvus experiment |

#### Systems & infrastructure

| Repo | What it does |
|------|--------------|
| [tps-bench](https://github.com/shadowmodder/tps-bench) | HTTP throughput & p50/p90/p99 latency benchmark for serving endpoints; warmup + JSON output |
| [cmsketch](https://github.com/shadowmodder/cmsketch) | Count-Min Sketch: approximate counts over high-cardinality streams; merge + serialization |

---

### Background

Apple (ML platform, scoring infrastructure, model monitoring) · SpotHero (Sr. Director of Data Science; built the IQ pricing engine) · Amazon Alexa (on-device fingerprinting, real-time services at Alexa scale) · Motorola / Google / Lenovo (Moto Access biometric platform, ~10 years). Georgetown, Texas.

Working on agent trust boundaries, agent memory governance or FDE-style AI adoption in your org? [Compare notes](https://sage7.ai/contact).
