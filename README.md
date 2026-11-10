# Sudhir Vissa

**Founder & CEO, [SAGE7 AI](https://sage7.ai) — a one-person AI company, run like a 65-person org.**

In the last twelve months, one person shipped: four papers (IEEE Access, SSRN), 25 open-source libraries, 13 upstream fixes to vLLM, litellm, mem0 and others, 5,500+ GitHub contributions, a production platform on my own Kubernetes cluster, and agent deployments inside an enterprise finance team. No team. Agents draft everything; I own every decision that touches money, data or a customer, and the audit line is written before anything acts.

That is also the product. SAGE7 builds the trust boundary that lets one accountable person run a fleet of agents — and lets a bank or an insurer do the same at their scale. This page is the working prototype.

Before this: 20 years leading engineering and data-science organizations — Sr. Director at SpotHero (2 teams → 7, 15 → 65 people, two countries), Sr. Director of Applied ML & Data Platforms at Apple (17 engineers), Tier-1 speech services at Amazon Alexa (~1B devices), a decade of devices and connectivity at Motorola/Google/Lenovo. 48 granted patents, 604 citations.

**Operating principle:** the guardrail is the design, not the heroics. Everything below — the leadership record, the papers, the libraries — is the same idea at different scales.

### How one person runs it

**An org chart, not a chatbot.** SAGE7 is staffed like a 65-person company. Every agent has a charter, a scope and the statuses it is allowed to move work into. A manager agent runs the drafting functions; I run the agents that touch production, customers or money myself. Nothing acts without an approval tag, and the audit line is written before the action.

| Function | Who runs it | Gate |
|---|---|---|
| Content, research, visibility | Manager agent → drafting agents | I approve every post; every number traces to a source |
| Outreach and pipeline | Manager agent → outreach agents | I approve every send; nothing goes out from a draft |
| Engineering: code, tests, infra | Agents reporting to me directly | Performance, scalability and architecture gates before merge |
| Customers, production, money | Me | No delegation |

**Repo to production in under 15 minutes.** One standing platform — own Kubernetes cluster, GitOps (ArgoCD), CI that builds and pins images, a namespace and database per product, observability — so a new product goes from first commit to a live URL in under 15 minutes, on infrastructure sized for ~100k customer interactions a day. Agents can only ship through the same gates: performant, scalable, reviewed.

**Customers.** Austin IBN, Intellect Capital Group, AlgebraIT and Upsimpl, plus engagements under NDA in energy (power generation and storage), IT services and staffing, and talent management — FDE-style training, agent-architecture patterns and production delivery. Working on agents that touch money, data or memory? [Reach out](https://sage7.ai/contact).

<p align="center">
  <a href="https://austinibn.com"><img src="https://austinibn.com/wp-content/uploads/2025/02/Logo1.png" height="44" alt="Austin IBN"></a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  <a href="https://algebrait.com"><img src="https://algebrait.com/wp-content/uploads/2025/01/AlgebraIT_Logo_1.png" height="36" alt="AlgebraIT"></a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  <a href="https://upsimpl.com"><img src="https://framerusercontent.com/images/sTWc3y2ttmyCKFgouahqoYNVRE.png" height="26" alt="Upsimpl"></a>
</p>

[sage7.ai/blog](https://sage7.ai/blog) · [LinkedIn](https://linkedin.com/in/sudhirvissa) · [Technical notes](https://shadowmodder.github.io) · sudhir.vissa@sage7.ai

---

<p align="center"><a href="https://sage7.ai/blog/agents-draft-i-approve"><img src="https://sage7.ai/blog/approval-loop.png" width="760" alt="How one person runs SAGE7 at team scale: agents draft, one human approves, a narrow actor executes, audit first."></a></p>

### Leadership record

What changed because I was in the room — the decision, then the result.

| Where | Situation → decision | Result |
|---|---|---|
| **SpotHero** · Sr. Director, Data Science / Insights & Forecasting | Pricing was rule-based and the data org was 15 people in 2 teams. Split ML engineering from data science, stood up a platform team, built the forecasting and experimentation practice, and architected **SpotHero IQ** (precision pricing) plus time-based reservation reselling. | ~6× revenue on the priced inventory by deployment, with measured ROI. Org grew to 7 teams / 65 people across the US and Canada with predictable delivery; KPIs and forecasts set executive pricing and spend decisions. |
| **Apple** · Sr. Director, Applied ML & Data Platforms | Model builders across the org each shipped their own way. Led 17 engineers on two teams to make the governed path the default — versioning, lineage, monitoring and rollback as platform primitives, plus a technical-debt framework. | Shorter model-deployment timelines and higher reliability across dozens of use cases. The same lineage-first idea is now the thesis of my IEEE Access paper. |
| **Amazon Alexa** · Sr. SDM, Alexa Services | Tier-1 services delivering ASR, TTS, speech-to-intent and wake-word models to the whole fleet needed to scale and stay certified. Re-architected on DynamoDB + S3; embedded threat modeling into daily delivery. | ~1B devices served at tens of thousands of TPS with cost-based dynamic scaling; security certification retained through the rebuild. |
| **Uptake** · Director of Engineering, Platform Data Sciences | Enterprise IIoT customers on Tier-1 model-management and DBaaS services with no operating discipline. Managed EMs, TPMs, principals, data scientists and SREs; instituted SLAs/SLOs and monthly cost/reliability reviews. | Operational-excellence controls (rate limiting, load testing, scaling) became routine; an invention-sprint program produced the lab's patent and white-paper portfolio. |
| **Motorola → Google → Lenovo** · Engineering Manager | From kernel Wi-Fi drivers and board bring-up to running 12-engineer connectivity and R&D teams (sensors, indoor positioning, biometrics) with silicon vendors and ODMs across Asia. | A patented cloud-decision geolocation feature shipped in Android M; the group's IP portfolio and ~40 upstream Linux-kernel contributions. |

Also: Head of Engineering at Next Step Dynamics (Sweden) — distributed full-stack, data and ML teams on a GDPR-regulated multi-tenant care platform with edge ML on wearable sensor streams.

**From people who worked with me** ([all recommendations](https://www.linkedin.com/in/sudhirvissa/details/recommendations/))

> "A strong leader that any engineering organization could benefit from … thoughtful in how he grew his engineers."
> — Ashwin Sawh, fellow Director at SpotHero

> "His technical expertise is outstanding, and as a mentor, his guidance is invaluable."
> — Luis M. Antunes, Staff Data Scientist, SpotHero

> "We counted on him as a technical leader for our development team."
> — Roland Labana, CTO Altafid; ex Snap, Google, Motorola

---

### Right now

| Focus | Now |
|---|---|
| memharness | Neutral eval harness for agent memory — vendors shouldn't grade their own homework. Latest verified run: 1,986 questions across the suite |
| Papers | Lineage-aware memory governance (IEEE Access), the autonomous agentic store (SSRN) — full list below |
| SAGE7 AI | Agent trust boundary for teams shipping agents in production. Recent client work (enterprise finance team, 2026): Oracle Fusion AR automation — ~70% of the receivables workload automated, refunds from 3–5 days to under 24h, error rate 12% → under 1%. Shipped eHire (autonomous outbound-sales workflow). |
| Open-source contributions | 13 open PRs, 3 approved — hands-on fixes to the LLM/ML libraries production runs on: litellm, vLLM, lancedb, mem0, qdrant-client, weaviate-python-client (full record at the bottom) |

---

### Papers

One argument, four papers: when an agent acts on money, data or memory, the trust boundary is an architecture decision, not a prompt. *Agentic Store* sets the safety requirements for agents that transact; *Lineage-Aware Memory* says an agent may act on a memory only if its provenance is checked first; *After Attention* works out the market economics when the buyer is an agent; *IT-IFC* keeps PII/PCI from leaking into AI-augmented analytics at ingestion.

| Paper | Venue |
|---|---|
| [Lineage-Aware Memory Governance](https://arxiv.org/abs/2610.07258) | IEEE Access, Oct 2026 ([DOI](https://doi.org/10.1109/ACCESS.2026.3730363)) |
| [The Autonomous Agentic Store: Architecture, Safety Requirements, and a Constitutional AI Deployment Framework for Fully Staffless Physical Retail](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6600538) | SSRN, Apr 2026 |
| [After Attention: The Economics of Markets Where the Buyer Is an Agent](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7516238) | SSRN, Sep 2026 |
| [IT-IFC: Ingestion-Centric Information Flow Control for Preventing PII/PCI Leakage in AI-Augmented BI](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6955238) | SSRN, Jun 2026 |

Earlier articles: *Optimizing Large-Scale MLOps Pipelines for Continuous ML Deployment* (2025), *The Evolution of Cloud-Native Data Pipelines*.

---

### IP/Patent portfolio

48 granted patents, 604 citations. What matters is how often later inventors build on them — the most-cited, by 88. The work spans biometrics, sensing, location, and audio — plus cloud and AI.

| Patent | Cited by |
|---|---|
| [Methods and devices for negotiating performance of control operations with acoustic signals](https://patents.google.com/patent/US10902855B2/en) (US10902855B2) | 88 |
| [Peer-to-peer group re-formation](https://patents.google.com/patent/US9560129B2/en) (US9560129B2) | 55 |
| [Location correlation in a region based on signal strength indications](https://patents.google.com/patent/US10499194B1/en) (US10499194B1) | 28 |
| [Electronic device with gesture actuation of companion devices](https://patents.google.com/patent/US10251056B2/en) (US10251056B2) | 18 |

Full list on [Google Patents](https://patents.google.com/?inventor=Sudhir+Vissa).

---

<details>
<summary><b>Writing — the flagship essay plus 12 technical posts</b></summary>

Essays at [sage7.ai/blog](https://sage7.ai/blog); technical notes at [shadowmodder.github.io](https://shadowmodder.github.io); earlier writing on [Medium](https://medium.com/@sid.vissa).

| Post |
|---|
| [My agents draft. I approve. Nothing acts without a tag.](https://sage7.ai/blog/agents-draft-i-approve) |
| [Your Fraud Model's Scores Are Not Probabilities](https://shadowmodder.github.io/posts/calibration-in-production.html) |
| [RAG Retrieval Isn't a Similarity Problem](https://shadowmodder.github.io/posts/rag-retrieval-isnt-similarity.html) |
| [Running an LLM Gateway in Production](https://shadowmodder.github.io/posts/llm-gateway-production.html) |
| [Streaming LLMs in Production: The Edge Cases That Break Your App](https://shadowmodder.github.io/posts/streaming-llms-production.html) |
| [Fine-Tuning vs. Prompting: A Decision Framework That Doesn't Lie to You](https://shadowmodder.github.io/posts/finetuning-vs-prompting.html) |
| [Claude Code Has No Memory. Here's How to Fix That.](https://shadowmodder.github.io/posts/claude-code-memory-persistence.html) |
| [CLAUDE.md: Everything You Can Put in Claude Code's Memory File](https://shadowmodder.github.io/posts/claude-md-guide.html) |
| [Patenting and Protecting Intellectual Property](https://medium.com/@sid.vissa/patenting-and-protecting-intellectual-property-4266486e2917) |
| [Harnessing the Power of Hybrid Generative-Discriminative Models](https://medium.com/@sid.vissa/harnessing-the-power-of-hybrid-generative-discriminative-models-873fb18a71ee) |
| [Making Informed Hiring Decisions for Software Development](https://medium.com/@sid.vissa/making-informed-hiring-decisions-for-software-development-4c1f59fbfbe7) |
| [Navigating the Data Engineering Space](https://medium.com/@sid.vissa/navigating-the-data-engineering-space-59c7a991340a) |

</details>


---

<details>
<summary><b>Open source — 25 small, dependency-light libraries: eval, threshold, memory, tool loop</b></summary>

Small, dependency-light libraries my teams ship with — the pieces where the decision actually gets made: the eval, the threshold, the memory, the tool loop.

#### Agentic & LLM infrastructure

| Repo | What it does |
|------|--------------|
| [tool-loop](https://github.com/shadowmodder/tool-loop) | Agentic tool-use loop: parallel dispatch, error isolation, auto-schema |
| [mcp-quickserver](https://github.com/shadowmodder/mcp-quickserver) | MCP server template: tools, resources, prompts; stdio + SSE |
| [stream-parse](https://github.com/shadowmodder/stream-parse) | Streaming LLM output parser: incremental JSON, tool-call deltas, SSE |
| [agent-scratchpad](https://github.com/shadowmodder/agent-scratchpad) | Persistent vector memory for agents |
| [prompt-cache-bench](https://github.com/shadowmodder/prompt-cache-bench) | Prompt-caching benchmarks: hit rate, latency, cost |
| [llm-eval-lite](https://github.com/shadowmodder/llm-eval-lite) | Eval harness for LLM/agent outputs (AllOf, AnyOf) |
| [rag-eval](https://github.com/shadowmodder/rag-eval) | RAG eval: chunking, retrieval quality, faithfulness |
| [llm-gateway](https://github.com/shadowmodder/llm-gateway) | Production Anthropic proxy: rate limiting, retry, cost tracking |
| [rag-demo](https://github.com/shadowmodder/rag-demo) | End-to-end RAG demo: BM25 + agent + faithfulness eval |

#### ML evaluation & calibration

| Repo | What it does |
|------|--------------|
| [ml-eval-report](https://github.com/shadowmodder/ml-eval-report) | Classifier eval reports: metrics, ROC/PR, threshold sweep, ECE |
| [calibrate-ml](https://github.com/shadowmodder/calibrate-ml) | Probability calibration: Platt, isotonic, ECE, reliability diagrams |
| [thresholdkit](https://github.com/shadowmodder/thresholdkit) | Operating thresholds under precision / FPR / cost constraints |
| [rankeval](https://github.com/shadowmodder/rankeval) | Ranking metrics: NDCG, MRR, AP@K, P@K, R@K |

#### Production ML & data

| Repo | What it does |
|------|--------------|
| [featurecheck](https://github.com/shadowmodder/featurecheck) | Feature drift (PSI/KS/chi-squared) + schema validation |
| [idgraph](https://github.com/shadowmodder/idgraph) | Identity graphs: synthetic-identity rings + risk scoring |
| [pii-redactor](https://github.com/shadowmodder/pii-redactor) | PII detection & redaction (email, phone, SSN, cards) |
| [capture-qa](https://github.com/shadowmodder/capture-qa) | Image capture-quality gates |
| [modelcard-gen](https://github.com/shadowmodder/modelcard-gen) | Model Card markdown from JSON config |
| [semantic_search](https://github.com/shadowmodder/semantic_search) | Semantic search: SentenceTransformers, Flask, Parquet; Milvus experiment |

#### Systems & infrastructure

| Repo | What it does |
|------|--------------|
| [tps-bench](https://github.com/shadowmodder/tps-bench) | HTTP throughput & p50/p90/p99 latency benchmark |
| [cmsketch](https://github.com/shadowmodder/cmsketch) | Count-Min Sketch: sublinear-memory counters |

</details>


---

<details>
<summary><b>Upstream work — 13 PRs to litellm, vLLM, lancedb, mem0 and others, plus 2013–15 Linux-kernel patches</b></summary>

Correctness and security fixes in the ML/LLM libraries production runs on, plus the kernel work underneath. Also tracked at [PORTFOLIO.md](https://github.com/shadowmodder/shadowmodder.github.io/blob/master/PORTFOLIO.md).

| Contribution | Repository | Date | Status |
|---|---|---|---|
| [fix(proxy): fail startup when a custom guardrail names an instance](https://github.com/BerriAI/litellm/pull/50848) | [BerriAI/litellm](https://github.com/BerriAI/litellm) | 2026-11-10 | Open |
| [fix(python): fetch minimum rank-fusion window per side in hybrid search](https://github.com/lancedb/lancedb/pull/4772) | [lancedb/lancedb](https://github.com/lancedb/lancedb) | 2026-10-30 | Open — approved |
| [fix(users): report Go zero time created_at as None for db users](https://github.com/weaviate/weaviate-python-client/pull/2244) | [weaviate/weaviate-python-client](https://github.com/weaviate/weaviate-python-client) | 2026-11-08 | Open — approved |
| [[Bugfix][Multimodal] Domain-separate content digests and caller uuids in mm hashes](https://github.com/vllm-project/vllm/pull/66473) | [vllm-project/vllm](https://github.com/vllm-project/vllm) | 2026-11-08 | Open — approved |
| [[Frontend][Responses] Reject empty assistant message content with 400 instead of 500](https://github.com/vllm-project/vllm/pull/66475) | [vllm-project/vllm](https://github.com/vllm-project/vllm) | 2026-11-08 | Open |
| [fix(responses): keep overlong system prompts in input on the chat to responses bridge](https://github.com/BerriAI/litellm/pull/50328) | [BerriAI/litellm](https://github.com/BerriAI/litellm) | 2026-11-05 | Open |
| [fix(proxy): redact guardrail-blocked request body from spend logs](https://github.com/BerriAI/litellm/pull/50214) | [BerriAI/litellm](https://github.com/BerriAI/litellm) | 2026-11-05 | Open |
| [test(router): fix direct-call num_retries assertion to match SDK-retry behavior](https://github.com/BerriAI/litellm/pull/49584) | [BerriAI/litellm](https://github.com/BerriAI/litellm) | 2026-11-01 | Open |
| [fix(local): reject non-object payloads on set/overwrite_payload and collection metadata updates](https://github.com/qdrant/qdrant-client/pull/1661) | [qdrant/qdrant-client](https://github.com/qdrant/qdrant-client) | 2026-11-03 | Open |
| [[Frontend][Responses] Accept input_audio content parts in user messages (#47659)](https://github.com/vllm-project/vllm/pull/64851) | [vllm-project/vllm](https://github.com/vllm-project/vllm) | 2026-10-30 | Open |
| [fix: GroundedProposer ignores hand-labeled demos](https://github.com/stanfordnlp/dspy/pull/9979) | [stanfordnlp/dspy](https://github.com/stanfordnlp/dspy) | 2026-07-05 | Open |
| [feat(metrics): add traditional IR metrics — NDCGScore, MRRScore, PrecisionAtK, RecallAtK](https://github.com/explodinggradients/ragas/pull/2816) | [explodinggradients/ragas](https://github.com/explodinggradients/ragas) | 2026-07-05 | Open |
| [feat(metrics): add ECE and RMS calibration error metrics](https://github.com/EleutherAI/lm-evaluation-harness/pull/3913) | [EleutherAI/lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness) | 2026-07-05 | Open |
| [fix(providers): retry empty completion choices across handlers](https://github.com/567-labs/instructor/commit/8da7a13f1babc7c8c6c2896b3734f1f1ae5e65b2) — co-authored, landed via maintainer's #2902 | [567-labs/instructor](https://github.com/567-labs/instructor) | 2026-11-05 | Merged |
| [Add Dockerfile](https://github.com/staart/ui/commit/95e2d6dba73aabb0f37f3a236791726cb726b96a) — merged as PR #1131 | [staart/ui](https://github.com/staart/ui) | 2021-05-09 | Merged |
Kernel work (2013–2015): ~40 Wi-Fi and connectivity patches in Motorola's Android trees — Ghost (Moto X 2013), Clark/MSM8992 (Moto X 2015), MSM8226 (Moto G), Shamu (Nexus 6) — still carried in up to 237 community trees. Authored as `shadowmodder`, `Sudhir C Vissa` and `fjdw67`.

Full list of the upstream commits carrying my name: [GitHub commit search](https://github.com/search?q=%22Sudhir+Vissa%22&type=commits).

</details>

---

### Background

SAGE7 AI (2024– ) · Apple · SpotHero · Next Step Dynamics · Uptake · Amazon Alexa · Motorola / Google / Lenovo (2007–2017). Georgetown, Texas.

M.S. Electrical Engineering, New Jersey Institute of Technology · B.Tech Electronics & Communication, MCET Hyderabad.

Working on agent trust boundaries, agent memory governance or FDE-style AI adoption in your org? [Compare notes](https://sage7.ai/contact).
