# Sudhir Vissa

**AI/ML leader. Founder & CEO, [SAGE7 AI](https://sage7.ai).** I build agents you can trust to act — with money, data and memory — and the teams and platforms behind them.

Sr. Director of Data Science at SpotHero (built the IQ pricing engine; grew the org from 2 teams to 6), AI/ML leader at Apple, real-time services at Amazon Alexa (wake-word, ASR, TTS to a ~1B-device fleet), biometrics at Motorola/Lenovo. 42 granted U.S. patents, 604 citations.

The longer goal: build, brick by brick, a high-value company that actually helps people and companies with real AI problems — which eval to trust, where an agent is allowed to act, what "good" looks like when the model is a moving target. The work below is the proof, not the pitch.

**Operating principle:** agents draft, a human approves, a narrow actor executes, and the audit line is written before the action. I run teams the same way — the guardrail is the design, not the heroics.

[sage7.ai/blog](https://sage7.ai/blog) · [LinkedIn](https://linkedin.com/in/sudhirvissa) · [Technical notes](https://shadowmodder.github.io) · sudhir.vissa@sage7.ai

---

### Right now

| Focus | Now |
|---|---|
| memharness | Neutral eval for agent memory — vendors grade their own homework. Verified run: 1,986 questions, every one retrieved |
| Whitepapers | Lineage-aware memory governance (IEEE Access), the autonomous agentic store (SSRN) — full list below |
| Sage7 AI | Agent trust boundary for teams shipping agents in production — Oracle Fusion AR: 70% of receivables automated, refunds under 24h, errors 12% to under 1%; shipped eHire (autonomous sales workflow) |
| Also shipped | [DocuSpark](https://docuspark.ai) (production RAG, Product Hunt), [PicNPlay](https://picnplay.com) (App Store), [forgein](https://forgein.ai) (Claude productivity toolkit), [basics.ai](https://basics.ai), [irohealth.com](https://irohealth.com), [kidkruz.com](https://kidkruz.com), Verra (HR compliance) |
| Open-source contributions | 12 open PRs, 2 approved — hands-on fixes to the LLM/ML libraries production runs on: litellm, vLLM, lancedb, mem0, qdrant-client, weaviate-python-client (full record at the bottom) |

---

### Papers

| Paper | Venue |
|---|---|
| [Lineage-Aware Memory Governance](https://arxiv.org/abs/2610.07258) | IEEE Access, Oct 2026 ([DOI](https://doi.org/10.1109/ACCESS.2026.3730363)) |
| [The Autonomous Agentic Store: Architecture, Safety Requirements, and a Constitutional AI Deployment Framework for Fully Staffless Physical Retail](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6600538) | SSRN, Apr 2026 |
| [After Attention: The Economics of Markets Where the Buyer Is an Agent](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7516238) | SSRN, Sep 2026 |
| [IT-IFC: Ingestion-Centric Information Flow Control for Preventing PII/PCI Leakage in AI-Augmented BI](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6955238) | SSRN, Jun 2026 |

Earlier articles: *Optimizing Large-Scale MLOps Pipelines for Continuous ML Deployment* (2025), *The Evolution of Cloud-Native Data Pipelines*.

---

### IP/Patent portfolio

42 granted U.S. patents, 604 citations. What matters is how often later inventors build on them — the most-cited, by 88. The work spans biometrics, sensing, location, and audio — plus cloud and AI.

| Patent | Cited by |
|---|---|
| [Methods and devices for negotiating performance of control operations with acoustic signals](https://patents.google.com/patent/US10902855B2/en) (US10902855B2) | 88 |
| [Peer-to-peer group re-formation](https://patents.google.com/patent/US9560129B2/en) (US9560129B2) | 55 |
| [Location correlation in a region based on signal strength indications](https://patents.google.com/patent/US10499194B1/en) (US10499194B1) | 28 |
| [Electronic device with gesture actuation of companion devices](https://patents.google.com/patent/US10251056B2/en) (US10251056B2) | 18 |

Full list on [Google Patents](https://patents.google.com/?inventor=Sudhir+Vissa).

---

### Writing

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

---

### Open source

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

---

### Background

Apple (AI/ML leader; ML platform, scoring, model monitoring) · SpotHero (Sr. Director of Data Science; IQ pricing engine; 2 → 6 teams) · Amazon Alexa (wake-word, ASR, TTS to a ~1B-device fleet) · Motorola / Google / Lenovo (Moto Access biometrics, ~10 years). Georgetown, Texas.

M.S. Electrical Engineering, New Jersey Institute of Technology · B.Tech Electronics & Communication, MCET Hyderabad.

Working on agent trust boundaries, agent memory governance or FDE-style AI adoption in your org? [Compare notes](https://sage7.ai/contact).

### Upstream work

Correctness and security fixes in the ML/LLM libraries production runs on — plus the kernel work underneath. One record, open PRs through kernel patches. Also tracked at [PORTFOLIO.md](https://github.com/shadowmodder/shadowmodder.github.io/blob/master/PORTFOLIO.md).

| Contribution | Repository | Date | Status |
|---|---|---|---|
| [fix(python): fetch minimum rank-fusion window per side in hybrid search](https://github.com/lancedb/lancedb/pull/4772) | [lancedb/lancedb](https://github.com/lancedb/lancedb) | 2026-10-30 | Open — approved |
| [fix(users): report Go zero time created_at as None for db users](https://github.com/weaviate/weaviate-python-client/pull/2244) | [weaviate/weaviate-python-client](https://github.com/weaviate/weaviate-python-client) | 2026-11-08 | Open — approved |
| [[Bugfix][Multimodal] Domain-separate content digests and caller uuids in mm hashes](https://github.com/vllm-project/vllm/pull/66473) | [vllm-project/vllm](https://github.com/vllm-project/vllm) | 2026-11-08 | Open — CI ready |
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
| [WIFi LFR roaming events from QC](https://github.com/MoKee/android_kernel_motorola_ghost/commit/42905835902165f44bb171524234003cafa8d213) | Ghost | 2013-04-25 | Authored · 33 trees |
| [DTIM 5 Beacon interval](https://github.com/emceethemouth/kernel_ghost/commit/4801399f3c2ecae77d3bdd5f66214fad1e8e9f98) | Ghost | 2013-10-15 | Authored · 12 trees |
| [SBA from QC for SAP Country code](https://github.com/emceethemouth/kernel_ghost/commit/332b038371e8a646759c9df2f888cd4803178f6e) | Ghost | 2013-10-23 | Authored · 12 trees |
| [PNO Sched_scan fix from SR 01332508](https://github.com/DC07/spirit_ghost/commit/ea14913146cd116b55bb56b247ec3e4459b99aa6) | Ghost | 2013-10-23 | Authored · 13 trees |
| [shamu_defconfig: Add BCMDHD configuration](https://github.com/CPA-Poke/android_kernel_moto_shamu/commit/d90bb83164d0ed088430b60c9d020595132e5f7c) | Shamu | 2014-05-22 | Authored · 237 trees |
| [arm: msm: bcm: remove msm_pcie_status_notify](https://github.com/SaberMod/android_kernel_moto_shamu/commit/3cc91bc41a65f01c5daaaadc32e37e4460513429) | Shamu | 2014-06-03 | Authored · 237 trees |
| [8994-bringup-hack: net: cnss: Reset](https://github.com/CyanogenMod/android_kernel_motorola_msm8992/commit/73349158029916d2093a30436bfd817c79ce516c) | MSM8992 | 2014-10-23 | Authored · 64 trees |
| [8994-bringup-hack arm/dt: 8994: Add gpio 112 to cnss node](https://github.com/CyanogenMod/android_kernel_motorola_msm8992/commit/dcb3858728a2f67b6e9b33cee9fbc7a4657bcb8b) | MSM8992 | 2014-10-23 | Authored · 64 trees |
| [arm/dt: 8992: Add gpio 112 to cnss node](https://github.com/CyanogenMod/android_kernel_motorola_msm8992/commit/d2976fcd7e97) | MSM8992 | 2015-01-08 | Authored · 32 trees |
| [additional logging for Clark driver on data stall](https://github.com/HashBang173/qcacld-2.0/commit/12d92b29542b2b20a15cb08c4f9982d67610c2a7) | qcacld-2.0 | 2015-04-27 | Authored · 1 tree |
| [enable packetlogs from ini for data stall](https://github.com/HashBang173/qcacld-2.0/commit/83a479aaca22c8fb00ce57243b7a6acdb14c68e3) | qcacld-2.0 | 2015-04-28 | Authored · 1 tree |
| [Add set Roam trigger support](https://github.com/TeamMoskvich/android_kernel_motorola_msm8226/commit/0222a70c39c7933176e4b52fe20fea14bc5e24eb) | MSM8226 | 2013-09-11 | Reviewed-by · 61 trees |
| [Reading of MAC from UTAG (Clark)](https://github.com/LineageOS/android_kernel_motorola_msm8992/commit/d748b77e92) | MSM8992 | 2015-02-13 | Reviewed-by · 35 trees |

Kernel work: Android trees at Motorola — Ghost (Moto X 2013), Clark/MSM8992 (Moto X 2015), MSM8226 (Moto G), Shamu (Nexus 6). Authored as `shadowmodder` (`sid@motorola.com`), also as `Sudhir C Vissa` and `fjdw67`. Status counts the community trees still carrying each change.

Full list of the upstream commits carrying my name: [GitHub commit search](https://github.com/search?q=%22Sudhir+Vissa%22&type=commits).
