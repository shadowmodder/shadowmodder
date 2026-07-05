# Sudhir Vissa

Machine-learning engineer focused on the parts that actually decide whether ML works in production — evaluation, calibration, thresholds, drift, identity/fraud signals, serving, and the tooling around them. Also building production agentic systems: tool loops, MCP servers, streaming parsers, and agent memory.

Small, sharp utilities: one job each, minimal dependencies, tests and CI on every repo.

### Focus
- Production ML platforms — feature pipelines, scoring services, A/B infrastructure, model monitoring
- Identity / fraud / biometrics ML
- LLM & agentic systems — MCP, RAG, eval harnesses, streaming, agent memory, prompt optimization
- Real-time serving & streaming

### Current exploration
- Calibration gaps in production risk models: most deployed fraud scores are uncalibrated, which quietly breaks threshold stability across cohorts
- Ranking quality for RAG retrieval: NDCG/MRR applied to document retrieval surfaces degradations that latency metrics miss entirely
- Prompt caching economics: measuring actual cache hit rates and cost savings in multi-turn agentic workflows

---

### Agentic & LLM infrastructure

| Repo | Lang | What it does |
|------|------|--------------|
| [tool-loop](https://github.com/shadowmodder/tool-loop) | Python | Correct agentic tool-use loop: parallel dispatch, error isolation, auto-schema from Python functions |
| [mcp-quickserver](https://github.com/shadowmodder/mcp-quickserver) | Python | MCP server template: tools, resources, and prompts with stdio and SSE transports |
| [stream-parse](https://github.com/shadowmodder/stream-parse) | Python | Parse streaming LLM output: incremental JSON, markdown blocks, tool-call deltas, SSE events |
| [agent-scratchpad](https://github.com/shadowmodder/agent-scratchpad) | Python | Persistent vector memory for agents: embed, store, retrieve by cosine similarity |
| [prompt-cache-bench](https://github.com/shadowmodder/prompt-cache-bench) | Python | Benchmark prompt caching: cache hit rate, latency delta, cost savings with real measurements |
| [llm-eval-lite](https://github.com/shadowmodder/llm-eval-lite) | Python | Assertion-based eval harness for LLM/agent outputs; composite checks (AllOf, AnyOf) |
| [rag-eval](https://github.com/shadowmodder/rag-eval) | Python | RAG pipeline evaluation: chunking strategies, retrieval quality, answer faithfulness |
| [llm-gateway](https://github.com/shadowmodder/llm-gateway) | Python | Production Anthropic API proxy: token-bucket rate limiting, retry with backoff, cost tracking |
| [rag-demo](https://github.com/shadowmodder/rag-demo) | Python | End-to-end RAG demo: BM25 + tool-loop agent + faithfulness eval + persistent memory |

### ML evaluation & calibration

| Repo | Lang | What it does |
|------|------|--------------|
| [ml-eval-report](https://github.com/shadowmodder/ml-eval-report) | Python | Binary-classifier eval: metrics, ROC/PR + AUC, threshold sweep, Brier score, ECE |
| [calibrate-ml](https://github.com/shadowmodder/calibrate-ml) | Python | Probability calibration: Platt scaling, isotonic regression, ECE, reliability diagram |
| [thresholdkit](https://github.com/shadowmodder/thresholdkit) | Python | Pick operating thresholds under precision / FPR / cost / expected-value constraints |
| [rankeval](https://github.com/shadowmodder/rankeval) | Python | NDCG, MRR, AP@K, P@K, R@K — ranking metrics for search, recommendation, RAG |

### Production ML & data

| Repo | Lang | What it does |
|------|------|--------------|
| [featurecheck](https://github.com/shadowmodder/featurecheck) | Python | Feature drift (PSI/KS/chi-squared) + schema/null/dtype validation |
| [idgraph](https://github.com/shadowmodder/idgraph) | Python | Identity/entity graphs from shared signals; surface synthetic-identity rings + risk scoring |
| [pii-redactor](https://github.com/shadowmodder/pii-redactor) | Python | Detect & redact PII (email, phone, SSN, IP, Luhn-validated cards); custom patterns |
| [capture-qa](https://github.com/shadowmodder/capture-qa) | Python | Image capture-quality gates (sharpness, exposure, resolution) |
| [modelcard-gen](https://github.com/shadowmodder/modelcard-gen) | Python | Generate Model Card markdown from a JSON config |

### Systems & infrastructure

| Repo | Lang | What it does |
|------|------|--------------|
| [tps-bench](https://github.com/shadowmodder/tps-bench) | Go | HTTP throughput & p50/p90/p99 latency benchmark for serving endpoints; warmup + JSON output |
| [cmsketch](https://github.com/shadowmodder/cmsketch) | Rust | Count-Min Sketch: approximate counts over high-cardinality streams; merge + serialization |

---

### Background
20+ years across devices, cloud, and ML — biometrics & sensing at Motorola/Google/Lenovo, real-time services at Amazon Alexa scale, and ML-platform work at SpotHero and Apple (feature pipelines, scoring infrastructure, model monitoring, data-science tooling). ~50 granted patents.

---

Find me on [LinkedIn](https://linkedin.com/in/sudhirvissa).
