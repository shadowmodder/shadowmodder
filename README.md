# Sudhir Vissa

**AI/ML Engineering Exec · Founder & CEO, [SAGE7 AI](https://sage7.ai)** — I build the organizations, platforms and guardrails that let AI act on money, data and customers in production.

| | |
|---|---|
| **Orgs built** | Grew SpotHero's data & ML org from 2 teams / 15 people to 7 teams / 65 across the US and Canada. Now lead the engineering teams building Apple's AI/ML platforms, promoted from ML platform architect to tech lead to delivery leader (Infosys engagement, 2023–present). 100+ engineers, scientists and managers led across Apple, Amazon, Uptake, SpotHero and Motorola/Google/Lenovo. |
| **Scale shipped** | Alexa's Tier-1 model-delivery services to ~1B devices at tens of thousands of TPS · Apple ML platforms behind dozens of production model use cases · Wi-Fi and connectivity in millions of Motorola and Nexus devices. |
| **Business moved** | SpotHero IQ — one of the parking industry's first ML pricing engines, A/B-tested across metro markets — ~6× revenue on the priced inventory. 2026: ~70% of an enterprise finance team's receivables workload automated, refunds from 3–5 days to under 24h. |
| **Recognized work** | ~50 patent grants (US and international), 604 citations · IEEE Access paper on agent-memory governance · fixes merged into vLLM and weaviate. |

**Now:** SAGE7 is where I run the operating model I'd bring to a larger org. Agents draft; an accountable human owns every decision that touches money, data or a customer; the audit line is written before anything acts. Run that way, one person shipped in twelve months: four papers, 25 open-source libraries, 17 upstream fixes to vLLM, litellm, lancedb and others, a production platform on my own Kubernetes cluster, and agent deployments inside an enterprise finance team. SAGE7 sells the same trust boundary to teams — a bank or an insurer — running agents at their scale.

**Operating principle:** the guardrail is the design, not the heroics. Everything below — the leadership record, the papers, the libraries — is the same idea at different scales.

### How one person runs it

**An org chart, not a chatbot.** SAGE7 is staffed like a 65-person company. Every agent has a charter, a scope and the statuses it is allowed to move work into. A manager agent runs the drafting functions; I run the agents that touch production, customers or money myself. Nothing acts without an approval tag, and the audit line is written before the action.

| Function | Who runs it | Gate |
|---|---|---|
| Content, research, visibility | Manager agent → drafting agents | I approve every post; every number traces to a source |
| Outreach and pipeline | Manager agent → outreach agents | I approve every send; nothing goes out from a draft |
| Engineering: code, tests, infra | Agents reporting to me directly — e.g. a nightly PR agent across a portfolio company's 7 repos that scans, fixes and verifies | Performance, scalability and architecture gates before merge; the PR agent is not allowed to merge |
| Customers, production, money | Me | No delegation |

**Repo to production in under 15 minutes.** One standing platform — own Kubernetes cluster, GitOps (ArgoCD), CI that builds and pins images, a namespace and database per product, observability — so a new product goes from first commit to a live URL in under 15 minutes, on infrastructure sized for ~100k customer interactions a day. Agents can only ship through the same gates: performant, scalable, reviewed.

**Customers.** GreenBridge AI (agentic platform for power generation and storage), Austin IBN, Intellect Capital Group, AlgebraIT and Upsimpl, plus engagements under NDA in IT services and staffing, and talent management — FDE-style training, agent-architecture patterns and production delivery. Working on agents that touch money, data or memory? [Reach out](https://sage7.ai/contact).


[sage7.ai/blog](https://sage7.ai/blog) · [LinkedIn](https://linkedin.com/in/sudhirvissa) · [Technical notes](https://shadowmodder.github.io) · sudhir.vissa@sage7.ai

---

<p align="center"><a href="https://sage7.ai/blog/agents-draft-i-approve"><img src="https://sage7.ai/blog/one-person-org.png" width="640" alt="How one person runs SAGE7: one accountable human, a manager agent over the drafting agents, engineering agents shipping through gates to production. Agents draft; nothing acts without an approval tag."></a></p>

### Leadership record

What changed because I was in the room — the decision, then the result.

| Where | Situation → decision | Result |
|---|---|---|
| **SpotHero** · Sr. Director, Data Science / Insights & Forecasting | Pricing was rule-based and the data org was 15 people in 2 teams. Split ML engineering from data science, stood up a platform team, built the forecasting and experimentation practice, and architected **SpotHero IQ** (precision pricing) plus time-based reservation reselling. | ~6× revenue on the priced inventory by deployment, with measured ROI. Org grew to 7 teams / 65 people across the US and Canada with predictable delivery; KPIs and forecasts set executive pricing and spend decisions. |
| **Apple AI/ML Platforms** · Engineering Leader (Infosys engagement, 2023–present) | Progressed from ML platform architect to tech lead to leading the delivery teams. Model builders across the org each shipped their own way. Led 17 engineers on two teams to make the governed path the default — versioning, lineage, monitoring and rollback as platform primitives, plus a technical-debt framework. | Shorter model-deployment timelines and higher reliability across dozens of use cases. The same lineage-first idea is now the thesis of my IEEE Access paper. |
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
| Open-source contributions | 17 upstream PRs, 3 merged, 1 approved — hands-on fixes to the LLM/ML libraries production runs on: vLLM, litellm, lancedb, qdrant-client, weaviate-python-client, instructor (full record at the bottom) |

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

~50 patent grants across the US and other countries, 604 citations. What matters is how often later inventors build on them — the most-cited, by 88. The work spans biometrics, sensing, location, and audio — plus cloud and AI.

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
<summary><b>Upstream work — 17 fixes to the LLM stack production runs on: vLLM, litellm, lancedb, qdrant, weaviate, instructor and the eval libraries (3 merged, 1 approved) · plus Wi-Fi kernel patches still carried in 240+ Android trees</b></summary>

I fix the libraries my own agents run on, at the spots where a quiet bug becomes a wrong answer, a leaked prompt or a bad bill: cache keys that can collide, guardrails that fail open, logs that keep what was blocked, retrieval that under-fetches, errors that come back as the wrong code. Same rule as the rest of this page: fail closed, keep the audit trail clean. Every PR is a small, tested change against a real failure. Also tracked at [PORTFOLIO.md](https://github.com/shadowmodder/shadowmodder.github.io/blob/master/PORTFOLIO.md).

**Serving — [vllm-project/vllm](https://github.com/vllm-project/vllm)**

| Fix | What changes for people running it | Opened | Status |
|---|---|---|---|
| [[Bugfix][Multimodal] Domain-separate content digests and caller uuids in mm hashes](https://github.com/vllm-project/vllm/pull/66473) | Caller-supplied uuids and content digests no longer share one hash space in the multimodal cache | 2026-11-09 | **Merged** |
| [[Bugfix][Compilation] Remove AllReduceFusionPass.\_\_del\_\_ destroying the shared FlashInfer workspace](https://github.com/vllm-project/vllm/pull/67643) | Tearing down one compile pass no longer frees the FlashInfer workspace other passes still use | 2026-11-14 | Open |
| [[Frontend][Responses] Reject empty assistant message content with 400 instead of 500](https://github.com/vllm-project/vllm/pull/66475) | A bad client request returns a 400 the caller can act on, not a server error | 2026-11-09 | Open |
| [[Frontend][Responses] Accept input_audio content parts in user messages](https://github.com/vllm-project/vllm/pull/64851) | Audio inputs work through the Responses API (vLLM issue #47659) | 2026-10-31 | Open |

**Gateway and guardrails — [BerriAI/litellm](https://github.com/BerriAI/litellm)**

| Fix | What changes for people running it | Opened | Status |
|---|---|---|---|
| [fix(proxy): redact guardrail-blocked request body from spend logs](https://github.com/BerriAI/litellm/pull/50214) | A request the guardrail blocked is no longer stored verbatim in spend logs | 2026-11-05 | Open |
| [fix(proxy): fail startup when a custom guardrail names an instance](https://github.com/BerriAI/litellm/pull/50848) | A misconfigured custom guardrail stops the proxy at startup instead of surfacing at request time | 2026-11-10 | Open |
| [fix(main): reject chat completions on decisions-only deployments](https://github.com/BerriAI/litellm/pull/51005) | Chat calls routed to a decisions-only deployment are refused up front | 2026-11-10 | Open |
| [fix(responses): keep overlong system prompts in input on the chat to responses bridge](https://github.com/BerriAI/litellm/pull/50328) | Long system prompts survive the chat → Responses bridge instead of being dropped | 2026-11-06 | Open |
| [test(router): fix direct-call num_retries assertion to match SDK-retry behavior](https://github.com/BerriAI/litellm/pull/49584) | Router retry test asserts the behavior the SDK actually has | 2026-11-01 | Open |

**Retrieval and vector stores**

| Fix | What changes for people running it | Opened | Status |
|---|---|---|---|
| [fix(python): fetch minimum rank-fusion window per side in hybrid search](https://github.com/lancedb/lancedb/pull/4772) | Hybrid search pulls enough candidates from each side for rank fusion · [lancedb/lancedb](https://github.com/lancedb/lancedb) | 2026-10-31 | Open — **approved** |
| [fix(users): report Go zero time created_at as None for db users](https://github.com/weaviate/weaviate-python-client/pull/2244) | Users with no creation time read as None, not year 0001 · [weaviate/weaviate-python-client](https://github.com/weaviate/weaviate-python-client) | 2026-11-09 | **Merged** |
| [fix(batch): stop a stale stream sender from stealing requests after a fast reconnect](https://github.com/weaviate/weaviate-python-client/pull/2262) | After a fast reconnect, a stale batch sender can no longer steal the next request into the dead stream and silently lose the batch · [weaviate/weaviate-python-client](https://github.com/weaviate/weaviate-python-client) | 2026-11-16 | Open |
| [fix(local): reject non-object payloads on set/overwrite_payload and collection metadata updates](https://github.com/qdrant/qdrant-client/pull/1661) | Local mode rejects malformed payloads the way the server does · [qdrant/qdrant-client](https://github.com/qdrant/qdrant-client) | 2026-11-03 | Open |

**Structured output and evaluation**

| Fix | What changes for people running it | Opened | Status |
|---|---|---|---|
| [fix(providers): retry empty completion choices across handlers](https://github.com/567-labs/instructor/pull/2902) | Empty provider completions are retried instead of failing; co-authored, landed via the maintainer's consolidation of my #2864 · [567-labs/instructor](https://github.com/567-labs/instructor) | 2026-11-01 | **Merged** |
| [fix: GroundedProposer ignores hand-labeled demos](https://github.com/stanfordnlp/dspy/pull/9979) | Hand-labeled demos reach the prompt optimizer instead of being skipped · [stanfordnlp/dspy](https://github.com/stanfordnlp/dspy) | 2026-07-05 | Open |
| [feat(metrics): add traditional IR metrics — NDCGScore, MRRScore, PrecisionAtK, RecallAtK](https://github.com/vibrantlabsai/ragas/pull/2816) | Classic ranking metrics alongside LLM-judged RAG metrics · [vibrantlabsai/ragas](https://github.com/vibrantlabsai/ragas) | 2026-07-05 | Open |
| [feat(metrics): add ECE and RMS calibration error metrics](https://github.com/EleutherAI/lm-evaluation-harness/pull/3913) | Measures whether a model's confidence matches its accuracy · [EleutherAI/lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness) | 2026-07-05 | Open |

**Earlier:** [Add Dockerfile](https://github.com/staart/ui/pull/1131) to [staart/ui](https://github.com/staart/ui) (2021, merged).

**Kernel work, 2013–2015.** Wi-Fi and connectivity patches from my Motorola years — roaming events (LFR), PNO scheduled scan, DTIM beacon interval, SoftAP country code, BCMDHD and CNSS bring-up — for the Moto X (Ghost, 2013), Nexus 6 (Shamu) and Moto X Style/Pure (Clark, MSM8992). They are still carried in [LineageOS](https://github.com/LineageOS/android_kernel_motorola_msm8992), CyanogenMod, AOSPA, SlimRoms, OmniROM and 240+ community kernel trees. Authored as `shadowmodder` and `Sudhir C Vissa`.

Full list of the upstream commits carrying my name: [GitHub commit search](https://github.com/search?q=%22Sudhir+Vissa%22&type=commits).

</details>

---

### Background

SAGE7 AI (2024– ) · Apple · SpotHero · Next Step Dynamics · Uptake · Amazon Alexa · Motorola / Google / Lenovo (2007–2017). Georgetown, Texas.

M.S. Electrical Engineering, New Jersey Institute of Technology · B.Tech Electronics & Communication, MCET Hyderabad.

Working on agent trust boundaries, agent memory governance or FDE-style AI adoption in your org? [Compare notes](https://sage7.ai/contact).
